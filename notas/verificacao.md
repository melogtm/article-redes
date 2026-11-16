# Verificação de citações: artigo/artigo.tex × PDFs do corpus

Rascunho verificado: `artigo/artigo.tex` de 16/11/2026 (606 linhas, 10 `\revisar`). Data da verificação: 16/11/2026.
Método: `pdftotext -layout` + `grep` em cada PDF de `ep2_export/`; tabelas e figuras conferidas na página renderizada
(ruiz01 p.22; zec12 p.36; yang18 pp.7, 9, 10, 11, 12). Os DOIs foram conferidos no Crossref (api.crossref.org).
Páginas: ruiz01 pdf n = p.(n+7); shah01 pdf n = p.(n+35); zane03 pdf n = p.(n+41); eath04 pdf n = p.(n+96);
zec12 pdf n = p.(n+28), com a p.29 sendo a *public review*; asai15 pdf n = p.(n+56). O PDF do yang18 é a versão
*early access* ("Content is final as presented, with the exception of pagination"), com páginas 1–16, e por isso só
os localizadores por § servem.

Status: CONFIRMADO, DIVERGENTE, NÃO ENCONTRADO, INFERÊNCIA SEM MARCA. "c/ nota" indica um item confirmado com uma
ressalva que o grupo deve conhecer, sem que isso mude o status.

## Afirmações do texto

