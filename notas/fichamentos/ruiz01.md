# ruiz01: Ruiz-Sánchez, Biersack, Dabbous (2001). Survey and Taxonomy of IP Address Lookup Algorithms

Fonte lida: `ep2_export/Survey_and_taxonomy_of_IP_address_lookup_algorithms.pdf` (versão publicada, 16 páginas no PDF,
páginas 8 a 23 da revista). A revista não numera seções. Por isso o localizador é "título da seção, p. N", com N
sendo a página impressa no rodapé.

**Aviso de extração.** O `pdftotext` perde o "µ" e os expoentes. Na camada de texto, a Tabela 3 sai como "(ms)" e o
"3.5 µs" da p. 22 sai como "3.5 ms". Na página renderizada os dois estão em **µs**, e a Fig. 22 tem o eixo em
"Microseconds". Os expoentes também somem: "2k–1" é 2^(k–1) e "224" é 2^24. Todos os números abaixo foram conferidos
na página renderizada.

## Referência
- **Autores:** Miguel Á. Ruiz-Sánchez (INRIA Sophia Antipolis, Universidad Autónoma Metropolitana); Ernst W. Biersack
  (Institut Eurécom Sophia Antipolis); Walid Dabbous (INRIA Sophia Antipolis). p. 8.
- **Título:** "Survey and Taxonomy of IP Address Lookup Algorithms". p. 8.
- **Veículo:** IEEE Network, "March/April 2001" (rodapé de todas as páginas). Linha de copyright: "0890-8044/01/$10.00 ©
  2001 IEEE" (p. 8).
- **Páginas:** 8 a 23 (rodapés da primeira e da última página).
- **Volume/número:** não impresso no PDF. Os metadados do arquivo trazem "15;2", mas isso não aparece impresso.
- **DOI:** não impresso no PDF. O campo Subject dos metadados traz `10.1109/65.912716`, mas também não aparece impresso.

## Problema e premissas
- [afirma] Problema: lookup = achar o prefixo mais longo que casa com o endereço de destino. Com CIDR os prefixos têm
  comprimento arbitrário e a busca fica "em duas dimensões: valor e comprimento". Notação: N = nº de prefixos,
  W = comprimento máximo (32 no IPv4). "Difficulty of the Longest Matching Prefix Search", p. 10.
- **FIB**
  - [afirma] A tabela cresce. Fig. 5 (Telstra, 21/12/2000) mostra três fases: exponencial antes do CIDR, quase linear de
    meados de 1994 a meados de 1998, exponencial de novo a partir de meados de 1998. Conclusão dos autores: "Algorithms
    must be scalable with respect to the number of prefixes". "Requirements on Address Lookup Algorithms", p. 10.
  - [afirma] A distribuição de comprimentos é dominada pelo /24 (Fig. 6, escala log, p. 10; texto na p. 11). Segundo
    Huston [2], "40 percent of the entries of a typical backbone forwarding table are prefix exceptions". p. 11.
  - [afirma] Tabela de referência: MaeEast [5] com 47,113 prefixos ("Path-Compressed Tries", p. 12; Fig. 22, p. 22).
    Em 16/08/1999 a MaeEast tinha só 96 prefixos maiores que 24 bits ("Multibit Tries in Hardware", p. 16).
- **Tráfego**
  - [afirma] Enlaces de backbone de "several gigabits per second" exigem "millions of packets per second on each of
    their ports". Abstract, p. 8.
  - [afirma] Traces de tráfego não são públicos e a estatística depende do local do roteador. Por isso a medição supõe
    que todo prefixo tem a mesma probabilidade de acesso. "Measured Lookup Time", p. 21–22.
- **Hardware**
  - [afirma] O modelo de custo é o de um computador com hierarquia de memória: estruturas pequenas cabem na cache e o
    número de acessos à memória deve ser minimizado. "Memory Hierarchy in Computers", p. 13–14.
  - [afirma] A única arquitetura dedicada discutida é a de Gupta et al. [8], com dois bancos de memória.
    "Multibit Tries in Hardware", p. 16.
  - [afirma] CAM/TCAM: não aparece no texto. Busquei CAM, TCAM, "associative" e "ternary" no PDF inteiro, sem
    ocorrências.
