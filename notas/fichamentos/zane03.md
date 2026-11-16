# Fichamento: zane03

Arquivo: `ep2_export/Coolcams_power-efficient_TCAMs_for_forwarding_engines.pdf` (11 páginas, numeração impressa 42 a 52).
Localizadores: seção (§), figura, tabela e página impressa (p.). Página impressa = página do PDF + 41.
Convenção: [afirma] = está no PDF, com localizador; [inferência] = leitura nossa.

## Referência

- Autores: Francis Zane, Girija Narlikar, Anindya Basu (Bell Laboratories, Lucent Technologies, Murray Hill, NJ) (p. 42, cabeçalho).
- Título: "CoolCAMs: Power-Efficient TCAMs for Forwarding Engines" (p. 42).
- Veículo: não impresso no PDF. Nas páginas só aparecem o rodapé "0-7803-7753-2/03/$17.00 (C) 2003 IEEE" (p. 42) e os números de página 42 a 52.
  O campo Subject dos metadados do arquivo traz "IEEE INFOCOM 2003. Twenty-second Annual Joint Conference of the IEEE Computer and Communications Societies (IEEE Cat. No.03CH37428);2003;1". Isso vem dos metadados e não do texto impresso.
- Ano: 2003 (rodapé, p. 42).
- Páginas: 42–52 (numeração impressa).
- DOI: não impresso no PDF. Os metadados do arquivo trazem 10.1109/INFCOM.2003.1208657. Conferir em doi.org/Crossref antes de usar no BibTeX.

## Problema e premissas

- [afirma] Problema: TCAMs são populares em forwarding engines, mas consomem muita energia: "as much as 12–15 Watts each when all the entries are enabled for search" (§I, p. 42). O consumo encarece alimentação e refrigeração e reduz a densidade de portas (§I, p. 42).
- [afirma] Modelo de energia: "The main component of power consumption in TCAMs is proportional to the number of searched entries" (§II, p. 43). Os autores usam o número de entradas pesquisadas como medida do consumo: "Given that the power consumption of a TCAM is linearly proportional to the number of searched entries, we use this number as a measure of the power consumed" (§II, p. 43). Nenhuma das duas frases tem citação.
- [afirma] Hardware: TCAMs comerciais permitem pesquisar só uma sub-tabela, definida como conjunto de blocos. Exemplo do texto: uma TCAM de 512K entradas dividida em 64 blocos de 8K, com sub-tabelas definidas por máscara de 64 bits. Hoje as TCAMs suportam poucas sub-tabelas ("such as 8 sub-tables addressed by a 3-bit ID"), e os autores supõem que o mesmo mecanismo "could be used to support more sub-tables" (§II, p. 43). Em §IV-D, p. 50, K pequeno "is often a limitation on commercially available TCAMs".
- [afirma] Semântica da TCAM: quando há várias entradas casando, retorna a de menor endereço. Os prefixos ficam ordenados por comprimento decrescente, e essa ordenação "makes it difficult to update the routing table". O problema de update é delegado a [9] = Shah e Gupta (§II, p. 42–43).
- [afirma] FIB: um estudo citado [2] e os dados dos autores mostram que menos de 2% dos prefixos de núcleo têm menos de 16 ou mais de 24 bits; "The remaining 98% of the prefixes that are 16 to 24 bits long are partitioned into buckets" (§III-A, p. 43). Os prefixos curtos e longos ficam em blocos que são pesquisados em todo lookup (§III-A, p. 43).
- [afirma] Premissas da seleção de bits: só o "split set" (prefixos de 16 a 24 bits) é particionado; há uma única TCAM, por simplicidade; K = 2^k buckets; os bits de hash saem dos primeiros 16 bits, porque senão o prefixo teria de ser replicado (§III-A, p. 43–44).
- [afirma] Escala: "routing engines capable of scaling up to 1 million entries". Uma TCAM de 18 Mbit guarda até 512K prefixos de 32 bits, logo são pelo menos 2 TCAMs só para IPv4 (§II, p. 43).
- [afirma] Tráfego: não há premissa sobre tráfego. A métrica é o número máximo de entradas pesquisadas por lookup, no pior caso sobre os endereços (§III-B, p. 44; §IV-D, p. 50).
- [afirma] Taxa de atualização: "For real tables, the expectation is that such recomputations will not be necessary very often" (§III-C, p. 45). As rajadas de updates "do appear to occur every few days in real-life traces" (§V, p. 51). A nota 3 supõe que "future additions will hit the same TCAM bucket which is mostly the case, at least in the short term" (§V, p. 51).
- [afirma] IPv6: "similar techniques can be used for IPv6 address lookups" (§I, p. 42). Não há avaliação em IPv6.

