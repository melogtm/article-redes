#!/usr/bin/env python3
"""Exporta as sessões do Claude Code deste projeto para Markdown, no formato dos logs do EP2.

Lê os JSONL que o Claude Code grava em ~/.claude/projects/<pasta-do-projeto>/ e escreve
logs/cc_<AAAAMMDD_HHMM>_<autor>.md (uma sessão por arquivo) e logs/sessoes.tex (índice para a entrega).
Prompts e respostas saem como estão no transcript; nada é resumido nem reescrito.
Fica de fora: system-reminders, hooks, metadados da sessão, raciocínio interno e a saída bruta das ferramentas.

Uso:  python3 -I .claude/skills/log-ia/export_log.py --autor Gabriel
      python3 -I .claude/skills/log-ia/export_log.py --selftest
"""
import argparse, base64, glob, json, os, re, sys, tempfile
from datetime import datetime, timedelta, timezone

BRT = timezone(timedelta(hours=-3))
LIXO = re.compile(r'<(system-reminder|local-command-caveat)>.*?</\1>\s*', re.S)
CMD = re.compile(r'<command-name>(.*?)</command-name>.*?<command-args>(.*?)</command-args>', re.S)
STDOUT = re.compile(r'<local-command-stdout>(.*?)</local-command-stdout>', re.S)
ANEXO = {'file': 'filename', 'pdf_reference': 'filename', 'directory': 'path'}
HOME = os.path.expanduser('~')


def curto(p, raiz):
    return os.path.relpath(p, raiz) if p.startswith(raiz + os.sep) else p.replace(HOME, '~', 1)


def texto(c):
    if isinstance(c, str):
        return c
    return '\n'.join(b.get('text', '') for b in c or [] if b.get('type') == 'text')


def narracao(b):
    """Bloco 'thinking' que guarda a fala mostrada na tela (assinatura do tipo 'narration')."""
    s = b.get('signature', '')
    try:
        return bool(b.get('thinking')) and b'narration' in base64.b64decode(s + '=' * (-len(s) % 4))
    except ValueError:
        return False


def acao(nome, e, raiz):
    if nome == 'Bash':
        return 'Bash: ' + (e.get('description') or e.get('command', '')[:80])
    if nome in ('Read', 'Write', 'Edit'):
        return f"{nome} `{curto(e.get('file_path', ''), raiz)}`" + (f" (p. {e['pages']})" if e.get('pages') else '')
    if nome == 'Skill':
        return f"skill `{e.get('skill')}`"
    if nome == 'WebSearch':
        return f'busca na web "{e.get("query")}"'
    if nome == 'WebFetch':
        return f"leitura de {e.get('url')}"
    return nome


def citar(s):
    return '\n'.join('> ' + l if l.strip() else '>' for l in s.strip().splitlines())


def data(ts):
    return datetime.fromisoformat(ts.replace('Z', '+00:00')).astimezone(BRT)


def relatorio(o):
    """Texto do relatório de um subagente em segundo plano (vem em 'origin', fora da fala do usuário)."""
    if o.get('handbackReportText'):
        return o['handbackReportText']
    corpo = o.get('body', '')
    if '[Subagent hand-back]' not in corpo or 'The report follows:\n' not in corpo:
        return None
    return '\n'.join(l[2:] if l.startswith('  ') else l for l in corpo.split('The report follows:\n', 1)[1].splitlines())


