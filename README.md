# EP2 Redes: TCAM ou algoritmo? Revisão crítica do lookup por longest prefix match

Exercício Prático 2 de ACH2026 Redes de Computadores (EACH/USP). O tema é uma revisão crítica de literatura,
com uso obrigatório de IA generativa, sobre lookup de rota por LPM: TCAM contra Tree Bitmap, DXR, Poptrie e SAIL,
nos eixos velocidade, memória, custo de atualização e energia.

Grupo: Gabriel Trigueiro Melo (15511832), Ana Vitória Chaves Viana (12733869) e Diogo dos Santos da Rocha (13673281).
Prazo: 07/12/2026.

## Entrega

Um PDF, `entrega/entrega.pdf`, com três partes:
1. o artigo no formato IEEE, em duas colunas, com 8 a 12 páginas contando as referências (`artigo/`);
2. o log completo de prompts e respostas com a IA (`logs/`);
3. a declaração de uso de IA (modelo, versão e finalidade), escrita em `entrega/entrega.tex`.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `artigo/artigo.tex`, `artigo/refs.bib` | Artigo (IEEEtran) e referências, com BibTeX tirado dos DOIs |
| `entrega/entrega.tex` | Capa, artigo, log e declaração num PDF só |
| `logs/` | `01_*` e `02_*`: conversas do claude.ai; `cc_*`: sessões do Claude Code (exportadas); `ext_*`: conversas com outras IAs (copiadas à mão) |
| `notas/fichamentos/` | Fichamento de cada um dos 7 artigos, com localizadores |
| `notas/estrutura.md` | Tese, estrutura e decisões do grupo |
| `notas/revisao_critica.md`, `notas/verificacao.md` | Relatórios do revisor crítico e do verificador de citações |
| `notas/pendencias.md` | O que falta validar antes da entrega, por integrante |
| `notas/prompts_outras_ias.md` | Prompts para usar no Gemini ou no ChatGPT |
| `CLAUDE.md` | Regras do projeto para a IA (referências, localizadores, log, estilo) |
| `.claude/agents/`, `.claude/skills/log-ia/` | Agentes do Claude Code (leitor, verificador, revisor) e o exportador do log |
| `ep2_export/` | PDFs dos artigos. Só o enunciado está no git; os artigos ficam fora por direitos autorais |

## Como compilar

Requer TeX Live com `texlive-publishers` (IEEEtran), `texlive-lang-portuguese` e LuaLaTeX.
O documento de entrega inclui o PDF do artigo, então compile o artigo primeiro.

```
cd artigo  && latexmk -pdf artigo.tex        # conferir: pdfinfo artigo.pdf (8 a 12 páginas)
cd entrega && latexmk -lualatex entrega.tex
```

Para atualizar o log das sessões do Claude Code antes de compilar, rode `/log-ia` dentro do Claude Code, ou
`python3 -I .claude/skills/log-ia/export_log.py --autor <Nome>` na raiz.

## Regras para trabalhar no texto

- Uma referência só entra se o PDF estiver em `ep2_export/`, com o BibTeX tirado do DOI.
- Toda afirmação sobre um artigo precisa de localizador da versão publicada: seção, tabela, figura ou página.
- Inferência do grupo aparece como tal no texto ("nossa leitura", "conta nossa").
- `\revisar{...}` (em vermelho no PDF) marca o que ainda precisa ser validado. Só apague depois de validar.
  Para ver o que falta: `grep -n '\\revisar' artigo/artigo.tex entrega/entrega.tex`.
- Toda conversa com IA entra no log, sem edição nem corte. Conversas com outras IAs seguem a seção
  "Uso de outras IAs" do `CLAUDE.md`.