- **Taxa de atualização**
  - [afirma] "Labovitz [1] found that backbone routers may receive bursts of route changes at rates exceeding several
    hundred prefix updates per second. He also found that, on average, route changes occur 100 times/s. Thus, update
    operations must be performed in 10 ms or less." "Requirements on Address Lookup Algorithms", p. 11.
  - [inferência] Os 10 ms saem da média (1/100 s), não das rajadas. Com rajadas acima de algumas centenas por segundo,
    o orçamento por update cairia para poucos ms. O próprio artigo não faz essa conta.

## Proposta
Não propõe algoritmo. É um survey com três partes:
1. Uma taxonomia pelo "aspecto algoritmo–estrutura de dados": busca em valores ou em comprimentos, linear ou binária
   (p. 13).
2. Quatro técnicas auxiliares: transformação de prefixos, compressão, otimização e hierarquia de memória (p. 13–14).
3. Uma comparação em dois níveis: complexidade assintótica de lookup, update e memória (Tabela 2, p. 20) e tempo de
   lookup medido em plataforma comum, com código dos autores originais (Tabelas 3–4 e Fig. 22, p. 22).

A tese central é que há um trade-off entre tempo de lookup e tempo de update incremental. "In the worst case the entire
data structure needs to be rebuilt" (Summary, p. 22).

### Taxonomia (o "mapa")
- **Eixos [afirma].** A dimensão buscada (valor ou comprimento) e o modo de busca (linear ou binário). "New IP Lookup
  Algorithms" e "A Taxonomy of IP Lookup Algorithms", p. 12–13.
- **Busca em valores [afirma].** "A Taxonomy...", p. 13; "Prefix Range Search", p. 19–20.
  - Busca sequencial num array de prefixos: O(N), "not scalable".
  - Busca binária em valores, que vira range search: Lampson et al. [14] e multiway range trees [15].
- **Busca em comprimentos [afirma].** p. 13.
  - Linear sobre a trie: trie binária e multibit tries.
  - Linear com uma tabela hash por comprimento: O(W).
  - Binária em comprimentos: Waldvogel et al. [6], p. 18–19.
- **Técnicas auxiliares [afirma].** "Auxiliary Techniques", p. 13–14.
  - Transformação de prefixos: expansão; prefixos disjuntos com leaf pushing [7].
  - Compressão: por exemplo run-length.
  - Otimização: escolher o conjunto de prefixos que minimiza memória.
  - Hierarquia de memória.
- **Esquemas cobertos, organizados pelo eixo algoritmo–estrutura [afirma].**
  - Multibit tries, p. 14–18: esquema básico e escolha de strides; update; hardware (Gupta [8]); path compression
    (LC trie, Nilsson [9]); otimização (Srinivasan [7] com programação dinâmica, Cheung [10]); compressão (Crescenzi
    [11], Lulea [12], Full Tree Bit Map de Eatherton [13]).
  - Busca binária em comprimentos, p. 18–19.
  - Range search, p. 19–20.
- **Critérios de comparação [afirma].** "The ideal scheme would be one with fast searching, fast dynamic updates, and a
  small memory requirement. [...] The most important metric is obviously lookup time, but update time must also be
  taken into account, as well as memory requirements. Scalability is also another important issue, with respect to both
  the number and length of prefixes." "Comparison and Measurements of Schemes", p. 20. O Abstract (p. 8) resume em
  "lookup speed, scalability, and update overhead".