| # | linha do .tex | afirmação (curta) | ref | status | PDF diz | localizador |
|---|---|---|---|---|---|---|
| 1 | 57 | LPM busca em duas dimensões, valor e comprimento | ruiz01 | CONFIRMADO | "searching in two dimensions: value and length" | p.10 |
| 2 | 58 | 100 GbE pede 148,8 Mlps com pacotes mínimos | asai15 | CONFIRMADO | "148.8 million lookups per second ... 100 Gigabit Ethernet (GbE) of minimum-size packets" | §1 |
| 3 | 59 | tabelas BGP completas passavam de 500 mil rotas "em 2014" | asai15 | DIVERGENTE | §1 diz só "the number of BGP full routes is beyond 500K", sem ano. O ano sai das datas dos snapshots da Tab. 1 (16–17/12/2014; jan/2015) | §1; Tab. 1 |
| 4 | 59–60 | SAIL cita mais de 700 mil entradas segundo o RIPE NCC | yang18 | CONFIRMADO | "According to the RIPE Network Coordination Centre, FIB sizes have become more than 700,000 entries [3]" | §I-A |
| 5 | 63 | TCAM compara com todas as entradas em paralelo e devolve a primeira | shah01 | CONFIRMADO | "searches ... with all the prefixes in parallel ... selects the first matching entry" | p.38 |
| 6 | 64–65 | família algorítmica: estrutura de dados, lookup pago em acessos à memória | ruiz01 | CONFIRMADO | taxonomia e técnicas auxiliares; "the number of memory accesses must be minimized". c/ nota: a taxonomia começa no fim da p.12 | pp.12–14 |
| 7 | 65–66 | os algorítmicos começam dizendo que a TCAM gasta energia demais e custa caro | zec12, asai15, yang18 | DIVERGENTE | zec12 §1 diz só "power-hungry TCAMs", sem nada sobre custo. asai15 §1 fala em "power consumption and heat", e o custo ("monetary cost") aparece no §2. yang18 §II sustenta as duas coisas: "huge amount of power", "very expensive" | zec12 §1; asai15 §1–2; yang18 §II |
| 8 | 67 | TCAM descrita como rápida, simples de gerenciar e de custo competitivo | zane03 | DIVERGENTE | conteúdo correto ("fast, cost-effective and simple to manage"; "costs that are competitive"), mas o `\cite` não tem localizador | Abstract; §II |
| 9 | 70, 242 | Poptrie18 de 1,37 a 2,62 vezes mais rápido que o SAIL, aleatório, 35 tabelas | asai15 | CONFIRMADO | "Poptrie18 is 24.5–46.1, 3.52–6.78, 1.37–2.62, and 1.04–1.34 times faster than Radix, Tree BitMap, SAIL, and D18R" | §4.5 |
| 10 | 71 | SAIL de 1,13 a 1,72 vezes mais rápido que o Poptrie | yang18 | CONFIRMADO | aleatório 1.13∼1.14; por prefixo 1.23∼1.32; real 1.59∼1.72 | §VI-C |
| 11 | 95–97 | He et al., IEEE/ACM ToN 2018, lido e descartado | — | NÃO ENCONTRADO | não há PDF em ep2_export. O nome aparece sem a marca `[NÃO VERIFICADO]` exigida no CLAUDE.md; há só um `\revisar` | — |
| 12 | 100–101 | a versão ToN 2018 do SAIL responde às medições do Poptrie | yang18 | CONFIRMADO | "the Poptrie authors didn't use our open-sourced SAIL implementation ... We use their open source codes" | §VI-C |
| 13 | 102 | mínimo de ⌈1,5×3⌉ = 5 artigos | enunciado | CONFIRMADO | "Qartigos = ⌈1,5 × Nparticipantes⌉ ... 3 participantes → Mínimo de 5 artigos" | enunciado, §3 |
| 14 | 113 | ruiz01: Pentium Pro de 200 MHz; MaeEast 1999 com 47.113 prefixos; tráfego uniforme por prefixo; código do FreeBSD, dos autores originais e próprio | ruiz01 | CONFIRMADO | "Pentium-Pro-based computer with a clock speed of 200 MHz"; Fig. 22 "MaeEast router (16 August, 1999) 47113 prefixes"; "every prefix has the same probability"; "extracted from the FreeBSD ... implemented by us ... obtained from the corresponding authors" | p.21; p.22 |
| 15 | 114 (e 402, 426, 476, 532) | shah01: tabelas MAE-EAST e MAE-WEST de 35 a 43 mil prefixos | shah01 | DIVERGENTE | na Tab. 1, a linha "Prefixes" é igual a Inserts + Deletes nas duas colunas: 43344 = 34204 + 9140 e 35217 = 34114 + 1103. O eixo das Figs. 13, 14 e 16 vai até 450×100 updates. A leitura "tamanho da tabela" não se sustenta sem ambiguidade. O `\revisar` da l.428 aponta o problema, mas o número é usado sem ressalva nas linhas 114, 402, 426, 476 e 532 | p.43, Tab. 1 |
| 16 | 114 | shah01: simulação; só traços de update de 3 h; concorrentes implementados pelos autores | shah01 | CONFIRMADO | "In our simulation we used two publicly available routing-table snapshots ... and three-hour BGP-update traces" | pp.39, 43 |
| 17 | 115 | zane03: PC de 800 MHz; 2 tabelas reais de 110 a 122 mil; 1 sintética de ≈1M | zane03 | CONFIRMADO | "run on a 800 MHz PC"; Tab. II: rrc04 109,600 e oregon 121,883; "synthetic table that has approximately 1 million prefixes" | §III-D; Tab. II |
| 18 | 116 | eath04: análise e projeto de hardware; Mae-East e Mae-West de 19 a 41 mil; 1M aleatória; números da literatura | eath04 | CONFIRMADO | Tab. 6: 40,902; 19,229; 1,000,000 "Random Generated"; o §3 traz números de outros trabalhos (87.7 M/s, 5 msec) | §7; Tab. 6; §3 |
| 19 | 117 | zec12: FX-8150 com 8 núcleos; Xeon W3530; 3 tabelas de 412 a 421 mil; tráfego sintético uniforme; radix do FreeBSD | zec12 | CONFIRMADO | LINX 417523, U. Oregon 421059, PAIX 412568; "3.6 GHz AMD FX-8150 8-core"; "2.8 GHz Intel Xeon W3530"; "uniformly distributed" | §4.1; Tab. 1; §4.3 |
| 20 | 117 | DXR: DIR-24-8 implementado pelos autores | zec12 | INFERÊNCIA SEM MARCA | o §4.3 diz só "We compared DXR with a software implementation of DIR-24-8-BASIC" e não informa quem escreveu essa implementação | §4.3 |
| 21 | 118 | asai15: i7-4770K com L3 de 8 MiB; 35 tabelas reais de 509 a 532 mil; 4 sintéticas de 756 a 886 mil; 4 padrões de tráfego; todos os concorrentes reimplementados | asai15 | CONFIRMADO | 32 RouteViews + 3 REAL; mínimo 508,700, máximo 532,637; SYN de 756,406 a 885,645; "We implemented these algorithms ourselves" | §4; Tab. 1; §4.2 |
| 22 | 119 | yang18: FPGA simulado; i7-3520M com 1 núcleo e L3 de 4 MB; GPU; many-core; RIPE de 114 a 495 mil; 12 FIBs de um tier-1; três tipos de tráfego | yang18 | CONFIRMADO | "We simulated ... using Xilinx ISE"; "4MB L3 cache"; "we only use one core"; Tab. IV: 114069 a 495401; "12 FIB instances of the same router" | §V; §VI-A; §VI-C; Tab. IV |
| 23 | 119, 293, 320–321 | o SAIL implementou ele próprio 4 dos 5 concorrentes de CPU (§VI-A) | yang18 | DIVERGENTE | o §VI-A diz só "For DXR, we implemented its fastest version – D18R". Os outros três estão na Conclusão: "four well known IP lookup algorithms (namely LC-trie, Tree Bitmap, Lulea, and DXR) that we implemented in [4]" | §VI-A; §VIII |
| 24 | 130–131 | a extração troca "µs" por "ms" no DXR e na Tab. 3 do survey | zec12, ruiz01 | CONFIRMADO | página renderizada: "11.9, 11.0, and 10.2 µs per prefix"; "Table 3. Percentiles of lookup times (µs)" | zec12 §4.4; ruiz01 Tab. 3 |
| 25 | 144–145 | SAIL cita de outros autores uma estatística de distribuição de prefixos | yang18 | CONFIRMADO | "Gupta et al. [18] and Pierluigi et al. [41] ... 99.93% of the prefixes ... ⩽ 24" | §I-C |
| 26 | 145–146 | "880 mil rotas" não aparece no Poptrie nem no SAIL | asai15, yang18 | CONFIRMADO | o grep encontra só 885,645, 876,944 e "1,880 block RAMs" | — |
| 27 | 153–154 | N prefixos de até W bits; LPM | ruiz01 | CONFIRMADO | "N to denote the number of prefixes ... W to indicate the maximum length" | p.10 |
| 28 | 154–156 | taxonomia por dimensão e modo de busca; técnicas auxiliares (expansão, compressão, hierarquia de memória) | ruiz01 | CONFIRMADO | "differ in the dimension to search and whether this search is linear or binary"; "Auxiliary Techniques". c/ nota: a taxonomia começa na p.12 | pp.12–14 |
| 29 | 157–158 | critérios: lookup, atualização, memória, escalabilidade com número e comprimento | ruiz01 | CONFIRMADO | "Scalability ... with respect to both the number and length of prefixes" | p.20 |
| 30 | 158–159 | o survey não trata de TCAM; hardware dedicado = arquitetura de dois bancos de memória | ruiz01 | CONFIRMADO | o grep por CAM, TCAM e "associative" não encontra nada; "Multibit Tries in Hardware", com "First memory bank" e "Second memory bank" | p.16 |
| 31 | 162 | comparação por complexidade assintótica | ruiz01 | CONFIRMADO | "Table 2. Complexity comparison" | p.20 |
| 32 | 163–164 | Pentium Pro de 200 MHz, uma tabela de 47.113 prefixos, tráfego uniforme [Tab. 3, p.22] | ruiz01 | DIVERGENTE | o Pentium Pro está na p.21. O número 47113 e o tráfego uniforme estão nas pp.21–22. A Tabela I do próprio texto já dá p.21 | pp.21–22 |
| 33 | 164–165 | compromisso entre tempo de lookup e tempo de atualização | ruiz01 | CONFIRMADO | "a trade-off between lookup time and incremental update time needs to be made" | p.22 |
| 34 | 165–166 | Lulea sem atualização incremental: "rebuilding the whole structure is the only solution" | ruiz01 | CONFIRMADO | "compression and the leaf pushing technique used do not allow incremental updates. Rebuilding the whole structure is the only solution." | p.18 |
| 35 | 166–168 | "but this is rarely the case for backbone routers" | ruiz01 | CONFIRMADO | sobre otimização, que compensa se a tabela "change very little, but this is rarely the case for backbone routers" | p.17 |
| 36 | 168–170, 347–349 | DXR e Poptrie mantêm uma radix ao lado e reconstroem só a parte afetada | zec12, asai15 | CONFIRMADO | "radix tree ... for rebuilding"; "each chunk is processed independently"; "replacing only the updated part of the trie" | zec12 §3.4; asai15 §3.5 |
| 37 | 173–175 | entrada ternária; busca em paralelo; codificador de prioridade escolhe o menor endereço | shah01 | CONFIRMADO | "priority encoder ... the matching prefix at the lowest physical memory address". c/ nota: os três estados (0, 1, X) estão na p.37 | p.38, Fig. 1 |
| 38 | 175–177 | inserir pode exigir O(N) deslocamentos na solução ingênua | shah01 | CONFIRMADO | "naive addition of a new entry can result in the need to move O(N) TCAM entries" | p.37 |
| 39 | 177–178 | TCAM de alta densidade gasta de 12 a 15 W com todas as entradas habilitadas | zane03 | CONFIRMADO | "consume as much as 12–15 Watts each when all the entries are enabled for search" | §I |
| 40 | 178–179 | potência modelada como proporcional ao número de entradas pesquisadas | zane03 | CONFIRMADO | "linearly proportional to the number of searched entries, we use this number as a measure" | §II |
| 41 | 179 | 18 Mbit guardava até 512 mil prefixos IPv4 | zane03 | CONFIRMADO | "A 18Mbit TCAM can store up to 512K 32 bit prefixes" | §II |
| 42 | 181–182 | PLO_OPT e CAO_OPT mantêm o espaço livre no centro | shah01 | CONFIRMADO | "keep all the unused entries in the center"; "CAO_OPT algorithm also keeps the free space pool in the center" | pp.40–41 |
| 43 | 182–183 | PLO_OPT move no máximo L/2 entradas; L = 32 no IPv4 | shah01 | CONFIRMADO | "swap at most L/2 memory entries"; "L equals 32 in IPv4" | pp.37, 40 |
| 44 | 183–185 | CAO_OPT: só prefixos da mesma cadeia precisam de ordem; no máximo D/2 de uma entrada livre; D é a maior cadeia | shah01 | CONFIRMADO | "only prefixes that lie on the same chain ... need to be ordered"; "at most D/2 prefixes between p and a free space entry" | pp.40, 42 |
| 45 | 185–186 | software de gerência com trie auxiliar fora do chip, que envia instruções à TCAM [p.38] | shah01 | DIVERGENTE | a p.38 traz o "memory manager software that arranges prefixes ... and sends appropriate instructions". A trie está na p.40 ("uses a trie data structure") e na p.43 ("auxiliary trie data structure"). O texto não diz "fora do chip" | pp.38, 40, 43 |
| 46 | 186–189 | buckets; k bits fixos entre os 16 primeiros; prefixos <16 ou >24 bits, menos de 2%, sempre pesquisados | zane03 | CONFIRMADO | "less than 2% in our datasets"; "These blocks are searched for every lookup"; "choosing the hashing bits from the first 16 bits" | §III-A |
| 47 | 189–191 | TCAM de índice pesquisada inteira; subtree-split e postorder-split | zane03 | CONFIRMADO | "requires the entire index TCAM to be searched every time" | §IV, Fig. 5 |
| 48 | 195–197 | Tree Bitmap: dois bitmaps, filhos contíguos, sem leaf pushing, atualização limitada ao tamanho de um nó | eath04 | CONFIRMADO | "two bitmaps per trie node"; "child nodes ... stored contiguously"; "update times are bounded by the size of a trie node" | §4 |
| 49 | 197–198 | DXR: k de 16 a 20; o índice aponta para o próximo salto ou para um bloco com busca binária | zec12 | CONFIRMADO | "k = 16..20 is used"; chunks com uma entrada apontam direto para o próximo salto | §3.2 |
| 50 | 198–200 | Poptrie: 64 vias, popcnt sobre vetor de 64 bits, tabela de topo de s bits | asai15 | CONFIRMADO | k = 6; "population count"; "direct pointing" | §3.1, §3.4 |
| 51 | 200–202 | SAIL separa o comprimento (bitmaps on-chip) do próximo salto (off-chip); trata ≤/24 e ≥/25 à parte; SAIL_L nos níveis 16, 24 e 32 | yang18 | CONFIRMADO | "In our experiments, the two levels are 16 and 24 ... to level 32" | §I-C; §IV-B |
| 52 | 215–216 | DXR admite que o teste sintético isola o lookup e que etapas reais disputariam a cache | zec12 | CONFIRMADO | "several working sets ... would compete for CPU caches ... synthetic benchmarks which isolated only lookup requests" | §4.2 |
| 53 | 216 (e 529) | "pela descrição dos testes, o mesmo vale para o Poptrie e o SAIL" | yang18 | DIVERGENTE | omite o SAIL_L implantado no PEARL, uma plataforma de roteador virtual, com o trace real: "the lookup speed becomes around 28 times faster". O resultado é só relativo, mas é processamento dentro de um roteador | §V-E |
| 54 | 227, 343 | TCAM >100 Mlps, dispositivo de 18 Mbit, dado de fabricante; "over 100 Million lookups/second" | zane03 | CONFIRMADO | "capacity (up to 18Mbits) and search rates of over 100 Million lookups/second [3], [8]", com [3] = IDT e [8] = Netlogic | §II |
| 55 | 228, 339–341 | Tree Bitmap: meta de 25 M/s no pior caso, sem medição; Tab. 5 analítica | eath04 | CONFIRMADO | "targeted to support up to 25 million worst case lookups per second"; a Tab. 5 sai da fórmula 12+6(j−2) | §7.2 |
| 56 | 229, 231–233 | TBM 56,24; D18R 179,92; Poptrie18 240,52; SAIL 158,22 Mlps | asai15 | CONFIRMADO | valores da Tab. 3. c/ nota: são da tabela REAL-Tier1-A, que é a pior para o Poptrie, e a Tabela II do texto não informa a tabela | Tab. 3 |
| 57 | 230 | DXR D16R a 490 Mlps, 8 núcleos, chaves uniformes | zec12 | DIVERGENTE | conteúdo correto, mas o `\cite` não tem localizador. Abstract: "achieves 490 million lookups per second"; a Tab. 2 dá 491 para k=16 e 8 núcleos | Abstract; Tab. 2 |
| 58 | 234–235, 318 | SAIL_L 231,47–236,08 Mpps no aleatório e 673,22–708,71 Mpps no trace, 1 núcleo do i7-3520M | yang18 | CONFIRMADO | valores impressos; "we only use one core" | §VI-C |
| 59 | 236 | SAIL_L a 479 Mpps em FPGA simulado, só os estágios on-chip | yang18 | CONFIRMADO | "measuring the lookup speed on the data structures stored in on-chip memory ... 479Mpps" | §VI-B |
| 60 | 243 | Poptrie18 1,22 vez mais rápido que o SAIL com trace real | asai15 | CONFIRMADO | "Poptrie18 is 3.02, 1.61 and 1.22 times faster than Tree BitMap, D18R and SAIL" | §4.7 |
| 61 | 243–245 | SAIL com o código aberto do Poptrie: 1,13–1,14 no aleatório, 1,59–1,72 no real | yang18 | CONFIRMADO | valores impressos | §VI-C |
| 62 | 245–246 | "probably introduces some unnecessary overhead" | yang18 | CONFIRMADO | citação literal | §VI-C |
| 63 | Fig. 1 (269–272) | razões 1,37–2,62; 1,22; 0,888; 0,976; 0,877–0,885; 0,758–0,813; 0,581–0,629 | asai15, yang18 | CONFIRMADO | conta refeita: 1122/1264 = 0,888; 480/492 = 0,976; 1/1,14 a 1/1,13; 1/1,32 a 1/1,23 (por prefixo: "1.23∼1.32"); 1/1,72 a 1/1,59 | asai15 §4.5, §4.7; yang18 §VI-C |
| 64 | 291 | CPU e cache: i7-4770K com L3 de 8 MiB; i7-3520M com L3 de 4 MB; 1 núcleo nos dois | asai15, yang18 | CONFIRMADO | "Intel(R) Core i7 4770K (3.9 GHz, 8 MiB cache)"; "a 4MB L3 cache"; "we only use one core" | asai15 §4; yang18 §V-B, §VI-C |
| 65 | 292, 321 | rival: Poptrie reimplementou o SAIL sem informar parâmetros; SAIL usou o código do Poptrie sem informar a configuração | asai15, yang18 | CONFIRMADO | nenhum dos dois informa parâmetros (no SAIL, o grep por Poptrie não traz s nem versão) | asai15 §4; yang18 §VI-C |
| 66 | 294, 325 | Poptrie: xorshift com o custo incluído; SAIL não descreve como gera o tráfego aleatório | asai15, yang18 | CONFIRMADO | "we did not exclude this overhead"; o SAIL diz só "randomly chosen destinations". c/ nota: essa descrição está no §VI-A, e o SAIL afirma que "the source code for synthetic traffic is available at [4]" | asai15 §4.2; yang18 §VI-A |
| 67 | 295, 303–305 (e o enquadramento em 42, 555, 600) | trace do Poptrie: "21,8% dos pacotes casam prefixos maiores que /24, contra 1,66%" para destinos uniformes | asai15 | DIVERGENTE | o PDF diz "21.8% of the packets of real-trace have **binary radix depth** more than 24, while only 1.66% of the whole IPv4 address space have binary radix depth more than 24". O próprio artigo define a profundidade como o número de bits verificados, que é maior ou igual ao comprimento do prefixo casado ("search down to the 24th level to decide that the matching prefix is only /8", Fig. 7). Pela métrica de prefixo casado, o SAIL mede 0,021% a 0,025% para destinos aleatórios, e não 1,66% | asai15 §4.7 (p.68); §4.1, Fig. 7; yang18 Fig. 11 |
| 68 | 295 | tier-1 na China; a fração acima de /24 do trace real não é informada | yang18 | CONFIRMADO | "peer relationship with a tier-1 router in China"; o único número de tráfego acima de /24 é o da Fig. 11 | §VI-A |
| 69 | 296, 314, 370 | SAIL: 44,24 MiB no total (medido pelo Poptrie); no máximo 2,13 MB on-chip | asai15, yang18 | CONFIRMADO | Tab. 3 "SAIL 44.24"; "(2^16 + 2^16∗16 + 2^24)/1024/1024/8 ≈ 2.13 MB" | asai15 Tab. 3; yang18 §IV-D |
| 70 | 301–303 | escopo do SAIL é o backbone; na borda, mais tráfego em prefixos longos e lookup mais lento | yang18 | CONFIRMADO | "The scope of this paper is on backbone routers"; "AS border routers ... more traffic hitting prefixes of length > 24. As a result, the lookup speed of SAILs could be slower" | §I-C; §VI-A |
| 71 | 307–308 | único número de tráfego acima de /24: aleatório, de 0,021% a 0,025% | yang18 | CONFIRMADO | "the percentages of 25 traffic traces with more than 24 bits matching prefix length range from 0.021% to 0.025%" | §VI-C, Fig. 11 |
| 72 | 310–311 | SAIL vence no sequencial (1264 contra 1122) e no repetido (492 contra 480) | asai15 | CONFIRMADO | valores impressos. c/ nota: só na REAL-Tier1-B ("For REAL-Tier1-B where Poptrie performed worse"), condição que o texto e a Fig. 1 não informam | §4.5 |
| 73 | 312 | SAIL: mediana de 22 ciclos e p99 de 299; Poptrie18: 46 e 169 | asai15 | CONFIRMADO | Tab. 4, REAL-Tier1-A. Na Tier1-B o p99 é 290 contra 166 | Tab. 4 |
| 74 | 313–315 | "pela nossa leitura": SAIL rápido com o dado na cache, lento na DRAM | asai15 | CONFIRMADO | o próprio artigo diz isso: "performance of SAIL relies on the destination IP address locality"; "tail distribution of SAIL ... L3 cache misses". Pode ser atribuído em vez de marcado como leitura | §2; §4.5; §4.6 |
| 75 | 323–325 | gerador de 1,22 ns; a 240,52 Mlps, 4,16 ns por lookup, cerca de 29% do gerador (conta nossa) | asai15 | CONFIRMADO | "1.22 nanoseconds per generation". Conta refeita: 1/240,52 M = 4,158 ns; 1,22/4,158 = 29,3% | §4.2; Tab. 3 |
| 76 | 330–331 | SAIL testa FIBs com 1% a 10% de prefixos longos e fica 1,47 a 2,83 vezes à frente | yang18 | CONFIRMADO | "SAIL_L is 1.47 ∼ 2.83 times faster than Poptrie"; "all the longer prefixes are generated randomly". c/ nota: a Fig. 14 plota só o SAIL_L (448–467, 357–380 e 271–296 Mpps); os números do Poptrie e a razão estão só no texto | §VI-C; Fig. 14 |
| 77 | 332 (`\revisar`) | qual tráfego a Fig. 14 usa | yang18 | NÃO ENCONTRADO | nem o texto nem a legenda da Fig. 14 informam o tráfego. As FIBs são as 12 da rrc, que no artigo só têm tráfego aleatório ou por prefixo, já que o trace real é do tier-1. Recomendação: escrever que o tráfego não é informado | §VI-C; Fig. 14 (p.12) |
| 78 | 335 | DXR chama o tráfego uniforme aleatório de pior caso | zec12 | CONFIRMADO | "This workload tries to replicate the worst case for a high performance router working in the core" | §4.1 |
| 79 | 336–337 | de 75,7% (D16R) a 94,5% (D20R) das chaves resolvidas no índice | zec12 | CONFIRMADO | coluna n=0: .757 e .945 ("n = 0 means a direct match in the lookup table") | Tab. 3 |
| 80 | 337–338 | Poptrie à frente do D18R por 1,04 a 1,34 vez | asai15 | CONFIRMADO | ver o item 9 | §4.5 |
| 81 | 338–339 | o p95 do DXR e do SAIL passa de 234 ciclos nas profundidades 24 e 25 | asai15 | CONFIRMADO | "those of SAIL and DXR exceed 234 cycles at the binary radix depth of 24 and 25" | §4.6 (p.67) |
| 82 | 339 | "o que no DXR bate com o custo da busca binária em prefixos longos" | asai15 | INFERÊNCIA SEM MARCA | o artigo atribui a diferença do D18R à "binary search stage in DXR", mas mede por profundidade de radix e não por comprimento de prefixo | §4.6 |
| 83 | 341–342 | Tree Bitmap de 3,52 a 6,78 vezes atrás | asai15 | CONFIRMADO | ver o item 9 | §4.5 |
| 84 | 344, 440 | nenhum artigo algorítmico mede uma TCAM real nem o próprio consumo | zec12, asai15, yang18 | CONFIRMADO | nenhum valor em W nos três; o yang18 só dá o tamanho "a few Mbs" | — |
| 85 | 350–351, 369 | radix com 30,48 MiB; Poptrie18 com FIB de 2,40 MiB; RIB em radix | asai15 | CONFIRMADO | Tab. 3 (também na Tab. 2); "routes are preserved in a separate routing table (RIB) such as radix" | Tab. 3; §3 |
| 86 | 352–353 | off-chip do SAIL em IPv4 não informado; pede ≥ 4 GB | yang18 | CONFIRMADO | "the off-chip memory is large enough (⩾ 4 GB)"; a Fig. 21 trata só de IPv6 sintético | §IV-D |
| 87 | 354–355 | trie auxiliar de gerência fora da TCAM [p.38], tamanho não informado | shah01 | DIVERGENTE | mesmo problema do item 45: a trie está nas pp.40 e 43, e "fora" é dedução | pp.40, 43 |
| 88 | 366 | TCAM: 18 Mbit ≈ 512 mil prefixos IPv4 | zane03 | CONFIRMADO | ver o item 41 | §II |
| 89 | 367 | Tree Bitmap: 11–23 B/prefixo na estrutura de busca; 128 B físicos; folhas fora | eath04 | CONFIRMADO | Tab. 6: 11, 13, 23; "do not include a leaf"; "128 Bytes of physical DRAM used per prefix" | Tab. 6; §7.2 |
| 90 | 368 | DXR D16R: 782 KB para 417 mil prefixos [§3.4] | zec12 | DIVERGENTE | o §3.4 (Updating) não traz o número. 782 KB está no Abstract e na Tab. 2 (k=16); a Tab. 1 dá 800672 B para a LINX, com 417523 prefixos | Abstract; Tab. 1; Tab. 2 |
| 91 | 375–377 | 128 B/prefixo e 1,6 GB para 10 M; 128 × 10 M = 1,28 GB | eath04 | CONFIRMADO | os dois números estão impressos e a diferença é real. Para o `\revisar`: o mesmo parágrafo dá 400 MB sem réplica, e 400 × 4 = 1,6 GB, o que equivale a 40 B/prefixo e não aos 32 (16+16) declarados | §7.2 (p.120) |
| 92 | 377–378 | por bit, a SRAM custa até 36 vezes a DRAM de rede com a mesma banda | eath04 | CONFIRMADO | "per bit price ratio between networking sram and networking dram with same total BW ... as high as 36:1". c/ nota: refere-se a SRAM discreta de rede (QDR); a SRAM on-chip sai cerca de 25× (§2.3.1) | §2.3.2 |
| 93 | 385–387 | Labovitz via survey: 100 mudanças/s em média, rajadas de "several hundred", logo 10 ms | ruiz01 | CONFIRMADO | "exceeding several hundred prefix updates per second ... on average, route changes occur 100 times/s ... 10 ms or less" | p.11 |
| 94 | 387–388 | Shah e Gupta citam trabalho do mesmo grupo: 100 a 1000 prefixos/s | shah01 | CONFIRMADO | "approximately 100 to 1,000 prefixes per second.15", com ref. 15 = Labovitz, Malan e Jahanian | p.38 |
| 95 | 388–389 | rajadas de até "a few thousand" adições num único segundo | zane03 | CONFIRMADO | "floods of up to a few thousand route additions in a single second" | §V |
| 96 | 389–390 | menos de 1 ms por atualização numa rajada (conta nossa) | — | CONFIRMADO | 1 s / 2000 = 0,5 ms | — |
| 97 | 402 | CAO_OPT: média de 1,02–1,05; 3 no pior caso observado; D/2 teórico; otimalidade conjecturada | shah01 | CONFIRMADO | Tabs. 2–3: 1.05 e 1.02, máximo 3.0; "we conjecture that the CAO_OPT algorithm is an optimal" (p.43). c/ nota: as Tabs. 2–3 estão na p.46, e o texto da p.44 diz 1.02 a 1.06 | pp.40, 43, 46 |
| 98 | 403 | CoolCAMs: 1 a 1,07 escrita; 0 a 74 recomputações com 8 buckets; pior caso reescreve a TCAM inteira; 3,4 e 3,6 milhões de updates | zane03 | CONFIRMADO | Tab. III: 3,412,540 e 3,614,740; Tab. IV (8 buckets): 0 a 74, e escritas extras de .01 a .07; "rewriting the entire table in the data TCAM". c/ nota: com 64 buckets, chega a 1957 recomputações e 1,56 escrita por update | Tabs. III–IV; §V |
| 99 | 404, 419–422 | Tree Bitmap: 256+C sem derivação, C não definida; arrays iniciais ≥13 bits com "poor update times"; 13 bits na referência de software | eath04 | CONFIRMADO | "256 + C node copy operations in the worst case where C is small"; "Array sizes of 13 bits or higher could, however, have poor update times"; "13,4,4,4,4,3 trie" | §4; §5.1; §6 |
| 100 | 405 | DXR: 10,2–11,9 µs por prefixo; prefixos curtos custam mais; radix fora; LINX removida e reinserida | zec12 | CONFIRMADO | página renderizada; Fig. 7 (eixo em ms, /8 perto de 1–3 ms); "latencies do not include ... the BSD radix tree" | §4.4; Fig. 7 |
| 101 | 406 | Poptrie18: 2,51 µs por update; 23.446 updates em 1 h de um peer; até 1 MiB (conta nossa) | asai15 | CONFIRMADO | "58.90 milliseconds for all 23,446 updates, i.e., only 2.51 microseconds"; "four 15 minute update archive files ... of RV-linx-p52" | §4.9; §3.4–3.5 |
| 102 | 407 | SAIL_L: 1,807–2,253 acessos por update; 7,88 observado; trie do plano de controle; 319×500 updates de 3 coletores | yang18 | CONFIRMADO | "1.854, 2.253 and 1.807"; "observed worst case is 7.88"; "319 ∗ 500 updates". c/ nota: pela Fig. 12, o eixo é em blocos de 500 e só a curva do rrc03 chega a 319; rrc00 e rrc01 terminam antes | §VI-C; Fig. 12; §IV-B |
| 103 | 412 | as médias medidas ficam "de duas a três ordens de grandeza abaixo dos 10 ms" | zec12, asai15 | DIVERGENTE | conta sem marca e imprecisa: 10 ms / 11,9 µs ≈ 840× (≈2,9 ordens) e 10 ms / 2,51 µs ≈ 3980× (≈3,6 ordens), ou seja, cerca de três a quatro ordens. "Todas" cobre só DXR e Poptrie, porque o SAIL mede acessos e o Tree Bitmap não mede | zec12 §4.4; asai15 §4.9 |
| 104 | 414 | SAIL_L com pior caso de atualização ilimitado | yang18 | CONFIRMADO | Tab. II "Unbounded"; "the update speed in the worst case is unbounded" | Tab. II; §IV-E |
| 105 | 414–415 | nenhum lookup enquanto a estrutura on-chip muda, o que pode causar perda de pacotes | yang18 | CONFIRMADO | "no lookup can be performed before changes are finished and therefore may cause packet losses". c/ nota: dito na atualização do SAIL_B, mas os arrays on-chip do SAIL_L são do mesmo tipo | §III-C |
| 106 | 415–417 | Poptrie atualiza sem bloquear, com escritor único e troca atômica; só informa a média | asai15 | CONFIRMADO | "lock-free approach"; "single-threaded update operation, the atomic instruction" | §3.5; §4.9 |
| 107 | 417–418 | array de topo de até 4×2^s bytes substituído; com s=18, 1 MiB (conta nossa) | asai15 | CONFIRMADO | "increases the memory footprint by 4×2^s bytes"; "the entire top-level array of 2^s entries needs to be replaced"; 4 × 2^18 = 1.048.576 B | §3.4–3.5 |
| 108 | 418–419 | DXR deixa fora a atualização da radix | zec12 | CONFIRMADO | ver o item 100 | §4.4 |
| 109 | 424–426 | o D, nas tabelas medidas, não passava de 5 [p.40] | shah01 | DIVERGENTE | a p.40 traz uma afirmação geral: "D is usually small (at most 5) for even large backbone forwarding tables". A medição nas tabelas está na p.44, "all chains have a length less than six", com a Fig. 15 na p.45 | pp.40, 44–45 |
| 110 | 426 | tabelas de 35 a 43 mil, uma ordem de grandeza menores que as do DXR e do Poptrie | shah01 | DIVERGENTE | depende da leitura da Tab. 1; ver o item 15 | Tab. 1 |
| 111 | 427 | traços de 3 h dão cerca de 3 a 4 atualizações por segundo (conta nossa, Tab. 1) | shah01 | CONFIRMADO | (34204+9140)/10800 s = 4,0/s e (34114+1103)/10800 s = 3,3/s. Vale qualquer que seja a leitura de "Prefixes" | p.43, Tab. 1 |
| 112 | 429–430 | o CoolCAMs conta uma escrita por atualização e delega a ordem a Shah e Gupta [§II] | zane03 | DIVERGENTE | a delegação está no §II ("recent work [9] has proposed innovative algorithms", com [9] = Shah e Gupta). A "minimum one data TCAM write" está no §V e na legenda da Tab. IV | §II; §V, Tab. IV |
| 113 | 434–435 | SAIL_U: 1 acesso on-chip por update e 4 por lookup; SAIL_L: 2 por lookup | yang18 | CONFIRMADO | Tab. II: SAIL_U ≤2.03MB, 4, 1; SAIL_L ≤2.13MB, 2, Unbounded | Tab. II |
| 114 | 438–439 | "power-hungry TCAMs"; energia e calor; "a huge amount of power" | zec12, asai15, yang18 | CONFIRMADO | citações literais | zec12 §1; asai15 §1; yang18 §II |
| 115 | 443 | o CoolCAMs chama a TCAM de "cost-effective" | zane03 | DIVERGENTE | a citação está correta, mas o `\cite` não tem localizador | Abstract |
| 116 | 443–444, 458–460 | redução garantida de 7,98× com 8 buckets (postorder-split, tabela de 1M) | zane03 | CONFIRMADO | "106/125,288 = 7.98; this reduced power budget is independent of the distribution" | §IV-D (p.50) |
| 117 | 444–446 | "extremely prohibitive"; 10 M × 52 bits: 20 componentes, >US$ 4000, >200 W | eath04 | CONFIRMADO | "would require 20 TCAM components. The cost could easily exceed $4000 ... power could easily be >200W" | §2.3.3 |
| 118 | 446–447 | o CoolCAMs "do not appear to be reflected in practice" | eath04 | CONFIRMADO | "[27] presents some ideas for reducing power consumption in TCAMs but these ideas do not appear to be reflected in practice", com [27] = CoolCAMs | §3 |
| 119 | 449 | o CoolCAMs trata de tabelas IPv4 de até 1 milhão de entradas | zane03 | CONFIRMADO | "routing engines capable of scaling up to 1 million entries" | §II |
| 120 | 450–451 | roteador multisserviço; chaves de VPN de 52 bits; até 10 M prefixos; cenário não comum | eath04 | CONFIRMADO | Tab. 3: "52 bits", "5M-10M"; "which would seemingly not be the common case". c/ nota: a Tab. 3 está na §2.2 | §2.1; Tab. 3; §7.2 |
| 121 | 452–453 | "if techniques are not employed to limit the components and banks of CAMs that are searched" | eath04 | CONFIRMADO | citação literal | §2.3.3 |
| 122 | 457–458, 460–461 | o CoolCAMs não mede potência: usa 15 W nominais × entradas, num modelo linear sem fonte; 15 W para 1M no pior caso, contra 15 W para 512K no §II | zane03 | CONFIRMADO | "with a 15 watt 1M-entry data TCAM"; §II: "18Mbit TCAM ... up to 15 Watts", "512K 32 bit prefixes". A frase do modelo linear não tem citação | §II; §IV-D |
| 123 | 461–462 | pesquisar 125.288 entradas daria cerca de 3,6 W pelo modelo (conta nossa) | zane03 | CONFIRMADO | 125.288 / 524.288 × 15 W = 3,58 W (3,67 W se 512K = 512.000). O artigo diz "under 2 watts" = 125.288 / 10^6 × 15 | §II; §IV-D |
| 124 | 463–465 | chips de 256K × 72 bits; 10 M pediriam cerca de 39; 20 só com 36 bits (conta nossa) | eath04 | CONFIRMADO | "18Mbit (that is 256k by 72-bit entries...)". 10^7 / 262.144 = 38,1, logo 39 chips; 18 Mbit / 36 b = 524.288 entradas, e 10^7 / 524.288 = 19,1, logo 20 chips | §2.3.3 |
| 125 | 471 | em NFV sobre servidores comuns não há TCAM | asai15 | CONFIRMADO | "virtualized network functions are currently implemented in software without TCAMs" | §1 |
| 126 | 476–478 | o caso de 1 milhão do CoolCAMs aparece só no pior caso e numa tabela sintética | zane03 | CONFIRMADO | ver os itens 17 e 116. c/ nota: o limite de "35" no início da frase depende do item 15 | §III-D; §IV-D |
| 127 | 478–479 | Tree Bitmap avalia 19–41 mil; requisito de "a million or more prefixes" | eath04 | CONFIRMADO | "may require a million or more prefixes" (projeção para 2005+) | Tab. 6; §2.2 |
| 128 | 479–481 | DXR, Poptrie e SAIL usam tabelas reais de 114 a 532 mil; só o Poptrie vai a 886 mil (sintéticas) | todos | CONFIRMADO | zec12 Tab. 1; asai15 Tab. 1; yang18 Tab. IV | — |
| 129 | 483–484 | SAIL guarda o chunk ID em 15 bits, o que bastava nas FIBs reais | yang18 | CONFIRMADO | "based on measurement from our real FIBs of backbone routers, 15 bits are enough" | §IV-B |
| 130 | 484–486 | nas SYN2 (877 e 886 mil), os chunks passam de 2^15 e o SAIL não compila | asai15 | CONFIRMADO | "C16[i] ... encoded in the 15 bits of BCN[i], but it exceeds 2^15"; Tab. 5 "N/A" | §4.8; Tab. 5 |
| 131 | 486–487 | "tiny problem"; 16 bits mais um bitmap de 2^16 bits, sem medir | yang18 | CONFIRMADO | "This is a tiny problem ... use additional 2^16 bits as the flag"; sem experimento | §VI-C |
| 132 | 489–490 | SYN2: prefixos de até /24, /20 e /16 divididos em 2, 4 e 8, com próximos saltos distintos | asai15 | CONFIRMADO | citação quase literal | §4.1 |
| 133 | 491 | DXR: até 2^19 faixas e 4096 entradas por chunk | zec12 | CONFIRMADO | "works for up to 2^19 address ranges ... and up to 4096 entries per chunk" | §3.2 |
| 134 | 492 | o Poptrie estendeu o DXR para 2^20 faixas | asai15 | CONFIRMADO | "we can extend it to 2^20" | §4.8 |
| 135 | 492–494 | FIB do Poptrie limitada a 2^16 entradas (folha de 16 bits), extensível | asai15 | CONFIRMADO | "the size of a leaf node is 16 bits, hence the number of FIB entries is limited to 2^16, though we can simply extend" | §5 |
| 136 | 496–497 | DXR declara inviável o índice direto em IPv6: 0,026% contra 60,36% | zec12 | CONFIRMADO | "(0.026%, vs. 60.36% for IPv4) [1]". c/ nota: o DXR cita a estatística de [1], bgp.potaroo.net | §3 |
| 137 | 497–498 | o Poptrie adaptou o D18R ao IPv6: 169,91 Mlps, endereços em 2000::/8 | asai15 | CONFIRMADO | "D16R and D18R ... 163.07 and 169.91 Mlps"; "random addresses within 2000::/8" | §4.10 |
| 138 | 499 | segundo o Poptrie, o SAIL não aceita prefixos acima de /64 | asai15 | CONFIRMADO | "it does not support more specific routes than /64" | §4.10 |
| 139 | 499–501 | híbrido de bitmaps e Bloom; até 12 acessos off-chip; FIBs IPv6 sintéticas derivadas das IPv4 | yang18 | CONFIRMADO | "2 + 10 hash table probes, i.e., 12 off-chip memory accesses"; "synthesize IPv6 FIBs based on the real IPv4 FIBs". O híbrido é proposto no §VII-B | §VII-B; §VII-C |
| 140 | 501–503, 529 | tabela IPv6 real de 20.440 prefixos; 211,32 Mlps; 1,24× o D18R; "less interesting" | asai15 | CONFIRMADO | valores e citação conferem. c/ nota: o artigo também avalia 13 RIBs IPv6 públicas da RouteViews (>20K prefixos), com pior caso de 211,32 Mlps | §4.10; Tab. 6 |
| 141 | 504 | o CoolCAMs diz que técnicas semelhantes servem ao IPv6, sem avaliar | zane03 | CONFIRMADO | "similar techniques can be used for IPv6 address lookups" | §I |
| 142 | 505 | L = 128; pior caso do PLO_OPT de 16 para 64 (conta nossa) | shah01 | CONFIRMADO | "L equals 32 in IPv4, and 128 in IPv6"; 128/2 = 64 | p.37 |
| 143 | 528 | ressalvas do SAIL_L: pior caso ilimitado e lookup bloqueado | yang18 | CONFIRMADO | ver os itens 104 e 105 | §III-C; Tab. II |
| 144 | 530 | DXR só para IPv4 | zec12 | CONFIRMADO | "optimized exclusively for the IPv4 protocol" | §3 |
| 145 | 533, 547–548 | o SAIL admite TCAM para prefixos ≥ /25 (proposto, não medido) | yang18 | CONFIRMADO | "to bound the worst case lookup speed, we can use TCAM or next hop arrays" | §I-D |
| 146 | 548–549 | o CoolCAMs usa uma trie numa TCAM de índice pequena | zane03 | CONFIRMADO | "initial, small-sized TCAM (containing the trie)" | §IV |
| 147 | 549–550 | os nós CAM do Tree Bitmap são codificação de nó, não um chip de TCAM | eath04 | CONFIRMADO | "replaced by a simple CAM type entry that has match bits, match length, and next hop pointers". c/ nota: o texto não diz "DRAM"; isso é dedução a partir do projeto de referência com RLDRAM (§7.2) | §5.5 |
| 148 | 564–565 | o survey publicava percentis e tratava o tráfego uniforme por prefixo como limitação | ruiz01 | CONFIRMADO | Tab. 3 com p10/p50/p99; "Although a knowledge of the access probabilities ... would allow better evaluation" | Tab. 3; p.22 |
| 149 | 566–567 | só o Poptrie publica distribuição de ciclos; o DXR dá a de passos da busca binária; o SAIL não traz distribuição de latência | asai15, zec12, yang18 | CONFIRMADO | asai15 Tab. 4; zec12 Tab. 3, "Fraction of addresses that require exactly n iterations". c/ nota: a Fig. 16 do SAIL dá faixas de latência na GPU por tamanho de lote, o que não é uma distribuição | asai15 Tab. 4; zec12 Tab. 3; yang18 Fig. 16 |
| 150 | 577–578 | "12 FIBs" listadas com 13 nomes | yang18 | CONFIRMADO | "rrc00, rrc01, rrc03, ··· rrc07, rrc10, ··· , rrc15" = 13 nomes. A Fig. 14 lista 12, sem o rrc13 | §VI-A (repete em §VI-B, §VI-D) |
| 151 | 578 | Tab. IV anunciada com 23 FIBs e 24 linhas | yang18 | CONFIRMADO | título "of 23 IPv4 FIBs"; 12 linhas rrc00-2002…2013 e 12 linhas rrcXX-2013 = 24 | Tab. IV (p.9) |
| 152 | 579 | três tamanhos para a rrc00 | yang18 | CONFIRMADO | 476,311 (§VI-B), 455 900 (§VII-C) e 495401 (rrc00-2013, Tab. IV) | §VI-B; §VII-C; Tab. IV |
| 153 | 579–580 | citações trocadas, como "Poptrie [11]" | yang18 | CONFIRMADO | [11] é Pao et al. ("bit-shuffled trie") e o Poptrie é [7]. Na mesma frase, "Lulea [36]" também está trocado: [36] é o Ruiz-Sánchez e o Lulea é [37] | §VI-C |
| 154 | 580–581 | os doze valores da Tab. 5 ficam 9 bits acima da fórmula | eath04 | INFERÊNCIA SEM MARCA | a conta está certa: 12+6(j−2) com j = ⌊acessos/lookup⌋ dá 96/198/396, 48/96/198, 48/96/192 e 24/48/96, e a tabela traz 105/207/405, 57/105/207, 57/105/201 e 33/57/105, todos +9. Falta a marca "conta nossa" | §7.2, Tab. 5 (pp.119–120) |