## Proposta

Lookup em dois estágios: o primeiro estágio escolhe uma partição (bucket) e o segundo pesquisa só esse bucket na "data TCAM" (§I, p. 42). Na **seleção de bits** (§III), k bits fixos dos primeiros 16 do endereço indexam o bucket, por meio de muxes. Os bits são escolhidos por três heurísticas: estática (últimos k bits dos primeiros 16), gulosa e força bruta (§III-C, p. 45, Fig. 2). Na **arquitetura por trie** (§IV), uma "index TCAM" pequena, sempre pesquisada inteira, e uma "index SRAM" devolvem o ID do bucket (Fig. 5, p. 47). A partição sai de uma trie de 1 bit por dois algoritmos: *subtree-split*, com buckets de tamanho entre ⌈b/2⌉ e b (Fig. 7, p. 48), e *postorder-split*, com buckets de exatamente b prefixos (Fig. 9, p. 49). Os dois algoritmos acrescentam o "covering prefix" ao bucket para preservar o LPM. Para cada arquitetura, o artigo dá um limite de pior caso para o consumo (Teorema III.1, p. 44; Teoremas IV.4 e IV.8, p. 48–49).

## Avaliação

- Plataforma: "All the experiments were run on a 800 MHz PC and required less than 1MB of memory" (§III-D, p. 45). O texto não diz se a mesma máquina foi usada nos experimentos da trie (Fig. 11). [inferência] Não há hardware real nem medição de potência: toda "potência" é a contagem de entradas pesquisadas.
- Tabelas: Tabela II (p. 45) traz rrc04 (Geneva, 11/01/2001, 109,600) e oregon (Oregon, 05/01/2002, 121,883). Datas copiadas como impressas; o PDF não diz se o formato é MM/DD ou DD/MM. Os autores dizem que aplicaram as heurísticas a "multiple real core routing tables" e mostram 2, "The results of applying the algorithms to the other core routing tables were similar" (§III-D, p. 45). A instituição que coletou as tabelas não está impressa.
- Tabela sintética: "approximately 1 million prefixes with 2^16 unique combinations of the first 16 bits", com número de prefixos por combinação sorteado. Só foi usada na seleção de bits, para tempo de execução e qualidade do split, aparecendo como "full" nas Figs. 3 e 4 (§III-D, p. 45–46).
- Updates: "real-life updates traces (each with a few million route updates) collected at the same times and sites as the routing tables in Table II" (§V, p. 50). São 3,412,540 updates para rrc4 e 3,614,740 para oregon (Tabela III, p. 51). A duração da janela de coleta não está impressa.
- Tráfego de pacotes: não usado. Nenhum trace de pacotes; a métrica não depende de tráfego.
- Comparação: só entre as variantes propostas. A seleção de bits aparece como brute, greedy e static (Fig. 4, p. 46) e a trie como subtree, postorder e post-opt (Fig. 12, p. 50; Tabela IV, p. 51). As referências são o split ideal 2^k (§III-B, p. 44) e a busca na TCAM inteira (fator 1). Não há comparação com Liu [5] nem com esquemas algorítmicos. A frase "in the same ballpark as the SRAM-based ASIC designs [3]" (§III-D, p. 46) cita apenas o site da IDT e não traz número.
- Quem implementou: os próprios autores ("we implemented the algorithms to take as input the total number of buckets K", §IV-D, p. 50). Não há concorrente externo.

## Números

| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| consumo de TCAM de alta densidade | 12–15 | Watts | cada TCAM, todas as entradas habilitadas | §I, p. 42 |
| consumo de TCAM de 18 Mbit | up to 15 | Watts | todas as entradas pesquisadas | §II, p. 43 |
| capacidade de TCAM | up to 18Mbits | — | dispositivos que estão chegando ao mercado | §II, p. 43 |
| taxa de busca | over 100 Million | lookups/second | idem, refs. [3], [8] (sites de fabricantes) | §II, p. 43 |
| prefixos IPv4 por TCAM de 18 Mbit | 512K | prefixos de 32 bits | — | §II, p. 43 |
| escala-alvo de FIB | 1 million | entradas | tendência de núcleo, ref. [2] | §II, p. 43 |
| prefixos curtos ou longos | less than 2% | dos prefixos | <16 ou >24 bits, "in our datasets" | §III-A, p. 43 |
| prefixos de 16–24 bits | 98% | dos prefixos | — | §III-A, p. 43 |
| maior bucket (limite superior), k=3 | 0.381 | fração de N | N=1M, L=16 | Tabela I, p. 44 |
| maior bucket (limite superior), k=6 | 0.117 | fração de N | N=1M, L=16 | Tabela I, p. 44 |
| redução garantida, seleção de bits | 1/.381 = 2.62 | fator | N=1M, k=3 | §III-B, p. 44; §III-E, p. 46 |
| combinações distintas dos 16 primeiros bits | less than 12,000 | — | tabelas reais, prefixos de 16–24 bits | §III-D, p. 45 |
| tempo da força bruta | less than 16 | seconds | tabelas reais, até 10 bits | §III-D, p. 45 |
| tempo da força bruta | as high as 80 | seconds | sintética ~1M, 8 bits | §III-D, p. 45 |
| tempo da gulosa | as low as 0.05 / about 0.22 | seconds | reais (até 10 bits) / sintética | §III-D, p. 45 |
| N/cmax | nearly 53 / around 49 / 64 | fator | k=6; brute e greedy / static / ideal | §III-D, p. 46 |
| exemplo de layout: N/cmax | 512K/12K = 42.67 | fator | 512K entradas, 64 blocos de 8K, maior bucket de 12K | §III-D, p. 46 |
| exemplo de layout: blocos pesquisados | (⌈12K/8K⌉ + 1) + 2 = 5 | blocos | idem | §III-D, p. 46 |
| exemplo de layout: redução | 64/5 = 12.8 | fator | idem | §III-D, p. 46 |
| exemplo de layout: orçamento | under 1.2 | Watts | TCAM de 15 W | §III-D, p. 46 |
| redução experimental, seleção de bits | over 7.5 | fator | 3 bits, lida da Fig. 4 | §III-E, p. 46 |
| limite subtree-split | K + ⌈2N/K⌉ + 1 | prefixos pesquisados | pior caso, index + data TCAM | Teorema IV.4, p. 48 |
| limite postorder-split | (W + 1)K + ⌈N/K⌉ + W | prefixos pesquisados | pior caso | Teorema IV.8, p. 49 |
| K ótimo | √(2N) / √(N/W) | buckets | subtree / postorder | §IV-D, p. 50 |
| tempo de partição (trie) | within one second | — | tabelas da Tabela II, até K≈2000 (Fig. 11) | §IV-D, p. 50 |
| redução com 8 buckets, rrc | 7.58 / 7.55 | fator | seleção de bits, exaustiva / gulosa | §IV-D, p. 50 |
| redução com 8 buckets, rrc | 6.09 / 7.95 | fator | subtree / postorder, "including the power consumed by the index TCAM" | §IV-D, p. 50 |
| potência com 8 buckets | less than 2.5 | watts | TCAM de 15 W, qualquer dos algoritmos | §IV-D, p. 50 |
| potência com 64 buckets | less than 0.5 | watts | idem | §IV-D, p. 50 |
| pior caso, postorder | 10^6/8 = 125,000 | entradas por bucket | 1M entradas IPv4, W=32, 8 buckets | §IV-D, p. 50 |
| pior caso, postorder | 125,288 | prefixos pesquisados | + até 32 covering + index de 8 × 32 = 256 | §IV-D, p. 50 |
| pior caso, postorder | 10^6/125,288 = 7.98 | fator | independe da distribuição de prefixos | §IV-D, p. 50 |
| orçamento de pior caso | under 2 / around 5.7 | watts | "15 watt 1M-entry data TCAM"; postorder / seleção de bits | §IV-D, p. 50 |
| updates aplicados | 3,412,540 / 3,614,740 | updates | rrc4 / oregon | Tabela III, p. 51 |
| prefixos de 16–24 bits, inicial → final | 107,195 → 103,873 / 119,226 → 113,436 | prefixos | rrc4 / oregon | Tabela III, p. 51 |
| recomputações, seleção de bits | 2 / 15 | vezes | coluna static, 8 buckets, t=1%; rrc4 / oregon | Tabela III, p. 51 |
| recomputações, seleção de bits | 12 / 13 | vezes | coluna static, 64 buckets, t=1%; rrc4 / oregon | Tabela III, p. 51 |
| recomputações, trie | 0 / 58 / 3 (.07) | vezes (writes extras) | rrc4, 8 buckets, t=1%; sub / post / post-opt | Tabela IV, p. 51 |
| recomputações, trie | 3 / 74 / 2 (.07) | vezes (writes extras) | oregon, 8 buckets, t=1% | Tabela IV, p. 51 |
| recomputações, trie | 41 / 1957 / 236 (.48) | vezes (writes extras) | rrc4, 64 buckets, t=1% | Tabela IV, p. 51 |
| recomputações, trie | 14 / 1042 / 84 (.56) | vezes (writes extras) | oregon, 64 buckets, t=1% | Tabela IV, p. 51 |
| writes por update, post-opt | 1.07 | TCAM writes | 8 buckets, t=1% (contra 1 write nos demais) | §V, p. 51 |
| rajadas de updates | up to a few thousand | route additions in a single second | traces reais | §V, p. 51 |