### Tabela 2: complexidade (p. 20, transcrita da página renderizada)
| Scheme | Worst case lookup | Update | Memory |
|---|---|---|---|
| Binary trie | O(W) | O(W) | O(NW) |
| Path-compressed tries | O(W) | O(W) | O(N) |
| k-stride multibit trie | O(W/k) | O(W/k + 2^k) | O(2^k NW/k) |
| LC trie | O(W/k) | – | O(2^k NW/k) |
| Lulea trie | O(W/k) | – | O(2^k NW/k) |
| Full expansion/compression | 3 | – | O(2^k + N^2) |
| Binary search on prefix lengths | O(log2 W) | O(N log2 W) | O(log2 W) |
| Binary range search | O(log2 N) | O(N) | O(N) |
| Multiway range search | O(log2 N) | O(N) | O(N) |
| Multiway range trees | O(log2 N) | O(k log_k N) | O(N k log_k N) |

- [afirma] O "–" significa que o update incremental é "difficult if not impossible" (Lulea, full
  expansion/compression) ou "very difficult" (LC trie). "Complexity Analysis", p. 21.
- [inferência] Há uma inconsistência interna na linha "Binary search on prefix lengths". A Tabela 2 dá memória
  O(log2W), mas o texto diz "memory consumption has complexity O(Nlog2W)" ("Binary Search on Lengths", p. 21).
  Tudo indica erro na tabela. Na revisão, citar o texto.

## Avaliação
- **Plataforma [afirma].** "Pentium-Pro-based computer with a clock speed of 200 MHz", "memory cache L2 is 512 kbytes",
  código em C, Linux. "Measured Lookup Time", p. 21.
- **Tabela [afirma].** MaeEast, 16/08/1999, 47113 prefixos (ref. [5], IPMA/Merit). Fig. 22 e Tabela 4, p. 22.
  Só uma tabela, de uma única data.
- **Tráfego [afirma].** "every prefix has the same probability of being accessed" e "random permutation of all entries
  in the forwarding table (extended to 32 bits by adding zeroes)". p. 22.
- **Comparados (5 esquemas) [afirma].** BSD trie, multibit trie, LC trie, full expansion/compression e binary search
  on prefix lengths. Fig. 22 e Tabela 3, p. 22.
  - O multibit trie medido usa stride variável com fill factor de 50 percent. p. 22.
  - Não entram na medição: Lulea, Gupta, range search, multiway range trees e Full Tree Bit Map. [inferência, por
    ausência nas Tabelas 3–4 e na Fig. 22]
- **Quem implementou [afirma].** "The code for the path-compressed trie (BSD trie) was extracted from the FreeBSD
  implementation, the code for the multibit trie was implemented by us [16], and the code for the other schemes was
  obtained from the corresponding authors." p. 21. Agradecimentos (p. 23): Waldvogel, Lampson, Srinivasan, Varghese,
  Crescenzi, Dardini, Grossi, Nilsson e Karlsson.
- **O que é medido [afirma].** Só tempo de lookup (Tabela 3, Fig. 22) e altura das tries (Tabela 4). Update e memória
  não são medidos na plataforma comum. [inferência, por ausência]

