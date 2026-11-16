---
name: log-ia
description: Exporta as sessões reais do Claude Code deste projeto para logs/cc_*.md, a parte 2 da entrega do EP2 (log completo de prompts e respostas). Use ao fim de cada sessão de trabalho e antes de compilar a entrega.
---

# /log-ia

O enunciado exige o log completo das conversas com a IA. Esta skill exporta o que está gravado nos
transcripts (JSONL) do Claude Code. Não se escreve log à mão.

1. Descubra quem está usando a máquina. Pergunte se não souber: Gabriel, Ana ou Diogo.
2. Rode na raiz do repositório:
   `python3 -I .claude/skills/log-ia/export_log.py --autor <Nome>`
   O script grava um `logs/cc_<data>_<autor>.md` por sessão e refaz `logs/sessoes.tex`, o índice que a entrega usa.
3. Confira o resultado sem editar o conteúdo:
   - `grep -c '^## Interação' logs/cc_*.md` mostra quantas interações cada sessão tem;
   - faça um grep pelo e-mail de quem está usando: ele não pode aparecer;
   - abra o arquivo novo e confira se o primeiro prompt da sessão aparece inteiro.
4. Se o script falhar porque o formato do JSONL mudou, conserte o script e rode `--selftest`.
   Não conserte o log à mão.
5. Faça commit de `logs/` junto com o restante da etapa.

Política, que não muda: nenhuma interação é inventada, editada ou removida. Os logs do claude.ai
(`logs/01_*`, `logs/02_*`) são cópias exatas dos arquivos originais.
