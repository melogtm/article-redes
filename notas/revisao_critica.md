# Revisão crítica do rascunho: `artigo/artigo.tex` (versão de 16/11/2026)

Revisor: agente `revisor-critico` (Claude Opus 5.5, Claude Code), lendo como o professor de ACH2026 leria.
Referência dos critérios: `ep2_export/enunciado_trabalho_redes.pdf` (seções 3, 4 e 5) e `CLAUDE.md`.
Números de linha: `artigo/artigo.tex` com 606 linhas. Os números de PDF citados aqui foram conferidos
no texto extraído dos PDFs de `ep2_export/` e nos fichamentos; ainda assim, confira cada um antes de usar.

## Build e aparência

- `latexmk -pdf artigo.tex` sem erro; nenhuma *overfull box*; duas *underfull* no parágrafo das linhas 438-441 (sem efeito visível).
- **9 páginas em A4**, com as referências. A última página tem só um terço ocupado. Cabe no intervalo de 8 a 12, e sobram
  cerca de 3 páginas para tratar as lacunas da seção D sem estourar o limite.
- Tabela I (p. 3): legível, com localizadores em todas as células, menos a linha do zane03 na última coluna.
- Tabela II (p. 4): a coluna "Valor" quebra número e unidade em duas linhas ("179,92 / Mlps", "231,47– / 236,08 / Mpps"),
  e "Tree / Bitmap" e "DXR / D16R" também quebram. O Tree Bitmap aparece em "M/s" e os demais em Mlps.
- Tabela III (p. 4): a primeira coluna hifeniza "concor-rentes", e as linhas "Tráfego aleatório" e "Tráfego real" encostam
  uma na outra sem espaço, o que faz as duas parecerem uma célula só.
- Fig. 1 (p. 4): legível, escala log correta, e as razões invertidas conferem (1/1,14 = 0,877; 1122/1264 = 0,888; 480/492 = 0,976).
  O problema dela é de conteúdo (C6).
- Tabelas V e VI (pp. 6 e 8): legíveis. A Tabela VI não tem linhas entre os cenários, e as células de 3 a 4 linhas ficam densas.
- Referências: 7 entradas IEEE completas (autores, título, veículo, volume, número, páginas, ano). O texto escreve "Ruiz-Sánchez"
  e a referência [1], "Ruiz-Sanchez". Os DOIs estão no `.bib`, mas o estilo não os imprime.

## Avaliação da tese

A tese combina (1) "os números publicados não são comparáveis diretamente" e (2) "normalizados por cenário, mostram quem
ganha em cada cenário". Hoje o texto não sustenta as duas sem contradição:

- **(1) está com a causa errada.** O resumo (l. 38-40) e a introdução (l. 74-75) atribuem a não comparabilidade ao fato de
  que "cada artigo mede com rigor o eixo em que a proposta é forte". O corpo do texto desmente isso para três dos sete artigos:
  o CoolCAMs não mede potência (l. 457), o Tree Bitmap não traz nenhuma medição de taxa (l. 339-341), e o Shah e Gupta conta
  movimentos em simulação (Tabela I). O que a Seção IV de fato demonstra é outra coisa: plataforma, tabela, tráfego,
  implementação do rival e definições de "memória" e "custo de atualização" diferentes.
- **(2) não tem procedimento.** "Normalizar por cenário" aparece no resumo (l. 40) e na introdução (l. 75), mas nem a Seção II-B
  nem a V dizem o que foi normalizado, nem como. Nenhum número é posto numa base comum: a Fig. 1 mostra razões medidas por
  cada artigo na sua própria plataforma. O critério da Tabela VI ("mais bem sustentada") também não é "vence", que é a palavra
  do título da Seção V (l. 512) e do resumo/introdução (l. 76, "mostram onde cada solução vence").
- **O corpo viola (1)** em pelo menos quatro lugares (C1, C3, C4, C5) e compara diretamente números de plataformas diferentes.
- **Vereditos condicionados por eixo:**
  - IV-A: só a parte Poptrie × SAIL termina com veredito (l. 327-332), e a parte do tráfego aleatório não fecha (C2).
    A subseção sobre DXR, Tree Bitmap e TCAM termina com "Nenhum artigo algorítmico mede uma TCAM real" (l. 343-344), sem
    veredito sobre TCAM × algoritmo, que é a pergunta do título.
  - IV-B: há veredito (l. 380-382), apoiado numa inferência (B9).
  - IV-C: há veredito (l. 432-435), mas compara grandezas de unidades diferentes e erra o "único limite" (C4, B6).
  - IV-D: há veredito modesto e coerente (l. 468-472).
  - IV-E: o veredito é negativo (l. 507-509), e a Tabela VI e a Conclusão o contradizem (A1).

---

## A. Vereditos da Tabela VI e da Conclusão sem apoio na Seção IV

**A1. Alta. Tabela VI, linha 529, e Conclusão, linha 592: IPv6.**
Trechos: "Roteador em software ou NFV em x86, tráfego de borda com prefixos longos, IPv4 e IPv6 & Poptrie" (l. 529);
"O Poptrie leva vantagem com prefixos longos e IPv6" (l. 592).
Problema: a Seção IV-E conclui que "No IPv6, a evidência é fraca em todas as famílias" (l. 496) e que nenhuma abordagem tem
evidência "para IPv6 em escala de produção" (l. 507). A Seção V afirma que "Os cenários com IPv6 [...] ficaram fora da tabela"
(l. 544). Na mesma tabela, no entanto, o IPv6 aparece como cenário do Poptrie, apoiado num teste com 20.440 prefixos que os
próprios autores chamam de "less interesting" (l. 503).
O que mudar: tirar o IPv6 da linha do Poptrie e da Conclusão, ou rebaixar a afirmação ao nível que a IV-E sustenta. A frase da
l. 544 e a tabela precisam dizer a mesma coisa.