def le_sessao(caminho, raiz):
    inter, pend, notas, meta, atual = [], {}, [], {}, None
    agentes, entregues = {}, set()
    for linha in open(caminho, encoding='utf-8'):
        d = json.loads(linha)
        t, m = d.get('type'), d.get('message') or {}
        a = d.get('attachment') or {}
        o = d.get('origin') or a.get('origin') or {}
        if o.get('kind') == 'peer' and (r := relatorio(o)) and atual is not None and o.get('from') not in entregues:
            entregues.add(o.get('from'))
            tipo, desc = agentes.get(o.get('from'), (o.get('name', 'subagente'), ''))
            atual['itens'].append(('claude', f"**Relatório do subagente `{tipo}`" + (f" ({desc})" if desc else '')
                                   + ', entregue em segundo plano:**\n\n' + citar(r)))
            continue
        if t == 'attachment':
            if atual and not atual['itens'] and a.get('type') in ANEXO:
                atual['anexos'].append(os.path.basename(a[ANEXO[a['type']]].rstrip('/')))
            continue
        if t not in ('user', 'assistant') or d.get('isSidechain') or d.get('isMeta'):
            continue
        if d.get('isCompactSummary'):
            if atual is not None:
                atual['itens'].append(('resumo', texto(m.get('content')).strip()))
            continue
        meta.setdefault('versao', d.get('version'))
        if m.get('model'):
            meta.setdefault('modelo', m['model'])
        c = m.get('content')
        if t == 'user' and isinstance(c, list) and any(b.get('type') == 'tool_result' for b in c):
            for b in c:
                nome, e = pend.pop(b.get('tool_use_id'), (None, None))
                r = texto(b.get('content')).strip()
                if nome == 'AskUserQuestion':
                    resp = (d.get('toolUseResult') or {}).get('answers') or {}
                    ls = [f"{i}. {resp.get(q['question'], '(sem resposta)')}" for i, q in enumerate(e.get('questions', []), 1)]
                    atual['itens'].append(('usuario', '\n'.join(ls) if resp else r))
                elif nome == 'ExitPlanMode':
                    atual['itens'].append(('usuario', '*Aprovou o plano.*' if 'approved your plan' in r else r))
                elif nome == 'Agent':
                    res = d.get('toolUseResult') or {}
                    if res.get('status') == 'async_launched':
                        # o relatório chega depois, como mensagem do subagente (ver relatorio())
                        agentes[res.get('agentId')] = (e.get('subagent_type', 'general-purpose'), e.get('description', ''))
                    else:
                        atual['itens'].append(('claude', '**Relatório do subagente:**\n\n' + citar(r)))
            continue
        if t == 'user':
            s = LIXO.sub('', texto(c)).strip()
            if (k := CMD.search(s)):
                notas.append(f"comando local `{(k.group(1) + ' ' + k.group(2)).strip()}`")
            elif (k := STDOUT.search(s)):
                if notas:
                    notas[-1] += f" ({k.group(1).strip()})"
            elif s:
                ts = data(d['timestamp'])
                meta.setdefault('inicio', ts)
                atual = {'data': ts.strftime('%d/%m/%Y %H:%M'), 'prompt': s, 'anexos': [], 'itens': [], 'notas': notas}
                notas = []
                inter.append(atual)
            continue
        if atual is None:
            continue
        for b in c if isinstance(c, list) else []:
            ty = b.get('type')
            if ty == 'text' and b['text'].strip():
                atual['itens'].append(('claude', b['text'].strip()))
            elif ty == 'thinking' and narracao(b):
                atual['itens'].append(('claude', b['thinking'].strip() + ' *(narração)*'))
            elif ty == 'tool_use':
                n, e = b['name'], b.get('input') or {}
                if n in ('AskUserQuestion', 'ExitPlanMode', 'Agent'):
                    pend[b['id']] = (n, e)
                if n == 'AskUserQuestion':
                    qs = [f"{i}. {q['question']} Opções: " + '; '.join(o['label'] for o in q.get('options', []))
                          for i, q in enumerate(e.get('questions', []), 1)]
                    atual['itens'].append(('claude', '**Perguntas da IA:**\n\n' + '\n'.join(qs)))
                elif n == 'ExitPlanMode':
                    atual['itens'].append(('claude', '**Plano apresentado para aprovação:**\n\n' + citar(e.get('plan', ''))))
                elif n == 'Agent':
                    atual['itens'].append(('acao', f"subagente `{e.get('subagent_type', 'general-purpose')}`: {e.get('description', '')}"))
                    atual['itens'].append(('claude', '**Prompt enviado ao subagente:**\n\n' + citar(e.get('prompt', ''))))
                else:
                    atual['itens'].append(('acao', acao(n, e, raiz)))
    return inter, meta