## refs.bib

| # | entrada | status | PDF / Crossref | observação |
|---|---|---|---|---|
| B1 | todo `\cite` tem entrada | CONFIRMADO | 7 chaves usadas (ruiz01, shah01, zane03, eath04, zec12, asai15, yang18); nenhuma entrada sobra | 3 `\cite` sem localizador: l.67, 230 e 443 (itens 8, 57 e 115) |
| B2 | ruiz01 | CONFIRMADO | o DOI não está impresso no PDF; o Crossref confirma título, autores, IEEE Network 15(2), 8–23, 2001. O PDF vai da p.8 à p.23, com rodapé "March/April 2001" | — |
| B3 | shah01 | DIVERGENTE | o PDF imprime "Fast Updating Algorithms for TCAMs", no plural; o Crossref e o bib trazem "TCAM". Autores, 21(1), pp.36–47 e 2001 conferem | diferença mínima, mas o comentário do bib diz que o título foi comparado com o PDF |
| B4 | zane03 | CONFIRMADO | o Crossref confirma o DOI, pp.42–52 e vol. 1, e não traz o ano (o comentário do bib explica). O PDF tem pp.42–52 e ISBN 0-7803-7753-2/03 | — |
| B5 | eath04 | CONFIRMADO | rodapé do PDF: "Volume 34, Number 2: April 2004", pp.97–122; Crossref igual | — |
| B6 | zec12 | CONFIRMADO | 42(5), pp.29–36, DOI ok. O mês `sep` vem do Crossref (2012-09-24); o rodapé do PDF diz "October 2012" | a p.29 é a *public review*; o artigo começa na p.30 |
| B7 | asai15 | CONFIRMADO | o DOI está impresso na p.57; pp.57–70; SIGCOMM '15, August 17–21 | — |
| B8 | yang18 | CONFIRMADO | autores, título, DOI e 2018 impressos no PDF. Vol. 26(4) e pp.1821–1836 vêm só do Crossref, porque o PDF é a versão *early access* | o grupo já usa só §; confere |

