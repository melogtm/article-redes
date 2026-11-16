# EP2 Redes: revisão crítica sobre lookup de rota (LPM), TCAM × algoritmos

ACH2026 Redes de Computadores (EACH/USP). Grupo: Gabriel Trigueiro Melo (15511832),
Ana Vitória Chaves Viana (12733869), Diogo dos Santos da Rocha (13673281).
Prazo improrrogável: 07/12/2026. Meta interna: 23/11/2026.
Enunciado: `ep2_export/enunciado_trabalho_redes.pdf`. Leia antes de qualquer tarefa de escrita.

## Entrega: um PDF (`entrega/entrega.pdf`)
1. Artigo de revisão crítica no formato IEEE, em duas colunas, com 8 a 12 páginas contando as referências (`artigo/`).
2. Log completo de prompts e respostas com a IA (`logs/`).
3. Declaração de uso de IA: modelo, versão e finalidade de cada uso.

O enunciado dá nota zero para texto gerado só por IA sem revisão crítica profunda, para referência
falsa ou inexistente e para uso de IA ocultado.

## Corpus (PDFs em `ep2_export/`, fora do git por copyright)
| id | arquivo | artigo |
|---|---|---|
| ruiz01 | `Survey_and_taxonomy_of_IP_address_lookup_algorithms.pdf` | Ruiz-Sánchez, Biersack, Dabbous. IEEE Network, 2001 |
| shah01 | `Fast_updating_algorithms_for_TCAM.pdf` | Shah, Gupta. IEEE Micro, 2001 |
| zane03 | `Coolcams_power-efficient_TCAMs_for_forwarding_engines.pdf` | Zane, Narlikar, Basu. INFOCOM 2003 |
| eath04 | `997150.997160.pdf` | Eatherton, Varghese, Dittia. Tree Bitmap, CCR 2004 |
| zec12 | `2378956.2378961.pdf` | Zec, Rizzo, Mikuc. DXR, CCR 42(5), 2012 (versão publicada) |
| asai15 | `2785956.2787474.pdf` | Asai, Ohara. Poptrie, SIGCOMM 2015 |
| yang18 | `Sail_2_ToN_18.pdf` | Yang et al. Constant IP Lookup With FIB Explosion (SAIL), IEEE/ACM ToN 2018 |

Slides da disciplina (`08CamRede*.pdf`, `09CamRede3.pdf`) servem só para alinhar a terminologia.

## Regras para a IA neste projeto
- Referência só entra se o PDF estiver em `ep2_export/`. O BibTeX sai do DOI impresso no PDF ou dos metadados
  oficiais do DOI (doi.org/Crossref), nunca de memória. Trabalho citado sem PDF leva a marca `[NÃO VERIFICADO]`.
- Toda afirmação sobre um artigo tem localizador da versão publicada: seção, figura, tabela ou página.
  Número de preprint ou de relatório técnico não vale (ver `logs/02_correcoes_01_11_2026.md`).
- Separe o que o artigo afirma da inferência. No texto do artigo, a inferência aparece como tal ("nossa leitura").
- Antes de chamar duas fontes de contraditórias, confira cenário, plataforma, tráfego, métrica e premissa.
- Os números dos logs de 31/10 e 01/11 vieram da IA. Confira cada um de novo no PDF antes de usar.
- `\revisar{...}` (vermelho) marca o que o grupo ainda precisa validar. Não remova sem o grupo pedir.
- Log: nunca invente, edite ou omita interações. As sessões do Claude Code são exportadas com `/log-ia`.
- Estilo: português, direto, sem elogio genérico. Evite linguagem inflada, tríades forçadas, construções
  "não é X, é Y", excesso de travessões e frase de efeito no fim do parágrafo. A skill `humanizer` faz esse passe.

## Agentes e skills
- `.claude/agents/leitor-artigo.md`: fichamento de um PDF em `notas/fichamentos/<id>.md`.
- `.claude/agents/verificador-citacoes.md`: confere número e localizador do `.tex` contra os PDFs e grava `notas/verificacao.md`.
- `.claude/agents/revisor-critico.md`: lê o artigo como o professor leria e grava `notas/revisao_critica.md`.
- `.claude/skills/log-ia/`: `/log-ia` exporta as sessões do Claude Code para `logs/cc_*.md`.
- `humanizer` (skill do usuário): revisão de estilo da prosa, sem mudar números nem citações.

## Build
```
cd artigo  && latexmk -pdf artigo.tex        # 8 a 12 páginas: pdfinfo artigo.pdf
cd entrega && latexmk -lualatex entrega.tex  # capa + artigo + log + declaração
grep -c '\\revisar' artigo/artigo.tex        # o que falta o grupo validar
```

## Uso de outras IAs (Gemini, ChatGPT etc.)
- Toda conversa entra no log. Ao fim de cada uma, copie a conversa inteira (prompts e respostas, sem resumir nem cortar)
  para `logs/ext_<AAAAMMDD>_<autor>_<ferramenta>.md`. No topo, informe a ferramenta, o nome do modelo exibido na tela, a data, o autor
  e o link de compartilhamento. Copie no mesmo dia, porque conversa apagada não volta. Antes do commit, retire dados pessoais (e-mail, telefone).
- `/log-ia` inclui esses arquivos na Parte II em ordem de data. Declare a ferramenta e o modelo na Parte III (`entrega/entrega.tex`).
- As regras acima valem para qualquer IA. Referência só com PDF em `ep2_export/` e BibTeX tirado do DOI. Número só com localizador
  conferido no PDF. Trecho escrito com outra IA só entra no `.tex` depois de passar pelo agente `verificador-citacoes`.
  Use essas IAs para pedir crítica e explicação, não texto pronto.