## Números
| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| updates em média (Labovitz) | 100 | times/s | backbone, citado de [1] | "Requirements...", p. 11 |
| rajadas de updates (Labovitz) | "exceeding several hundred" | prefix updates per second | backbone, citado de [1] | "Requirements...", p. 11 |
| tempo máximo por update | 10 | ms ("10 ms or less") | derivado da média de 100/s | "Requirements...", p. 11 |
| exceções de agregação (Huston) | 40 | percent das entradas | "typical backbone forwarding table", citado de [2] | "Requirements...", p. 11 |
| entradas na tabela Telstra em jan./2001 | ~100,000 (leitura do eixo, não é valor impresso) | entradas | 21/12/2000 | Fig. 5, p. 10 |
| acessos no pior caso, trie binária IPv4 | 32 | acessos à memória | — | p. 12; "The Basic Scheme", p. 14 |
| acessos no pior caso, stride 4 | 8 | acessos à memória | IPv4 | "The Basic Scheme", p. 14 |
| nós da BSD trie | 93,304 | nós | 47,113 prefixos [5] | "Path-Compressed Tries", p. 12 |
| altura da BSD trie (máx./média) | 26 / "almost 20" | níveis | 47,113 prefixos | p. 12 |
| altura da trie binária (máx./média) | 30 / "almost 22" | níveis | mesma tabela | p. 12 |
| nós modificados por update em multibit trie | 2^(k–1) (no máximo) | nós | subtrie de stride k, sem leaf pushing | "Updating Multibit Tries", p. 15; p. 21 |
| Gupta, 1º banco | 2^24 entradas × 2 bytes = 32 Mbytes | — | ponteiros de 15 bits | "Multibit Tries in Hardware", p. 16 |
| Gupta, 2º banco | 2^20 entradas de 1 byte (1 Mbyte), "maximum of 2^12 = 4096 subtries" | — | exemplo dos autores | p. 16 |
| prefixos maiores que /24 | 96 | prefixos | MaeEast, 16/08/1999 | p. 16 |
| Gupta, lookup | "maximum of two memory accesses" | acessos | — | p. 16 |
| Crescenzi, acessos | "three memory accesses" | acessos | strides 16/16, expansão a 32 bits | "Multibit Tries and Compression", p. 18 |
| Crescenzi, memória | 1.2 | Mbytes | "typical backbone forwarding table"; "not small enough to fit in the cache" | p. 18 |
| Lulea, strides | 16,8,8 | bits | altura 3 | p. 18 |
| Lulea, acessos | 4 por nível; 12 no pior caso | referências à memória | IPv4 | p. 18 |
| Lulea, memória | 160 | kbytes | 32,732 prefixos | p. 18 |
| markers por prefixo (Waldvogel) | log2 W (máximo) | markers | — | "Binary Search on Prefix Lengths", p. 18; p. 21 |
| intervalos básicos (range search) | 2N (pior caso) | intervalos | — | "Range Search", p. 21 |
| BMPs recomputados por update (range search) | N (pior caso) | intervalos | — | p. 20 |
| plataforma | 200 MHz; L2 512 kbytes | — | Pentium Pro, C, Linux | "Measured Lookup Time", p. 21 |
| lookup BSD trie, percentis 10/50/99 | 4.63 / 5.95 / 8.92 | µs | MaeEast 47113, tráfego uniforme | Tabela 3, p. 22 |
| lookup multibit trie, percentis 10/50/99 | 0.82 / 1.33 / 2.99 | µs | idem; stride variável, fill factor 50% | Tabela 3, p. 22 |
| lookup LC trie, percentis 10/50/99 | 0.95 / 1.28 / 1.98 | µs | idem | Tabela 3, p. 22 |
| lookup full expansion/compression, percentis 10/50/99 | 0.26 / 0.48 / 0.84 | µs | idem | Tabela 3, p. 22 |
| lookup binary search on prefix lengths, percentis 10/50/99 | 1.09 / 1.58 / 7.08 | µs | idem | Tabela 3, p. 22 |
| lookup com 5 hashes (busca binária em comprimentos) | "about 3.5" | µs | grupos de 1 a 5 hashes | p. 22; Fig. 23, p. 23 |
| altura média/máxima, trie binária | 21.84 / 30 | níveis | MaeEast 16/08/1999 | Tabela 4, p. 22 |
| altura média/máxima, BSD trie | 19.95 / 26 | níveis | idem | Tabela 4, p. 22 |
| altura média/máxima, LC trie | 1.81 / 5 | níveis | idem | Tabela 4, p. 22 |
| altura média/máxima, multibit trie | 2.76 / 12 | níveis | idem | Tabela 4, p. 22 |

## Atualização
- **Unidade [afirma].** Não há medição de tempo de update. O custo aparece de duas formas:
  - Complexidade assintótica, em operações ou entradas modificadas (Tabela 2, p. 20).
  - Contagens qualitativas: nós modificados (2^(k–1), p. 15), intervalos cujo BMP é recomputado (N, p. 20) e markers
    ou BMPs pré-computados (O(N log2 W), p. 21).
  - O único requisito em tempo é "10 ms or less" (p. 11).