## Contagem por status

Afirmações do texto (154 itens):
- CONFIRMADO: 132
- DIVERGENTE: 17
- NÃO ENCONTRADO: 2
- INFERÊNCIA SEM MARCA: 3

refs.bib (8 itens): CONFIRMADO 7, DIVERGENTE 1.

## Itens fora de CONFIRMADO, por gravidade

Alta
1. **Item 67** (l.295 e 303–305, com o enquadramento em 42, 555 e 600). O 21,8% e o 1,66% do Poptrie medem *binary radix depth* > 24, isto é, os bits verificados até decidir o LPM. Não medem a fração de pacotes que "casa prefixos maiores que /24". Pela métrica de prefixo casado, o próprio SAIL dá 0,021–0,025% para destinos aleatórios. O argumento central pode continuar, porque é a profundidade que leva o SAIL_L ao nível 32, mas a redação está errada nos quatro lugares.
2. **Itens 15 e 110** (l.114, 402, 426, 476 e 532). Na Tab. 1 do shah01, "Prefixes" é exatamente Inserts + Deletes. Isso torna o número "35 a 43 mil prefixos" ambíguo, e ele é usado como tamanho de tabela em cinco lugares, só um deles com `\revisar`.

Média
3. **Item 11** (l.95–97). He et al. não tem PDF no corpus e não leva a marca `[NÃO VERIFICADO]`. Com o critério de referência falsa do enunciado, convém anexar o PDF ou retirar o nome.
4. **Item 103** (l.412). "Duas a três ordens de grandeza" é uma conta sem marca e imprecisa: o certo é ≈2,9 (DXR) a ≈3,6 (Poptrie), ou seja, três a quatro ordens.
5. **Item 53** (l.216 e 529). "O mesmo vale para o SAIL" omite a implantação no PEARL (§V-E), um roteador virtual com o trace real e "28 times faster".
6. **Item 109** (l.424–426). O "D não passava de 5 nas tabelas medidas" aponta para a p.40, que traz uma afirmação geral. A medição está na p.44 e na Fig. 15 (p.45).
7. **Item 23** (l.119, 293 e 320–321). O "4 de 5 implementados (§VI-A)" está sustentado só pela §VIII. O §VI-A cita apenas o D18R.
8. **Item 77** (l.332, `\revisar`). O yang18 não informa o tráfego da Fig. 14, e a figura não mostra o Poptrie. Dá para resolver o `\revisar` escrevendo "tráfego não informado".
9. **Item 154** (l.580–581). A conta dos +9 bits da Tab. 5 está correta, mas não tem a marca "conta nossa".

