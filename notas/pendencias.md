# Pendências antes da entrega (situação em 16/11/2026)

Meta interna: 23/11. Prazo: 07/12.
Cada pessoa lê a sua parte do artigo com os PDFs de `ep2_export/` abertos. Confira cada número no localizador citado,
refaça as "contas nossas" e reescreva com as suas palavras o que não soar seu. Só apague um `\revisar{...}` depois de
validar o trecho.
Lista atualizada: `grep -n '\\revisar' artigo/artigo.tex entrega/entrega.tex`. Os números de linha abaixo mudam
conforme o texto é editado; procure pelo texto da marca.

Se usar Gemini, ChatGPT ou outra IA, siga a seção "Uso de outras IAs" do `CLAUDE.md`: a conversa inteira vai para
`logs/ext_<AAAAMMDD>_<autor>_<ferramenta>.md`.
Prompts prontos para colar (crítica de seção e leitura de artigo): `notas/prompts_outras_ias.md`.

## Gabriel: I Introdução, II Método, IV-B Memória, VII Conclusão, referências
- [x] artigo l.96 (II-A): confirmar as bases e as strings de busca que o grupo de fato usou.
- [x] artigo l.101 (II-A): retirar do texto o nome do artigo descartado.
- [x] artigo l.103 (II-A): justificar o corte em 2018 com o motivo real do grupo.
- [x] artigo l.429 (IV-B): conferir a conta do Tree Bitmap na p. 120 do eath04 (128 B × 10 milhões = 1,28 GB, contra os 1,6 GB do artigo).
- [x] Conferir as Tabelas I a IV contra os PDFs.
- [x] `artigo/refs.bib`: conferir cada entrada contra a primeira página do PDF (autores, título, ano, DOI).

## Ana: IV-A Velocidade, IV-C Atualização
- [ ] artigo l.354 (IV-A): confirmar no yang18 qual tráfego foi usado na Fig. 14. O verificador não achou.
- [ ] artigo l.468 (IV-C): conferir no yang18 se o bloqueio do lookup descrito no §III-C (SAIL_B) vale também para o SAIL_L.
- [ ] artigo l.472 (IV-C): conferir no §4.9 do asai15 se os 2,51 µs incluem a atualização da radix.
- [ ] artigo l.482 (IV-C): na Tab. 1 do shah01 (p. 43), confirmar que "Prefixes" = Inserts + Deletes.
- [ ] Conferir a Fig. 1 e a Tabela V contra os PDFs (II e III conferidas pelo Gabriel em 16/11).
- [ ] entrega l.104: a sua linha na declaração (ferramenta, modelo, datas; ou "não usou IA").

## Diogo: III Fundamentos, IV-D Energia, IV-E Escala e IPv6, V Discussão, VI Limitações
- [ ] artigo l.520 (IV-D): refazer a conta da potência do CoolCAMs (125.288 entradas → cerca de 3,6 W).
- [ ] artigo l.523 (IV-D): refazer a conta dos chips de TCAM do Tree Bitmap (cerca de 39 chips com entradas de 72 bits).
- [ ] artigo l.536 (IV-E): conferir na Tab. IV do yang18, que é imagem no PDF, os valores 114.069 (2002) e 495.401 (2013).
- [ ] artigo l.658 (VI): refazer a conta dos "9 bits" da Tab. 5 do eath04.
- [ ] artigo l.664 (VI): completar com o resultado da revisão do grupo.
- [ ] Conferir a Tabela VI contra os PDFs.
- [ ] entrega l.105: a sua linha na declaração (ferramenta, modelo, datas; ou "não usou IA").

## Os três juntos, depois das revisões
- [ ] artigo l.135 (II-B): quem leu cada artigo e quem conferiu cada inferência e cada "conta nossa".
- [ ] artigo l.159 (II-C): o que o grupo mudou no rascunho e quem revisou cada seção.
- [ ] entrega l.119–125 (tabela da declaração): coluna "O que o grupo fez", sobre fichamentos, referências, rascunho, estilo, verificação e LaTeX.
- [ ] entrega l.140: erros que a revisão do grupo encontrou.
- [ ] entrega l.142: "O que é do grupo", com as palavras do grupo. Cada um escreve a sua parte; a do Gabriel inclui
  busca, organização, decisões de tese e de enquadramento, fechamento.
- [ ] entrega l.148: confirmar ou retirar a frase sobre logs de outras IAs.

## Fechamento (Gabriel, uma vez, no fim)
0. Data da entrega na capa (entrega l.57), no dia da entrega.
1. Pedir ao Claude Code para rodar o agente `verificador-citacoes` no texto final e corrigir o que vier divergente.
2. `grep -c '\\revisar' artigo/artigo.tex entrega/entrega.tex`: deve dar 1 em cada arquivo, que é a definição do comando.
3. `/log-ia`, depois `cd artigo && latexmk -pdf artigo.tex` (`pdfinfo`: de 8 a 12 páginas) e `cd entrega && latexmk -lualatex entrega.tex`.
4. Abrir `entrega/entrega.pdf` inteiro, fazer commit e push, e entregar.