def render(inter, meta, autor):
    out = [f"# Sessão do Claude Code: {autor}, {meta['inicio'].strftime('%d/%m/%Y')}", '',
           f"- Ferramenta: Claude Code {meta.get('versao')}, modelo `{meta.get('modelo')}`", '']
    for i, it in enumerate(inter, 1):
        out += [f"## Interação {i}: {it['data']}", '', f'### {autor}', '']
        if it['notas']:
            out += ['*' + '; '.join(it['notas']) + '.*', '']
        out += [it['prompt'], '']
        if it['anexos']:
            out += ['Anexos: ' + ', '.join(f'`{a}`' for a in it['anexos']) + '.', '']
        quem, acoes = autor, []
        for tipo, s in it['itens'] + [('fim', '')]:
            if tipo == 'acao':
                if quem != 'Claude':
                    out += ['### Claude', '']
                    quem = 'Claude'
                acoes.append(s)
                continue
            if acoes:
                out += ['*Ações da IA: ' + '; '.join(acoes) + '.*', '']
                acoes = []
            if tipo == 'fim':
                break
            if tipo == 'resumo':
                out += ['### Resumo automático de contexto (Claude Code)', '',
                        '*O contexto da conversa encheu e o Claude Code gerou o resumo abaixo, que passou a substituir as '
                        'mensagens anteriores para o modelo. Não foi digitado pelo usuário.*', '', citar(s), '']
                quem = 'resumo'
                continue
            fala = 'Claude' if tipo == 'claude' else autor
            if fala != quem:
                out += [f'### {fala}', '']
                quem = fala
            out += [s, '']
    return '\n'.join(out)


def exporta(raiz, autor, pasta):
    logs = os.path.join(raiz, 'logs')
    for f in sorted(glob.glob(os.path.join(pasta, '*.jsonl'))):
        inter, meta = le_sessao(f, raiz)
        if inter:
            nome = f"cc_{meta['inicio'].strftime('%Y%m%d_%H%M')}_{autor.lower()}.md"
            with open(os.path.join(logs, nome), 'w', encoding='utf-8') as o:
                o.write(render(inter, meta, autor))
            print('gravado', os.path.join('logs', nome), f'({len(inter)} interações)')
    # cc_<AAAAMMDD_HHMM>_<autor>.md (Claude Code) e ext_<AAAAMMDD>_<autor>_<ferramenta>.md (outras IAs, copiados à mão), por data
    idx = sorted((os.path.basename(p) for p in glob.glob(os.path.join(logs, 'cc_*.md')) + glob.glob(os.path.join(logs, 'ext_*.md'))),
                 key=lambda n: n.split('_', 1)[1])
    with open(os.path.join(logs, 'sessoes.tex'), 'w', encoding='utf-8') as o:
        o.write(''.join(f'\\markdownInput{{../logs/{n}}}\n\\clearpage\n' for n in idx))