- **Caso médio:** não encontrado. Nenhum valor medido ou analítico de caso médio.
- **Pior caso [afirma].** Leitura da Tabela 2 e do texto:
  - Multibit sem leaf pushing: O(W/k + 2^k).
  - Com leaf pushing os BMPs deixam de ser locais e "updates will suffer longer worst case times" (p. 15).
  - Gupta: "updates may take a long time in some cases" (p. 16).
  - Busca binária em comprimentos: O(N log2 W).
  - Range search: O(N). Multiway range trees: O(k log_k N).
  - Lulea e full expansion/compression: "Rebuilding the whole structure is the only solution" (p. 18).
  - LC trie: "very difficult" (p. 17, p. 21).
- **Otimização [afirma].** "Using optimization techniques makes sense if the entries of the forwarding table do not
  change at all or change very little, but this is rarely the case for backbone routers." Inserir e remover degrada o
  ganho e pode exigir reconstrução. "Multibit Tries and Optimization Techniques", p. 17.
- **Estrutura auxiliar [afirma].** A multibit trie com expansão precisa de "an additional structure for managing
  original prefixes" para suportar remoção. p. 16.

## Memória e energia
- [afirma] Memória total só em complexidade (Tabela 2) e em valores reportados de outros trabalhos, não medidos aqui:
  Crescenzi 1.2 Mbytes; Lulea 160 kbytes para 32,732 prefixos; Gupta 32 Mbytes + 1 Mbyte. p. 16 e 18.
- **Total × on-chip.** Não usa os termos on-chip/off-chip. A distinção equivalente é entre caber na cache ou não:
  - Lulea: "references are almost always to the cache memory because the whole data structure is very small" (p. 18).
  - Crescenzi: "not small enough to fit in the cache memory" (p. 18).
  - Cheung [10]: três níveis de memória hierárquica com tempos e tamanhos diferentes (p. 17).
- **Energia/consumo:** não encontrado.
- **Custo (US$, área):** não encontrado.

## Limitações
Admitidas pelo artigo:
- [afirma] Tráfego uniforme por prefixo. "Although a knowledge of the access probabilities [...] would allow better
  evaluation of the average lookup time, assuming constant traffic per prefix still allows us to measure important
  characteristics, such as the worst-case lookup time." p. 22.
- [afirma] Variações pequenas nos tempos se devem a "cache misses as well as background operating system tasks".
  p. 22.
- [afirma] O fill factor é "simply a reasonable heuristic" e "does not allow a guarantee on worst-case height". p. 17.
- [afirma] O mecanismo de decodificação do Lulea não é detalhado: "Due to lack of space". p. 18.
- [afirma] O limite O(NW) da trie binária "is not tight". p. 21.
- [afirma] Multibit tries "scale badly to longer addresses" (IPv6). Range search é escalável para IPv6 "if the number
  of entries does not grow excessively". "Scalability and IPv6", p. 21.

Inferidas:
- [inferência] O artigo declara três eixos (lookup, update, memória) mais escalabilidade, mas só mede lookup. Update e
  memória ficam no plano assintótico ou em números de terceiros obtidos em tabelas diferentes. Não serve como fonte
  de comparação empírica de update.
- [inferência] Uma tabela só (47113 prefixos, 1999), sem variar N. A escalabilidade com N, apontada como requisito na
  p. 10, não é testada.
- [inferência] As chaves de lookup são os próprios prefixos completados com zeros. A distribuição dos comprimentos
  casados segue a da tabela (dominada pelo /24), não a de tráfego real.
- [inferência] Hardware de 2001 (Pentium Pro 200 MHz, L2 de 512 kbytes) e código de origens diferentes: FreeBSD,
  implementação dos autores e código dos autores originais. Os valores absolutos não se transferem e o nível de
  otimização entre implementações não é controlado.