Os valores dos gráficos (Figs. 3, 4, 11 e 12) não estão impressos em texto. O pico das curvas da Fig. 12 só pode ser lido visualmente e não deve ser citado como número exato.

## Atualização

- Unidade: [afirma] principalmente **número de recomputações**, isto é, reparticionamentos da tabela inteira. Cada uma pode exigir "rewriting the entire table in the data TCAM" (§V, p. 50; Tabelas III e IV, p. 51). A unidade secundária é **TCAM writes por update**: o mínimo é 1 write na data TCAM, e o post-opt faz em média 0.01 a 0.56 writes extras (Tabela IV, p. 51). O tempo de recomputação está em segundos (§III-D, p. 45; §IV-D, p. 50).
- Gatilho: [afirma] na seleção de bits, recalcula quando o maior bucket passa de c_thresh = (1 + t) × c_max, na ordem static → greedy → brute (§V, p. 50). Na trie, recalcula "each time any bucket overflows", com buckets de ⌈2N/K⌉ (subtree) e ⌈N/K⌉ (postorder) (§V, p. 51). O post-opt transfere prefixos para buckets vizinhos e só reparticiona quando os dois vizinhos estão cheios (§V, p. 51).
- Caso médio: [afirma] 1 TCAM write por update. No post-opt com 8 buckets e t=1%, são 1.07 (§V, p. 51). Com 8 buckets, as recomputações vão de 0 a 15 em mais de 3 milhões de updates (Tabelas III e IV, p. 51).
- Pior caso: [afirma] reescrever a data TCAM inteira (§V, p. 50), mas o artigo não dá número em writes nem em tempo. O tempo de recomputação no pior caso vai até "as high as 80 seconds" (força bruta, sintética de 1M, 8 bits; §III-D, p. 45). Na trie, fica abaixo de 1 s nas tabelas reais (§IV-D, p. 50).
- Rajadas: [afirma] "these floods often cause a single bucket in the trie-based architecture to repeatedly overflow"; a seleção de bits "requires far fewer repartitions" e "has a natural advantage compared to trie-based schemes in the face of such events" (§V, p. 51).
- [inferência] O "1 TCAM write" por update ignora os movimentos necessários para manter a ordem por comprimento de prefixo dentro do bucket, que é justamente o problema de shah01, citado como [9] em §II, p. 43. O artigo não mede esse custo.
- [inferência] As Tabelas III e IV não usam a mesma régua. A seleção de bits usa limiar relativo a c_max; a trie usa estouro de bucket com folga de ⌈2N/K⌉ ou ⌈N/K⌉. Mesmo assim, com 8 buckets e t=1%, o subtree-split recomputou menos (0 e 3) que a seleção de bits (2 e 15). A frase "far fewer repartitions" do §V vale contra o postorder-split, não contra a trie em geral.

## Memória e energia