def selftest():
    sig = lambda tag: base64.b64encode(b'\x08' + tag).decode()
    linhas = [
        {'type': 'user', 'timestamp': '2026-11-16T13:00:00Z', 'version': '9.9', 'message': {'content':
            '<command-name>/effort</command-name>\n<command-message>effort</command-message>\n<command-args></command-args>'}},
        {'type': 'user', 'timestamp': '2026-11-16T13:00:00Z', 'message': {'content': '<local-command-stdout>ok</local-command-stdout>'}},
        {'type': 'user', 'timestamp': '2026-11-16T13:00:01Z', 'message': {'content': 'Pedido <system-reminder>segredo</system-reminder>real'}},
        {'type': 'attachment', 'attachment': {'type': 'file', 'filename': '/x/enunciado.pdf'}},
        {'type': 'attachment', 'attachment': {'type': 'session_context', 'context': {'userEmail': 'NAO-VAZAR'}}},
        {'type': 'assistant', 'message': {'model': 'm1', 'content': [
            {'type': 'thinking', 'thinking': 'interno', 'signature': sig(b'thinking')},
            {'type': 'thinking', 'thinking': 'fala resumida', 'signature': sig(b'narration')},
            {'type': 'tool_use', 'id': 'a', 'name': 'Bash', 'input': {'description': 'Lista arquivos'}},
            {'type': 'tool_use', 'id': 'q', 'name': 'AskUserQuestion', 'input': {'questions': [{'question': 'Q1?', 'options': [{'label': 'Sim'}]}]}}]}},
        {'type': 'user', 'toolUseResult': {'answers': {'Q1?': 'Resposta do usuário'}}, 'message': {'content': [
            {'type': 'tool_result', 'tool_use_id': 'a', 'content': 'saída bruta'},
            {'type': 'tool_result', 'tool_use_id': 'q', 'content': 'The user answered'}]}},
        {'type': 'assistant', 'message': {'content': [{'type': 'text', 'text': 'Resposta final.'},
            {'type': 'tool_use', 'id': 'g', 'name': 'Agent', 'input': {'subagent_type': 'leitor', 'description': 'Fichar X', 'prompt': 'Leia X'}}]}},
        {'type': 'user', 'toolUseResult': {'status': 'async_launched', 'agentId': 'ag1'}, 'message': {'content': [
            {'type': 'tool_result', 'tool_use_id': 'g', 'content': 'Async agent launched. agentId: ag1 METADADO'}]}},
        {'type': 'user', 'isCompactSummary': True, 'timestamp': '2026-11-16T13:05:00Z', 'message': {'content': 'This session is being continued RESUMO'}},
        {'type': 'attachment', 'attachment': {'type': 'queued_command', 'prompt': '<agent-message from="ag1">...', 'origin': {
            'kind': 'peer', 'from': 'ag1', 'name': 'leitor', 'body': '[Subagent hand-back] aviso. The report follows:\n  Relatório real\n  linha 2'}}},
        {'type': 'user', 'isMeta': True, 'origin': {'kind': 'peer', 'from': 'ag1', 'handbackReportText': 'Relatório real\nlinha 2'},
         'message': {'content': 'duplicado'}},
    ]
    with tempfile.TemporaryDirectory() as tmp:
        f = os.path.join(tmp, 's.jsonl')
        with open(f, 'w') as o:
            o.write('\n'.join(json.dumps(l) for l in linhas))
        inter, meta = le_sessao(f, tmp)
    md = render(inter, meta, 'Gabriel')
    for ok in ('Pedido real', '`enunciado.pdf`', 'comando local `/effort` (ok)', 'fala resumida *(narração)*',
               '*Ações da IA: Bash: Lista arquivos.*', 'Q1? Opções: Sim', '1. Resposta do usuário', 'Resposta final.', 'Claude Code 9.9',
               '### Resumo automático de contexto (Claude Code)', '> This session is being continued RESUMO',
               '**Relatório do subagente `leitor` (Fichar X), entregue em segundo plano:**\n\n> Relatório real\n> linha 2'):
        assert ok in md, (ok, md)
    for nao in ('segredo', 'NAO-VAZAR', 'interno', 'saída bruta', 'METADADO', 'duplicado', 'aviso'):
        assert nao not in md, (nao, md)
    assert len(inter) == 1 and md.count('Relatório real') == 1
    print('selftest ok')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--autor')
    ap.add_argument('--raiz', default=os.getcwd())
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        selftest()
        sys.exit()
    if not a.autor:
        ap.error('--autor é obrigatório')
    raiz = os.path.abspath(a.raiz)
    exporta(raiz, a.autor, os.path.join(HOME, '.claude', 'projects', re.sub(r'[^A-Za-z0-9]', '-', raiz)))