**A2. Alta. Tabela VI, linha 528: SAIL\_L em "FIB crescendo".**
Problema: a IV-E mostra que, nas maiores tabelas sintéticas, o SAIL não compila (l. 483-487) e que a correção "não foi medida"
(l. 487). A própria IV-E fecha com "inclusive no SAIL, que se apresenta como independente do tamanho da FIB" (l. 508-509).
A tabela, porém, recomenda o SAIL justamente para FIB crescendo, e a coluna de ressalva não menciona o limite de 15 bits.
A evidência "M (CPU, FPGA simulado)" também não cobre o cenário: o cenário é ASIC/FPGA, e no FPGA o SAIL não foi comparado com
nenhum concorrente (yang18 §VI-B, segundo o fichamento). A comparação com o Poptrie foi feita em CPU.
O que mudar: pôr o limite de formato e a correção não medida na ressalva; dizer que a vantagem medida sobre os concorrentes
é de CPU; e explicar por que o SAIL vence nesse cenário e contra quem, em especial contra a TCAM, que é a alternativa natural
em hardware de backbone.

**A3. Alta. Tabela VI, linha 532, e Conclusão, linhas 593-595: TCAM para "determinismo e gerência simples".**
Problema: nenhuma subseção da IV discute determinismo da TCAM, e a "gerência simples" contradiz o próprio texto. A Seção III-B
(l. 185-186) e a IV-B (l. 354-355) dizem que a TCAM depende de um software de gerência com trie auxiliar fora do chip, e a
IV-C (l. 429-430) mostra que o custo da ordenação e o do particionamento nunca foram medidos juntos. A única fonte de "simples
de gerenciar" é o resumo do CoolCAMs (l. 67, sem localizador), isto é, a autodescrição de uma das partes, coisa que o artigo
critica nos outros. Além disso, "tabelas pequenas ou médias" é a faixa em que a TCAM *foi testada* (35 a 122 mil), não uma faixa
em que se mostrou que ela vence. Na Conclusão, "continua defensável" é uma afirmação sobre o presente apoiada em dispositivos de
2001 a 2004 (a l. 573 admite isso).
O que mudar: ou apoiar determinismo e gerência na Seção IV com fonte e localizador, ou tirar os dois da tabela e da Conclusão.
Separar "faixa testada" de "faixa em que vence". Tirar o "continua" ou qualificar a data dos dados.

**A4. Média. Tabela VI, linha 533: linha do híbrido.**
Problema: a tabela se chama "Abordagem mais bem sustentada por cenário", e essa linha tem como evidência "proposto, não medido"
e como ressalva "sem avaliação no corpus". O rótulo "proposto" também não está na legenda M/C/A (l. 515-516). A Seção IV não
mostra por que o híbrido seria melhor que o próprio SAIL\_L, que já trata /25 ou mais com arrays de próximo salto.
O que mudar: tirar a linha da tabela e manter o híbrido no texto da Seção V como hipótese, ou criar na legenda uma categoria
explícita para "sem evidência".

**A5. Média. Tabela VI, linha 528: rótulo de evidência inconsistente com a legenda.**
Problema: a legenda (l. 516) define **A** como "análise, modelo ou simulação sem tráfego", e o FPGA do SAIL é simulado e mede
só os estágios on-chip (Tabela II, l. 236). Pela legenda, é A, não M.
O que mudar: aplicar a legenda de forma uniforme em todas as linhas.

**A6. Média. Tabela VI, linha 530: DXR por "menor pegada de memória".**
Problema: a IV-B não argumenta que o DXR tenha a menor pegada; a Tabela IV põe 782 KB (DXR, LINX com 417 mil prefixos) ao
lado de 2,40 MiB (Poptrie18, REAL-Tier1-A com 531 mil), duas tabelas diferentes medidas por grupos diferentes. A IV-B ainda
diz que DXR e Poptrie "cabem com folga" na L3 (l. 380), o que tira o peso do critério "menor pegada". A comparação na mesma
tabela existe no corpus (asai15, Tab. 3: D16R 1,16 MiB contra Poptrie0 1,49 MiB e Poptrie18 2,40 MiB na REAL-Tier1-A) e não
foi usada.
O que mudar: apoiar a linha na comparação feita na mesma tabela e dizer em que cenário a pegada menor pesa mais que a
velocidade (por exemplo, quando a L3 é dividida com outras tarefas, ponto que a l. 215-216 levanta).

**A7. Média. Tabela VI, linha 531: Tree Bitmap para "chaves largas" e "pior caso determinístico".**
Problema: a única evidência é o cenário que o próprio Tree Bitmap declara (l. 450-451); o artigo testa tabelas de 19 a 41 mil
prefixos e nenhuma chave de 52 bits. O "pior caso determinístico" vem da Tabela 5 do eath04, que a Seção VI (l. 580-581) diz
estar 9 bits acima da fórmula do próprio texto. Ou seja, o veredito se apoia numa tabela que o artigo considera inconsistente.
O que mudar: dizer de onde vem a recomendação (autodeclaração e projeto, sem medição) e reconciliar com a crítica da l. 580.

**A8. Média. Linhas 538-539: "a escolha depende mais da composição do tráfego e do tamanho da cache que do tamanho da tabela".**
Problema: nenhum experimento do corpus isola os três fatores, e a IV-E mostra o tamanho da tabela derrubando o SAIL e exigindo
modificação no DXR (l. 483-492). O próprio Poptrie cai de 240,52 para 174-188 Mlps nas tabelas sintéticas maiores (asai15,
Tab. 5).
O que mudar: tirar a comparação de importância ("mais [...] que") ou apoiar a afirmação em dados.