- Energia: [afirma] o consumo é medido apenas como número de entradas pesquisadas (§II, p. 43). Os watts do texto são proporções da potência máxima nominal de 15 W (§III-D, p. 46; §IV-D, p. 50). Não há medição de potência.
- Pegada da seleção de bits: [afirma] não exige TCAM extra, só "a set of simple muxes and can be very cost effective" (§III-E, p. 46). O layout pode pesquisar até ⌈c_max/s⌉ + 1 blocos, mais os blocos de prefixos curtos e longos (§III-D, p. 46).
- Pegada da trie: [afirma] index TCAM e index SRAM com K entradas no subtree-split (Teorema IV.2, p. 48). No postorder-split, cada bucket contribui com até W + 1 entradas na index TCAM e na index SRAM (Teorema IV.6, p. 49). A data TCAM recebe ainda até 1 covering prefix por bucket no subtree-split (Teorema IV.1, p. 48) e até W no postorder-split (Teorema IV.5, p. 49).
- On-chip × off-chip: não encontrado. A TCAM é um dispositivo externo; o artigo não discute memória on-chip nem dá tamanho de SRAM em bytes.
- Preço e capacidade: [afirma] "TCAM devices have traditionally been more expensive and less dense compared to conventional ASIC-based devices. However, both the density and the cost of TCAMs have dramatically improved in the past few years" (§I, p. 42). Os dispositivos de até 18 Mbit e mais de 100 M lookups/s "are now coming to market with costs that are competitive with alternative technologies (such as pipelined ASIC-based routing engines)" (§II, p. 43, refs. [3], [8], que são sites da IDT e da Netlogic). Preço em dólares: não encontrado. O "$17.00" do rodapé (p. 42) é a taxa de copyright do IEEE e não preço de TCAM.
- Custo operacional: [afirma] alimentação e refrigeração "account for a significant portion of an ISP's operational expenses [1]" (§I, p. 42); [1] é um artigo de revista comercial (Lightwave).

## Limitações

Admitidas pelos autores:
- [afirma] O pior caso garantido pela seleção de bits "is fairly high"; o projetista "would be forced to design for a much higher worst-case power consumption than will ever be seen in practice" (§III-E, p. 46).
- [afirma] A seleção de bits supõe a maioria dos prefixos entre 16 e 24 bits: "This assumption may not hold in the future. In particular, the number of long (> 24-bit) prefixes may increase rapidly in the future [2]" (§III-E, p. 46). Pela nota 2, os limites da Tabela I aumentariam se a premissa fosse violada (p. 46).
- [afirma] A heurística estática funciona nas tabelas examinadas, mas "may not be true for tables that we have not examined or for tables of the future" (§III-C, p. 45).
- [afirma] A economia real é menor que N/c_max por causa do arredondamento de blocos e dos blocos de prefixos curtos e longos (§III-D, p. 46).
- [afirma] A trie exige "some additional hardware" (§IV, p. 47). No postorder-split, a index TCAM passa a dominar quando K > 64 (§IV-D, p. 50).
- [afirma] Rajadas de updates prejudicam a trie (§V, p. 51). Usar a própria data TCAM como index TCAM "would reduce the throughput of the lookup process by half" (§VII, p. 52).

Inferidas:
- [inferência] Não há medição de potência, latência nem vazão. A arquitetura por trie faz dois acessos sequenciais a TCAM por lookup, e o custo em latência não é avaliado.
- [inferência] O exemplo de pior caso usa uma "15 watt 1M-entry data TCAM" (§IV-D, p. 50), mas o §II, p. 43 diz que 15 W corresponde a uma TCAM de 18 Mbit com 512K prefixos. Com o modelo linear do próprio artigo e 1M entradas em dois dispositivos de 15 W, pesquisar 125,288 entradas daria cerca de 15 × 125,288/524,288 ≈ 3.6 W, não "under 2 watts".
- [inferência] A conta de 125,288 usa 8 × 32 = 256 entradas de índice, mas o Teorema IV.8 dá (W + 1)K = 264. O fator continua ≈ 7.98; a diferença é pequena, mas a conta não segue o teorema à risca.
- [inferência] Na comparação de 8 buckets (§IV-D, p. 50), os fatores da trie incluem a index TCAM. Os da seleção de bits (7.58 e 7.55) parecem vir da métrica N/c_max, que deixa de fora os blocos de prefixos curtos e longos (§III-D, p. 46). As duas colunas não são diretamente comparáveis.
- [inferência] Os limites com K = 64 ou mais supõem TCAMs com mais sub-tabelas do que as "8 sub-tables" típicas da época (§II, p. 43).
- [inferência] As tabelas reais têm de 109,600 a 121,883 prefixos (Tabela II). O cenário de 1M só aparece na análise teórica e na tabela sintética, que é uniforme e foi chamada pelos próprios autores de mais fácil (§III-D, p. 46).
- [inferência] Detalhe editorial: a legenda da Fig. 8 (p. 48) fala em "five resulting buckets", mas a tabela (e) mostra 4.

## Ganchos com outros artigos do corpus