- [inferência] O requisito de 10 ms é de fonte secundária (tese de Labovitz, 1999) e usa só a média.
- [inferência] O artigo não tem ramo de CAM/TCAM, energia ou custo. Como "mapa", precisa ser complementado por
  shah01 e zane03.
- [inferência] Não há seção de problemas em aberto. O que fica em aberto, pelo texto:
  - o trade-off lookup × update incremental (Summary, p. 22);
  - a escalabilidade para IPv6 (p. 21);
  - a avaliação com tráfego real, sem traces públicos (p. 21–22);
  - a extensão para classificação de pacotes [17] (Summary, p. 23).

## Ganchos com outros artigos do corpus
- **shah01 (Shah & Gupta, "Fast Updating Algorithms for TCAMs").** O survey não menciona TCAM. Ele cita Gupta, Lin e
  McKeown [8] (DIR-24-8, p. 16); Pankaj Gupta, coautor de [8], também assina shah01 (conferido na p. 1 desse PDF).
  [inferência] Os eixos se complementam: o ruiz01 fixa o requisito de update em 10 ms, e o shah01 ataca o update no
  ramo TCAM, que o ruiz01 não cobre.
- **zane03 (CoolCAMs).** Sem citação. [inferência] O ruiz01 não trata energia nem TCAM, e o zane03 preenche esse eixo
  do mapa.
- **eath04 (Tree Bitmap, Eatherton/Varghese/Dittia).** [afirma] O survey cita a tese "Full Tree Bit Map" de Eatherton
  [13] numa frase só: "Leaf pushing is avoided, so incremental updates are allowed" (p. 18). Não entra na Tabela 2 nem
  na medição. [inferência] O eath04 é o desenvolvimento publicado dessa linha.
- **zec12 (DXR).** [afirma, lado do DXR] O DXR cita o survey como [14]: "Ruiz-Sanchez et al. [14], and Waldvogel et al.
  [20] give useful surveys of software solutions up to the year 2001" (§2 Related Work, p. 3 do PDF
  2378956.2378961.pdf). [inferência] O DXR descende do ramo range search (Lampson [14] do ruiz01, p. 19–20) e do
  DIR-24-8.
- **asai15 (Poptrie).** Sem citação ao survey no PDF do Poptrie (busca por "Ruiz" e "taxonomy" sem resultado).
  [inferência] Pertence ao ramo multibit trie + compressão (Lulea, p. 18).
- **yang18 (SAIL, ToN).** [afirma, lado do SAIL] O SAIL cita o survey como [36] para trie binária, "binary range
  search" e lista de algoritmos (§II Related Work, p. 2 do PDF Sail_2_ToN_18.pdf), e também como referência do Lulea
  ("similar to Lulea [36]", p. 11 do PDF). [inferência] O SAIL acrescenta categorias que o ruiz01 não tem (Bloom
  filter, TCAM, FPGA, GPU, multi-FIB). É um sinal de que o mapa de 2001 precisa de ramos novos.

## Conferência das afirmações antigas (IA, 01/11)
1. **CONFIRMADO, com ressalvas de redação.**
   - A seção "Requirements on Address Lookup Algorithms" começa na p. 10 (coluna direita) e a frase está no topo da
     p. 11. Transcrição: "Labovitz [1] found that backbone routers may receive bursts of route changes at rates
     exceeding several hundred prefix updates per second. He also found that, on average, route changes occur 100
     times/s. Thus, update operations must be performed in 10 ms or less."
   - A referência [1] (p. 23) é: C. Labovitz, "Scalability of the Internet Backbone Routing Infrastructure," Ph.D.
     thesis, Univ. of Michigan, 1999.
   - Ressalva 1: o original diz "exceeding several hundred", não "algumas centenas".
   - Ressalva 2: os 10 ms são derivados da média de 100/s, não das rajadas. "No máximo ~10 ms" corresponde a "10 ms or
     less".
2. **CONFIRMADO.** O rodapé da primeira página é "8" (p. 8, com "0890-8044/01/$10.00 © 2001 IEEE") e o da última é
   "23". O PDF tem 16 páginas.