**A9. Média. Título e Conclusão, linha 591: a pergunta "TCAM ou algoritmo?" não é respondida no mesmo cenário.**
Problema: a Tabela VI nunca põe TCAM e solução algorítmica no mesmo cenário. A TCAM só aparece numa linha à parte (tabelas
pequenas) e num híbrido não medido. A IV-A termina sem veredito de velocidade entre TCAM e algoritmo, e a IV-D diz que a
energia não pode ser comparada. O leitor fica sem saber, por exemplo, o que o corpus diz sobre hardware de backbone com TCAM
contra SAIL.
O que mudar: ou dizer explicitamente, na Seção V e na Conclusão, que o corpus não permite responder à pergunta do título em
nenhum cenário compartilhado (e por quê), ou acrescentar o cenário em que as duas famílias se enfrentam, com o nível de
evidência.

---

## B. Afirmações sem suporte

**B1. Alta. Linhas 125-129 (II-B) e 137-141 (II-C): quem leu e quem inferiu.**
Trechos: "Cada artigo foi lido inteiro e fichado pelo mesmo roteiro" (l. 125); "Separamos o que o artigo afirma do que é dedução
nossa [...] (``pela nossa leitura'', ``conta nossa'')" (l. 127-128).
Problema: a II-C diz que os fichamentos foram feitos por agentes de IA ("um leitor que faz o fichamento de um artigo (rodamos
sete em paralelo)", l. 138) e que a IA escreveu o primeiro rascunho. Lida junto, a voz passiva da II-B fica parecendo
ocultação, e as "deduções nossas" do texto são, em boa parte, as "[inferência]" dos fichamentos da IA. Pelo enunciado (seção 4),
ocultar o uso de IA e entregar texto gerado por IA "sem revisão crítica profunda" dá nota zero. A marca da l. 146 cobre o que
o grupo mudou no rascunho, mas não cobre quem leu os artigos nem quem validou cada inferência.
O que mudar: na II-B, dizer quem fez cada etapa (IA ou integrante) e como cada "nossa leitura" e "conta nossa" foi conferida
por uma pessoa. **Falta uma marca `\revisar`** aqui (ver seção G).

**B2. Média. Linha 140: a skill *humanizer*.**
Problema: o nome, lido por um professor que avalia o uso de IA, sugere uma ferramenta para disfarçar texto de IA. A declaração
é honesta, mas, do jeito que está, pode ser lida como admissão de evasão.
O que mudar: descrever o que a ferramenta faz (revisão de estilo segundo as regras do grupo, sem mudar números nem citações)
e dizer que a revisão de conteúdo foi humana, se de fato foi.

**B3. Média. Linhas 204-206: "Em relação à TCAM, o custo sai da energia e vai para a hierarquia de memória".**
Problema: a frase, sem citação, pressupõe que as soluções algorítmicas gastam menos energia que a TCAM. A IV-D (l. 468-469)
diz que ninguém mede a energia delas. A Seção III afirma o que a IV declara desconhecido.
O que mudar: tirar a afirmação sobre energia ou marcá-la como premissa dos artigos algorítmicos, não da revisão.

**B4. Média. Faltam localizadores (regra do `CLAUDE.md`).**
- l. 67: "rápida, simples de gerenciar e de custo competitivo~\cite{zane03}". Está no Resumo do zane03; "competitive" também
  aparece no §II. Além disso, "Os da primeira" generaliza para a família um texto de um artigo só (o Shah e Gupta não diz isso).
- l. 230 (Tabela II): "DXR D16R & 490 Mlps [...] \cite{zec12}" sem localizador. O valor está no Resumo e na Tab. 2 do zec12
  (491 com 8 núcleos).
- l. 443: "``cost-effective''~\cite{zane03}" sem localizador (Resumo).
- l. 115 (Tabela I, linha do zane03): "só variantes próprias" e "não usa (métrica não depende de tráfego)" sem localizador. A
  segunda é inferência: a garantia de pior caso não depende do tráfego, mas a potência média da seleção de bits depende de
  qual bucket recebe os pacotes.
O que mudar: pôr o localizador e, quando for inferência, marcar.

**B5. Média. Linhas 414-415 e Tabela VI (l. 528): bloqueio do lookup atribuído ao SAIL\_L.**
Problema: o trecho citado (yang18 §III-C) está na subseção "FIB Update for SAIL Basic" e fala das estruturas dos níveis 0 a 24
do SAIL\_B. Estender a afirmação ao SAIL\_L é plausível, mas é inferência.
O que mudar: marcar como inferência ou achar o trecho que trate do SAIL\_L. **Falta `\revisar`.**

**B6. Média-alta. Linhas 434-435: "O único limite pequeno garantido pela própria estrutura é o do SAIL\_U".**
Problema: a Seção III-B (l. 182-183) diz que o PLO\_OPT "move no máximo $L/2$ entradas por operação", isto é, 16 no IPv4, um
limite pequeno garantido pela estrutura. O SAIL\_B também tem um acesso on-chip por atualização (yang18, Tab. II). O texto se
contradiz.
O que mudar: corrigir a frase de modo que inclua o PLO\_OPT (e explicar por que o CAO\_OPT, com limite dependente de $D$, foi o
preferido) ou restringi-la às soluções algorítmicas.

**B7. Média. Linha 412: "de duas a três ordens de grandeza abaixo dos 10 ms".**
Problema: 10 ms / 11,9 µs ≈ 840 (10^2,9) e 10 ms / 2,51 µs ≈ 3984 (10^3,6). A faixa certa vai de cerca de três a quase quatro
ordens. E "todas as soluções algorítmicas medidas" inclui o SAIL\_L, que não mede tempo, só acessos (Tabela V).
O que mudar: corrigir a faixa e restringir a frase a DXR e Poptrie. **Falta `\revisar`.**