- shah01: [afirma] citado como [9] (Shah e Gupta, IEEE Micro 2001) em §II, p. 43 ("recent work [9] has proposed innovative algorithms for performing TCAM updates simply and efficiently") e em §VI, p. 51 ("Two solutions for this problem of updating TCAM-based routing tables have been proposed more recently [9]"). zane03 delega a shah01 a ordenação por comprimento e não incorpora o custo em movimentos no próprio custo de update. [inferência] Cruzar a unidade de shah01 (movimentos por update) com o "1 TCAM write" de zane03.
- ruiz01: não citado (verificado na lista de referências, p. 52). A nota 4 diz que referências a algoritmos de lookup em software ou ASIC foram omitidas "due to lack of space" (p. 51). [inferência] As frases de §I, p. 42, de que tries "may require multiple memory accesses" e de que TCAMs são "much easier to manage and update than tables implemented using tries", devem ser confrontadas com a taxonomia de ruiz01.
- eath04, zec12, asai15, yang18: não citados, porque são posteriores (2004 a 2018). [inferência] A tese de zane03 (TCAM "cost-effective", consumo como único problema que resta) é o contraponto natural aos esquemas algorítmicos em SRAM, DRAM ou cache. Conferir nos respectivos fichamentos como cada um caracteriza custo e energia de TCAM antes de chamar de contradição.
- Interno: a própria introdução se tensiona. §I, p. 42 diz que TCAMs são mais fáceis de atualizar que tries; §II, p. 43 diz que a ordenação "makes it difficult to update"; §V, p. 50 admite reescrever a tabela inteira a cada reparticionamento.

## Afirmações antigas (IA, 31/10): conferência

1. **CONFIRMADO.** Resumo, p. 42: "Ternary Content-Addressable Memories (TCAMs) are becoming very popular for designing high-throughput forwarding engines on routers: they are fast, cost-effective and simple to manage. However, a major drawback of TCAMs is their high power consumption." O termo impresso é "cost-effective". "Econômica" é tradução nossa. O resumo não traz número de preço; a afirmação de custo se apoia em §I, p. 42 e §II, p. 43, com refs. [3] e [8], que são sites de fabricantes.
2. **CONFIRMADO.** §II, p. 43: "The main component of power consumption in TCAMs is proportional to the number of searched entries." Na mesma página: "linearly proportional to the number of searched entries". É premissa sem citação e sem medição.
3. **CONFIRMADO, com ressalvas.** §IV-D, p. 50: "a data TCAM that can support 8 buckets, and an IPv4 routing table with 1 million entries (here W = 32)… 10^6/125,288 = 7.98; this reduced power budget is independent of the distribution of prefixes". Ressalvas: (a) o valor vale para o postorder-split, não para a seleção de bits (2.62) nem para o subtree-split; (b) o 1M é exato (10^6) e hipotético, porque as tabelas reais têm cerca de 110K–122K (Tabela II, p. 45); (c) o texto não diz que a tabela de 1M é "de núcleo" (o núcleo aparece em §II, p. 43, como tendência de escala); (d) a conta usa 256 entradas de índice, e o Teorema IV.8 daria 264.
4. **CONFIRMADO.** §III-A, p. 43: "less than 2% in our datasets" são curtos (<16) ou longos (>24); "The remaining 98% of the prefixes that are 16 to 24 bits long are partitioned into buckets". §III-E, p. 46: "assumes that the bulk of the prefixes lie in the 16-24 bit range. This assumption may not hold in the future… the number of long (> 24-bit) prefixes may increase rapidly in the future [2]". Detalhe: o 98% é uma observação dos dados de §III-A; em §III-E o texto diz "bulk".
5. **CONFIRMADO, com ressalva.** A trie fica numa "separate, small TCAM" (§I, p. 42; Fig. 5 e §IV, p. 47), e os esquemas por trie "do not assume that the bulk of the prefixes lie in the 16-24 bit range" (§IV, p. 46). Sobre as rajadas, §V, p. 51: "these floods often cause a single bucket in the trie-based architecture to repeatedly overflow… the bit selection scheme… requires far fewer repartitions". Ressalva: a Tabela IV conta recomputações ao longo de todo o trace e não isola as rajadas. Com 8 buckets, o subtree-split recomputou menos (rrc4 0, oregon 3) que a seleção de bits (2 e 15, Tabela III). A afirmação vale sem ressalva só para o postorder-split.
