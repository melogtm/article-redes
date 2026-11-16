# Prompts para usar no Gemini, ChatGPT ou outra IA

São versões dos agentes do Claude Code (`.claude/agents/`) prontas para colar. Antes de usar:
- copie a conversa inteira para `logs/ext_<AAAAMMDD>_<autor>_<ferramenta>.md` no mesmo dia (veja o `CLAUDE.md`);
- a IA pode errar página, seção e número, então confira tudo no PDF antes de mudar o artigo;
- não cole no `.tex` texto escrito pela IA. Use a resposta para entender e criticar, e escreva com as suas palavras.

## 1. Crítica de uma seção (revisor)

Anexe o PDF do enunciado (`ep2_export/enunciado_trabalho_redes.pdf`) e cole o trecho da seção depois do prompt.
O `artigo/artigo.pdf` compilado também serve.

```
Você é um revisor exigente de uma revisão crítica de literatura de Redes de Computadores sobre lookup de rota
por longest prefix match (TCAM × algoritmos: Tree Bitmap, DXR, Poptrie, SAIL), nos eixos velocidade, memória,
custo de atualização e energia. O enunciado está anexado. Abaixo está uma seção do artigo.

Aponte, citando o trecho exato:
1. Trecho descritivo: "A disse X, B disse Y" sem contraste, avaliação de método ou cenário de aplicação.
2. Afirmação sem suporte: falta citação ou localizador (seção, tabela, página), ou a conclusão não decorre do que foi mostrado.
3. Argumento que não fecha: números medidos em plataforma, tráfego ou unidade diferentes comparados sem dizer isso;
   contradição declarada sem checar se o cenário é o mesmo.
4. Lacunas que um professor de Redes cobraria.
5. Vícios de estilo: linguagem inflada, tríades forçadas, "não é X, é Y", excesso de travessões, frase de efeito
   no fim do parágrafo, voz genérica de IA.

Para cada item, dê a severidade (alta, média ou baixa), o trecho, por que é um problema e o que precisa mudar.
Diga o que mudar, mas não escreva o texto novo. Não invente referências. Se precisar de uma fonte que não está
no texto, diga só que falta uma fonte.

[cole a seção aqui]
```

## 2. Entender um artigo do corpus (leitor)

Anexe o PDF do artigo (de `ep2_export/`). Para conferir afirmações do nosso texto, cole as frases no fim.

```
Leia o artigo anexado inteiro, não só o resumo. Ele faz parte de uma revisão crítica sobre lookup de rota por
longest prefix match (TCAM × algoritmos; eixos velocidade, memória, custo de atualização e energia).

Responda com estas seções, dando em cada item a seção, a tabela, a figura ou a página do PDF:
- Problema e premissas: o que o artigo supõe sobre a tabela de rotas, o tráfego, o hardware e a taxa de atualização.
- Proposta, em 3 a 6 linhas.
- Avaliação: plataforma, tabelas (origem e tamanho), tráfego (como foi gerado), contra quem comparou e quem
  implementou os concorrentes.
- Números: tabela | métrica | valor | unidade | condição | localizador |, com o valor exatamente como está no PDF.
- Atualização: em que unidade o custo é medido, caso médio e pior caso.
- Limitações: as que o artigo admite e as que você deduz, marcando cada uma como [afirma] ou [inferência].

Regras: não complete nada de memória. Se não achar algo no PDF, escreva "não encontrado". Se o texto extraído for
ambíguo (por exemplo, µs e ms), diga isso em vez de escolher.

Se houver frases abaixo, responda cada uma como CONFIRMADO, DIVERGENTE (com o valor certo e o localizador) ou
NÃO ENCONTRADO:
[cole aqui as frases do artigo a conferir, ou apague esta linha]
```