**B8. Média. Linha 501: "O Poptrie é o único com teste numa tabela IPv6 real".**
Problema: o SAIL mede a memória on-chip numa FIB IPv6 real de cerca de 14 mil entradas ("about 2.2MB", yang18 §VII-A). O que
só o Poptrie tem é teste de *velocidade* em IPv6 real.
O que mudar: qualificar a frase. **Falta `\revisar`.**

**B9. Baixa-média. Linha 382: "o custo por bit favorece a DRAM e pesa contra a TCAM".**
Problema: a razão de 36 vezes (eath04 §2.3.2) compara SRAM e DRAM, não TCAM e DRAM. Estender o resultado à TCAM é inferência; o
número de TCAM do mesmo artigo é outro (US\$ 4000 por 20 componentes, §2.3.3).
O que mudar: apoiar a frase no §2.3.3 ou marcá-la como inferência.

**B10. Baixa. Linha 385: "O requisito mais citado é de Labovitz".**
Problema: "mais citado" não tem apoio (dois artigos do corpus o citam: ruiz01 p. 11 e shah01 ref. 15). Labovitz é nomeado sem
entrada no `.bib` e sem a marca `[NÃO VERIFICADO]` que o `CLAUDE.md` exige. Na l. 387, "outro trabalho do mesmo grupo" é
ambíguo: o leitor entende que é do grupo de Shah e Gupta, quando a ref. 15 do shah01 é de Labovitz, Malan e Jahanian.
O que mudar: tirar o "mais citado", seguir a regra da marca e desfazer a ambiguidade.

**B11. Baixa. Tabela V, linha 406: "Fora da conta: ---" no Poptrie.**
Problema: o asai15 §4.9 não deixa explícito se os 58,90 ms incluem a atualização da radix (o fichamento registra isso como
"leitura mais natural", não como afirmação do artigo). O travessão afirma que nada ficou de fora.
O que mudar: marcar como incerto. **Falta `\revisar`.**

**B12. Baixa. Linhas 576-581: erros atribuídos a artigos publicados.**
Problema: afirmar que um artigo publicado tem erro é a afirmação mais exposta do texto. As inconsistências do SAIL estão
conferidas no fichamento; a dos "9 bits" da Tabela 5 do Tree Bitmap é a mais difícil de checar, porque depende de uma fórmula
do §7.2 e de uma tabela de 12 valores.
O que mudar: um integrante deve refazer a conta dos 9 bits antes da entrega. **Falta `\revisar`.**

**B13. Baixa. Linha 572: "tem um representante por família".**
Problema: a família TCAM tem dois artigos (shah01 e zane03).
O que mudar: corrigir.

---

## C. Argumentos que não fecham