Baixa
10. **Item 90** (l.368). Os 782 KB do D16R estão citados no §3.4; o número está no Abstract, na Tab. 2 e na Tab. 1.
11. **Itens 8, 57 e 115** (l.67, 230 e 443). Três `\cite` sem localizador; os trechos estão no Abstract (zane03, zec12) e no §II (zane03).
12. **Item 7** (l.65–66). "Custa caro" não está no §1 do zec12 nem no do asai15; no asai15, o custo aparece no §2.
13. **Itens 45 e 87** (l.185–186 e 354–355). A trie auxiliar do shah01 está nas pp.40 e 43, não na p.38, e "fora do chip" não está escrito.
14. **Item 112** (l.429–430). A "uma escrita por atualização" do CoolCAMs está no §V e na Tab. IV, não no §II.
15. **Item 32** (l.163–164). O Pentium Pro do survey está na p.21, não na p.22.
16. **Item 3** (l.59). O "em 2014" não está no §1 do asai15; vem das datas da Tab. 1.
17. **Item 82** (l.339). "Busca binária em prefixos longos" é dedução; o asai15 fala em profundidade de radix.
18. **Item 20** (l.117). "DIR-24-8 implementado pelos autores" não está escrito no zec12 §4.3.
19. **B3**. O título do shah01 no bib está no singular ("TCAM"), conforme o Crossref, e o PDF imprime "TCAMs".

## Notas para os `\revisar` que tocam em números

- l.332 (Fig. 14 do yang18): ver o item 77. O tráfego não é informado.
- l.377 (eath04, p.120): os números estão impressos como no texto. Ver no item 91 a pista dos 400 MB.
- l.428 (Tab. 1 do shah01): ver o item 15. A suspeita do grupo procede.
- l.463 e l.465 (contas de 3,6 W e 39/20 chips): as duas contas conferem (itens 123 e 124).