**C1. Alta. Linhas 317-319: SAIL medido por ele mesmo contra SAIL medido pelo Poptrie.**
Trecho: "O SAIL mede a si mesmo a 231,47--236,08~Mpps [...] e o Poptrie mede o SAIL a 158,22~Mlps. Essa diferença é compatível
com a queixa do SAIL sobre a reimplementação."
Problema: é a comparação direta que a tese (1) proíbe. Muda a CPU (i7-3520M a 2,9 GHz contra i7-4770K a 3,9 GHz), a tabela
(FIB2013 do RIPE contra REAL-Tier1-A), o gerador de tráfego e a unidade declarada. O artigo menciona só a L3. Pior: o próprio
texto, seis linhas abaixo (l. 323-325), mostra que o Poptrie inclui 1,22 ns do gerador em cada lookup e não aplica essa correção
aqui. Descontado o gerador, 158,22 Mlps viram cerca de 196 Mlps, e a diferença cai de cerca de 1,47× para cerca de 1,19×
(conta deste revisor). A "compatibilidade com a queixa" fica bem mais fraca.
Na l. 213-214, o texto ainda trata Mlps e Mpps como unidades diferentes ("A unidade varia entre lookups por segundo num laço de
CPU (Mlps), pacotes por segundo (Mpps)"), quando na CPU o Mpps do SAIL é taxa de lookups num laço. Ou são a mesma grandeza com
nomes diferentes (e então não entram na lista de diferenças de unidade), ou não são (e então não podem ser comparadas na l. 317).
O que mudar: listar todas as diferenças de condição, aplicar a correção do gerador que o próprio texto propõe e decidir se Mpps
e Mlps são a mesma grandeza.

**C2. Alta. Linhas 327-330 e 42: veredito do tráfego aleatório e explicação pelo tamanho da cache.**
Trechos: "Com tráfego aleatório, ou com muitos pacotes em prefixos longos [...] o Poptrie lidera" (l. 329-330); no resumo, a
disputa "se explica [...] pelo tamanho da cache" (l. 42); "Com 44,24~MiB de estrutura e 8~MiB de L3, o tráfego aleatório leva
o SAIL ao segundo caso" (l. 313-315).
Problema: com tráfego aleatório, o SAIL mediu o SAIL\_L 1,13 a 1,14 vez mais rápido que o Poptrie (l. 244), e a Fig. 1 mostra
isso. O veredito escolhe um dos lados de uma divergência que o próprio texto atribui a viés de implementação dos dois lados
(l. 317-321). O argumento da cache aponta na direção contrária: o SAIL venceu no aleatório justamente na máquina com *metade*
da L3 (4 MB). Se a cache explicasse a disputa, o SAIL deveria perder com folga maior lá. O texto não trata disso. Os 44,24 MiB
também são da reimplementação do Poptrie; a pegada do SAIL na implementação dos próprios autores não é conhecida (l. 352-353).
O que mudar: com tráfego aleatório, o corpus não define vencedor (o sinal depende de quem mede). O veredito precisa dizer isso,
e o resumo precisa parar de apresentar o tamanho da cache como explicação até que o texto resolva a inversão.

**C3. Alta (lacuna de método no caso central). Tabela III (l. 287-298) e linha 301: falta a agregação de rotas.**
Problema: o Poptrie liga por padrão a agregação de rotas em todos os resultados próprios ("Unless otherwise noted, the
performance results of Poptrie shown in this paper are with the route aggregation option", asai15 §3, p. 59) e não diz se os
concorrentes reimplementados também a receberam. Na Tab. 2 do asai15, o Poptrie18 sem agregação faz 191,95 Mlps e com ela,
240,52 Mlps, um ganho de cerca de 25%. Sem a agregação, a razão Poptrie18/SAIL na REAL-Tier1-A cai de 1,52 para cerca de 1,21
(conta deste revisor, mesma tabela e mesma máquina). Do outro lado, o SAIL não diz com que opções rodou o código do Poptrie.
A frase "Quatro fatores explicam a divergência sem que nenhum dos lados tenha errado as contas" (l. 301) deixa de fora talvez o
maior fator quantificável e afirma mais do que mostra: "explicam" sem medir quanto cada fator pesa.
O que mudar: acrescentar a agregação como fator na Tabela III e no texto; trocar "explicam" por uma formulação que não afirme
explicação completa.

**C4. Média-alta. Linhas 432-433: "DXR e Poptrie vencem em software, e o CAO\_OPT deixa a TCAM competitiva em número de movimentos".**
Problema: a Tabela V foi montada para mostrar que as unidades não se comparam (µs por prefixo, µs por update, movimentos,
acessos, cópias de nó), e a frase seguinte declara vencedor e "competitivo" entre elas. "Vencem" contra quem? O SAIL só
informa acessos. Além disso, o DXR mede sem a radix (l. 418-419) e o Poptrie provavelmente com ela (B11), cada um com uma carga
de teste diferente (Tabela V, última coluna).
O que mudar: limitar o veredito ao que é comparável (cada solução contra o orçamento de 10 ms ou de 1 ms) e não declarar
vencedor entre unidades diferentes.

**C5. Média. Linhas 70-71: "o SAIL se declara de 1,13 a 1,72 vezes mais rápido".**
Problema: a faixa junta tráfego aleatório (1,13-1,14) e real (1,59-1,72) e é posta ao lado de uma faixa do Poptrie que é só de
tráfego aleatório (1,37-2,62). Para quem ainda não chegou à IV-A, parece que os dois mediram a mesma coisa. Comparadas
condição a condição (aleatório contra aleatório), as faixas se contradizem de fato, o que reforça o argumento.
O que mudar: separar as condições já na introdução.

**C6. Média. Fig. 1 (l. 250-280): razões de plataformas e tabelas diferentes no mesmo eixo.**
Problema: a figura põe lado a lado razões medidas em CPUs diferentes, em tabelas diferentes (35 RIBs, REAL-RENET, REAL-Tier1-B,
FIB2013, 12 FIBs do RIPE, 12 FIBs do tier-1) e com implementações diferentes. A legenda diz "segundo quem mediu", mas não
avisa que os pontos não estão na mesma base, justamente o que a tese (1) diz. A condição "SAIL: por prefixo" aparece na figura
e não é discutida no texto. Ela é relevante: no tráfego por prefixo, a fração que chega a /25 ou mais acompanha a fração de
prefixos longos da FIB (cerca de 2,3%, yang18 §VI-C), muito acima da do aleatório, e mesmo assim o SAIL vence por 1,23 a 1,32.
Isso pesa contra a explicação pela fração acima de /24 e precisa ser enfrentado.
O que mudar: dizer na legenda que as bases diferem e discutir a condição por prefixo no texto.

**C7. Média. Linhas 303-308: a fração acima de /24 depende da tabela, não só do tráfego.**
Problema: o texto compara 1,66% ("se os destinos fossem uniformes", REAL-RENET, asai15 §4.7) com 0,021-0,025% (tráfego
aleatório, FIB2013, yang18 Fig. 11). As duas medidas são de tráfego uniforme, mas sobre tabelas diferentes. A diferença de
cerca de 70 vezes vem da tabela (a REAL-RENET tem rotas de IGP mais específicas, asai15 §4.7), não do tráfego. A tese de que a
disputa depende da "fração do tráfego que casa prefixos maiores que /24" precisa separar a composição da FIB da composição do
tráfego.
O que mudar: dizer que os dois números vêm de tabelas diferentes e tratar a composição da tabela como fator próprio.

**C8. Média. Linhas 305-306 e 327-329: premissas não declaradas sobre os traces.**
- "Os dois traces reais estão, portanto, em lados opostos da premissa" (l. 305-306): a frase seguinte admite que a fração do
  trace do tier-1 não é conhecida, então o "portanto" não decorre. O texto supõe que roteador tier-1 implica tráfego de
  backbone abaixo de /24 (o yang18 diz "a tier-1 router in China", §VI-A, sem quantificar).
- "o SAIL\_L lidera nas duas medições que se aproximam dessa condição: o tráfego sequencial no Poptrie" (l. 328-329): o
  tráfego sequencial percorre os 2^32 endereços em ordem e tem a mesma distribuição de comprimentos que o uniforme (os mesmos
  cerca de 1,66% acima de /24). Ele se aproxima de "boa localidade", não de "tráfego concentrado até /24". O texto mistura as
  duas condições.
- "o tráfego com localidade, como o do trace do tier-1" (l. 314-315): o yang18 §VI-C afirma que "real traffic has the best IP
  locality"; falta citar.
O que mudar: declarar cada premissa e separar localidade de distribuição por comprimento de prefixo.

**C9. Média. Conclusão, linhas 594-595, e IV-D, linha 470: o fator de 8 vezes.**
Problema: o 7,98 vale para o *postorder-split* numa tabela sintética de 1 milhão de entradas (l. 458-460). A Conclusão o associa
a "tabelas de tamanho moderado". A garantia da seleção de bits no mesmo artigo é de 2,62 vezes (zane03, seção da seleção de bits, localizador a conferir; "guarantees a
power reduction of a factor by 1/.381 = 2.62"), e o texto não a menciona.
O que mudar: dizer na Conclusão a variante e o tamanho de tabela a que o fator se aplica, e informar a garantia da outra
variante.

**C10. Baixa-média. Linhas 335-337: "pior caso" do DXR.**
Problema: o texto opõe o "pior caso" do DXR a um padrão "favorável", sem dizer que o DXR define pior caso pela localidade
temporal ("flows are spread across the entire IPv4 address space with minimum or no temporal locality", zec12 §4.1), e não pela
profundidade da busca. Fica parecendo contradição do DXR, quando os dois sentidos convivem.
O que mudar: explicitar os dois sentidos de "pior caso".

**C11. Baixa-média. Linhas 380-381 contra 215-216: "cabem com folga [...] o que atende roteadores em software".**
Problema: a IV-A lembra que nenhum número de CPU inclui o processamento real de pacotes e que outras etapas disputariam a cache.
A IV-B conclui que caber na L3 basta para roteadores em software.
O que mudar: condicionar a conclusão da IV-B à ressalva da IV-A.

**C12. Baixa. Linha 493: "O próprio Poptrie limita a FIB a $2^{16}$ entradas".**
Problema: num parágrafo sobre número de prefixos, o leitor entende que o Poptrie aceita no máximo 65.536 prefixos, o que
contradiz o teste com 886 mil. No Poptrie, a "FIB" é a tabela de próximos saltos indexada pela folha (asai15 §3 e §5).
O que mudar: dizer que o limite é de entradas de próximo salto.

**C13. Baixa. Linhas 547-550: "Os híbridos aparecem em três artigos".**
Problema: a mesma frase conclui que os "nós CAM" do Tree Bitmap não são TCAM; então são dois artigos, não três.
O que mudar: acertar a contagem.

**C14. Baixa. Linha 499: o limite de /64 do SAIL.**
Problema: o texto registra a crítica do Poptrie, mas não a premissa do SAIL ("An IPv6 prefix has 64 bits", yang18 §VII-A). O
Tree Bitmap tem premissa parecida ("Typically <64 bits in practice", eath04 Tab. 3). A divergência é de premissa e precisa ser
dita como tal. A versão de 2018 também não resolve o ponto (os filtros de Bloom vão até o nível 64).
O que mudar: declarar a premissa e dizer que a versão de 2018 a mantém.

---

## D. Lacunas que o professor cobraria

**D1. Alta. Crescimento da FIB.**
Problema: a introdução dá dois pontos soltos (mais de 500 mil em 2014; mais de 700 mil "segundo o RIPE", l. 59-60), e a IV-E
fecha com "tabelas reais maiores que 532 mil" (l. 507) sem dizer o tamanho atual da tabela. Esse limite só tem sentido diante do
tamanho de hoje. O corpus tem material que não foi usado: a série rrc00 de 2002 a 2013 na Tab. IV do yang18 (114.069 a 495.401,
segundo o fichamento); "around 660K in 2017" e crescimento de "around 15% every year" (yang18 §VII-C), que contradiz os
"700,000" do §I-A do mesmo artigo; as projeções de 2003 e 2004 para "1 million entries" (zane03 §II) e "a million or more
prefixes" (eath04 §2.2). Comparar projeção com realizado é uma análise crítica que só este corpus permite.
O que mudar: acrescentar um parágrafo sobre crescimento com esses dados; para o tamanho atual, só com fonte cujo PDF esteja em
`ep2_export/` (regra do `CLAUDE.md`).

**D2. Alta. Corpus até 2018, sem justificativa.**
Problema: a revisão é de 2026, e o artigo mais recente é de 2018. A Seção VI (l. 572-573) só registra o fato. Os critérios de
inclusão da II-A (l. 92-94) não têm corte por data, então o professor vai perguntar por que nada depois de 2018 entrou. O grupo
decidiu manter os 7 (log de 16/11), o que é legítimo, mas a decisão precisa de justificativa no texto.
O que mudar: justificar o corte na II-A (por exemplo, a relação com a disputa Poptrie × SAIL) ou acrescentar trabalhos
recentes com PDF. Direções de busca, sem afirmar que existam artigos específicos: lookup LPM em switches programáveis (onde a
TCAM continua presente), índices aprendidos para lookup IP e lookup IPv6 em escala.

**D3. Média. IPv6 na TCAM.**
Problema: a IV-E trata IPv6 na TCAM só pelo número de movimentos do PLO\_OPT (l. 505). O efeito principal é outro: a largura da
entrada. O zane03 §II diz que 18 Mbit guardam 512 mil prefixos de 32 bits e que IPv6 e classificação exigem mais dispositivos.
Entradas mais largas reduzem a capacidade e aumentam a potência por busca.
O que mudar: tratar capacidade e potência da TCAM para IPv6 com o que o zane03 §II oferece, marcando como "conta nossa" o que
for derivado.

**D4. Média. Taxa de linha como critério.**
Problema: a introdução fixa 148,8 Mlps para 100 GbE (l. 57-58), e a IV-A nunca usa esse número para julgar os resultados. Esse
seria um veredito condicionado barato para a IV-A: quais soluções passam do limiar em um núcleo, segundo quem mediu e em que
plataforma.
O que mudar: usar o limiar da introdução na IV-A.

**D5. Média. Multinúcleo.**
Problema: o texto compara tudo em um núcleo, mas o corpus traz escalabilidade (DXR com 8 núcleos, zec12 Tab. 2; Poptrie com 914
Mlps em 4 núcleos, asai15 §1 e Fig. 8, p. 65). O yang18 §IV-E diz que o SAIL\_L "currently does not support multi-core platforms",
na mesma frase em que diz suportar "many-core"; essa contradição precisa ser conferida. Isso pesa no cenário "roteador em
software" da Tabela VI.
O que mudar: incluir a escalabilidade com o número de núcleos no eixo de velocidade e na linha correspondente da Tabela VI.

**D6. Média. Quem implementou: falta o teste de sanidade disponível.**
Problema: o DXR mede o próprio D16R a 75 Mlps em um núcleo (AMD FX-8150; 64 no Xeon W3530; zec12 Tab. 2), e o Poptrie mede
a reimplementação dele a 116,63 Mlps (i7-4770K, asai15 Tab. 3). A Tabela II usa o número de 8 núcleos (490), que não se compara
com os demais, e deixa de fora o de 1 núcleo, que mostra que a reimplementação feita por um concorrente não saiu
necessariamente pior (ou que a geração da CPU pesa muito). Isso entra direto na discussão sobre viés de implementação
(l. 317-321).
O que mudar: usar o número de 1 núcleo na Tabela II e discutir o contraste, com as diferenças de CPU e de tabela.

**D7. Média-baixa. Reprodutibilidade: código disponível.**
Problema: a Seção V pede "a reimplementação publicada" (l. 557), mas o artigo não diz quais dos sete publicam código (o Poptrie
indica um repositório, asai15 p. 63, nota 2; o SAIL diz ter publicado o seu código e o de quatro concorrentes em [4],
yang18 §VI-C e §VIII; para os demais, conferir).
O que mudar: acrescentar à Tabela I uma coluna de disponibilidade de código.

**D8. Baixa. Ligação com o vocabulário da disciplina.**
Problema: a Seção III não usa a terminologia dos slides (por exemplo, repasse baseado em destino e o lugar do lookup na porta de
entrada do roteador). O `CLAUDE.md` diz que os slides servem para alinhar a terminologia.
O que mudar: alinhar dois ou três termos da Seção III com os slides.

---

## E. Trechos descritivos ("A disse X, B disse Y")

**E1. Média. Linhas 496-505: parágrafo do IPv6.**
Problema: é o trecho mais descritivo do artigo: "O DXR declara [...]. Mesmo assim, o Poptrie adaptou [...]. Segundo o Poptrie, o
SAIL [...]; a versão de 2018 propõe [...]. O Poptrie é o único [...]. Do lado da TCAM, o CoolCAMs diz [...] e Shah e Gupta só
definem $L=128$". A única avaliação é "o que não decide a questão". Faltam o contraste de método (endereços sorteados em
2000::/8 contra FIBs sintéticas derivadas das IPv4, com geradores diferentes), as premissas (C14) e um cenário.
O que mudar: organizar o parágrafo por questão (premissa de comprimento, tipo de carga, escala) e não por artigo, e terminar
com veredito condicionado.

**E2. Baixa-média. Linhas 194-202: as quatro estruturas descritas uma após a outra.**
Problema: é normal em Fundamentos, mas há um contraste pronto que o texto não faz: o Tree Bitmap evita *leaf pushing* para
limitar o custo de atualização (l. 196-197), e o SAIL\_L expande prefixos para os níveis 16, 24 e 32 e por isso tem pior caso de
atualização ilimitado (l. 414). Essa ligação anteciparia o eixo de atualização.
O que mudar: ligar as escolhas de projeto aos eixos.

**E3. Baixa. Linhas 547-550 (híbridos) e 474-481 (escala testada).**
Problema: são enumerações por artigo com uma frase de avaliação no fim.
O que mudar: na escala, comparar a escala testada com a escala que cada artigo diz suportar (o texto faz isso só para o Tree
Bitmap, l. 478-479). Nos híbridos, dizer em que cenário cada um faria sentido.

**E4. Baixa. Linhas 385-389: requisito de atualização.**
Problema: lista três fontes ("Ruiz-Sánchez exige [...]; Shah e Gupta citam [...]; o CoolCAMs observa [...]") antes da conta. Está
quase bom, porque a conta do orçamento em rajada (l. 389-390) é a parte crítica.
O que mudar: dizer que as três fontes remetem à mesma base empírica de Labovitz, salvo o CoolCAMs, que traz traces próprios.

---

## F. Estrutura e formato

**F1. Baixa.** 9 páginas, IEEEtran em duas colunas, A4: atende o enunciado (seção 5). Há espaço para as lacunas da seção D.

**F2. Média.** A seção de uso de IA (II-C) existe e é franca, mas depende das marcas pendentes (l. 146 e 586) e do ajuste B1.
O enunciado avalia "como a ferramenta foi utilizada"; hoje a II-C diz o que a IA fez e quase nada sobre o que o grupo fez com o
resultado.

**F3. Baixa.** Referências: inconsistência de acento em Ruiz-Sánchez (texto contra [1]); DOIs não impressos (o enunciado pede
"referências bibliográficas rigorosas"; imprimir o DOI ajuda o professor a conferir). A versão do yang18 em `ep2_export/` é a
"accepted for inclusion in a future issue", com paginação provisória. A l. 131-132 diz que "Os localizadores seguem a paginação
impressa da versão publicada"; para o yang18, dizer que só se usaram seções, figuras e tabelas.

**F4. Baixa.** Aparência das Tabelas II e III (ver "Build e aparência").

**F5. Baixa.** O resumo e a introdução repetem quase as mesmas frases (l. 38-41 e 74-76: "mede com rigor o eixo em que a [sua]
proposta é forte e trata os demais/outros por modelo ou de forma qualitativa"; "Normalizados por cenário, porém, [...] deixam de
se anular"). "Há duas famílias de solução" aparece no resumo (l. 35) e na introdução (l. 62).

---

## G. Marcas `\revisar`

As 9 marcas existentes (l. 91, 97, 146, 332, 377, 428, 463, 465, 586) correspondem a pendências reais e não foram tratadas como
defeito. Faltam marcas nestes pontos:

| linha | o que validar |
|---|---|
| 125-129 | quem leu e fichou cada artigo, e quem conferiu cada "nossa leitura" e "conta nossa" (B1) |
| 230 | localizador do DXR 490 Mlps (Resumo ou Tab. 2) e troca pelo número de 1 núcleo (B4, D6) |
| 406 | se os 2,51 µs do Poptrie incluem a radix (B11) |
| 412 | ordens de grandeza (B7) |
| 414-415 | se o bloqueio do §III-C do yang18 vale para o SAIL\_L (B5) |
| 434-435 | "único limite pequeno" contra o PLO\_OPT (B6) |
| 501 | "único com teste numa tabela IPv6 real" (B8) |
| 580-581 | conta dos "9 bits" da Tabela 5 do Tree Bitmap (B12) |
| 317-319 | comparação entre plataformas, com e sem o desconto do gerador (C1) |

---

## H. Vícios de estilo

**H1. Média. Frases de efeito no fim do parágrafo.** São o traço que mais faz o texto soar como IA:
- l. 71: "Lidos lado a lado, os números parecem se anular." (montagem retórica: "parecem se anular" na l. 71, "deixam de se
  anular" nas l. 41 e 75).
- l. 301: "sem que nenhum dos lados tenha errado as contas".
- l. 343-344: "Nenhum artigo algorítmico mede uma TCAM real."
- l. 471-472: "o que resolve a questão sem depender de números."
- l. 508-509: "inclusive no SAIL, que se apresenta como independente do tamanho da FIB." (ironia)
- l. 541-542: "divergem porque tratam de pontos diferentes desse espaço."
- l. 465-466: "o número publicado não é reprodutível" ("reprodutível" se aplica a experimento; aqui o problema é uma conta que
  não fecha).
O que mudar: terminar os parágrafos no último fato ou na última condição, sem a frase-resumo.

**H2. Baixa. Tiques de vocabulário.** "próprio/própria/próprios/próprias" aparece 19 vezes ("o próprio SAIL", "o próprio
artigo", "o próprio Poptrie"); "porém" intercalado entre vírgulas, 7 vezes, quase sempre na mesma posição (l. 40, 69, 75, 320,
331, 354, 449). Lido em sequência, o padrão fica evidente.
O que mudar: variar ou cortar a maioria.

**H3. Baixa. Opinião sem marca.** l. 341-342: "comparação que não faz justiça a um esquema pensado também para hardware".
O que mudar: marcar como avaliação do grupo e apoiar no título e no §7 do eath04.

**H4. Baixa. Tríade e roteiro genéricos.** l. 78-83 (contribuições em cinco itens mais o roteiro das seções) e l. 469-472 (três
"afirmações mais modestas" em sequência). Não são graves, mas são o formato padrão de texto gerado.

Não encontrei a construção "não é X, é Y" nem excesso de travessões (o único "---" é uma célula vazia da Tabela V).

---

## Os 5 problemas mais graves

1. A Tabela VI e a Conclusão contradizem a Seção IV: IPv6 na linha do Poptrie e na Conclusão (l. 529, 592) contra l. 496, 507 e 544; SAIL para "FIB crescendo" (l. 528) contra a falha de compilação da IV-E; TCAM por "determinismo e gerência simples" (l. 532, 594) sem apoio e contra l. 186 e 354; um híbrido sem evidência numa tabela de "mais bem sustentada"; FPGA simulado rotulado M contra a própria legenda.
2. O veredito de velocidade com tráfego aleatório (l. 329-330) e a explicação "pelo tamanho da cache" (l. 42, 313-315) não fecham: o SAIL vence no aleatório na máquina com metade da L3, e a agregação de rotas (asai15 §3 e Tab. 2: 191,95 contra 240,52 Mlps, o que leva a razão sobre o SAIL de 1,52 para cerca de 1,21) falta entre os fatores da Tabela III.
3. O corpo viola a tese (1) com comparações diretas entre plataformas: 231 Mpps no i7-3520M/FIB2013 contra 158 Mlps no i7-4770K/REAL-Tier1-A sem descontar o gerador que a l. 323 descreve (l. 317-319); vencedores declarados entre µs, movimentos e acessos (l. 432-433); "menor pegada" do DXR com tabelas diferentes (Tab. IV e VI).
4. A tese está mal formulada: a causa da não comparabilidade ("cada artigo mede com rigor o eixo em que é forte", l. 38-40 e 74-75) é desmentida pelo próprio texto para CoolCAMs, Tree Bitmap e Shah e Gupta; "normalizar por cenário" nunca é definido; e "vence" (resumo, l. 76, título da Seção V) não é o critério "mais bem sustentada" da Tabela VI.
5. Transparência do uso de IA: a II-B diz "Cada artigo foi lido inteiro e fichado" e chama de "dedução nossa" inferências que vieram dos fichamentos feitos pela IA (II-C, l. 138); falta `\revisar` sobre quem leu e validou cada inferência, e a menção à skill *humanizer* (l. 140) pode ser lida como evasão. Esse é o risco de nota zero do enunciado.
