# shah01: Shah & Gupta, "Fast Updating Algorithms for TCAMs"

Arquivo: `ep2_export/Fast_updating_algorithms_for_TCAM.pdf` (12 páginas de PDF, que correspondem às pp. 36–47 impressas).
Convenção: "p. N" é a página impressa (página do PDF = N − 35). As seções do artigo **não são numeradas**, então cito pelo título da seção.
Marcação: [afirma] = está no PDF, com localizador; [inferência] = conclusão minha.

## Referência

- **Autores**: Devavrat Shah, Pankaj Gupta (Stanford University) (p. 36).
- **Título**: "Fast Updating Algorithms for TCAMs" (p. 36).
- **Veículo**: IEEE Micro (rodapé das páginas pares, p. 38, 40, ..., 46).
- **Mês/ano**: January–February 2001 (rodapé das páginas ímpares, p. 37, ..., 47). Linha de copyright: "0272-1732/01/$10.00 © 2001 IEEE" (p. 36).
- **Páginas**: 36–47 (o texto termina na p. 46; referências e biografias ficam na p. 47).
- **Volume / número**: não impresso no PDF.
- **DOI**: não impresso no PDF. O campo Subject dos metadados do arquivo traz "IEEE Micro;2001;21;1;10.1109/40.903060", ou seja, vol. 21, n. 1, DOI 10.1109/40.903060. Isso vem dos metadados, não do texto impresso.
- Título corrente das páginas pares: "TERNARY CAMS".

## Problema e premissas

- **Problema** [afirma]: a TCAM faz LPM guardando as entradas em ordem decrescente de comprimento de prefixo. Manter essa lista ordenada torna as atualizações incrementais lentas: na inserção ingênua, é preciso mover O(N) entradas (p. 37, 1ª col.).
- **Por que a ordem importa (prioridade pela posição)** [afirma]: a TCAM compara o endereço com todas as entradas em paralelo, e "a priority encoder logic then selects the first matching entry—the entry with the matching prefix at the lowest physical memory address" (p. 38, §Longest prefix matching using TCAMs, Fig. 1). Assim, a prioridade é a posição física. Para que o primeiro casamento seja o mais longo, prefixos sobrepostos mais longos precisam ficar em endereços menores (p. 37–38). A alternativa é um circuito de máximo sobre os comprimentos, o que elimina a ordenação, mas "computing the maximum of O(M)/log2 M-bit numbers is expensive in current technology in terms of logic area and speed" (p. 37, 2ª col.).
- **Relaxamento** [afirma]: só prefixos que se sobrepõem precisam de ordem, isto é, os que estão na mesma cadeia raiz→folha da trie ("chain-ancestor ordering constraint") (p. 40, Fig. 6; p. 37, 2ª col.).
- **Hardware** [afirma]:
  - M "is around 16K to 64K presently" (p. 37).
  - Uma escrita na memória leva um ciclo de 20 ns, e a lookup engine faz um lookup em 20 ns. Essas são premissas do exemplo do algoritmo ingênuo (p. 39).
  - Algumas TCAMs têm "single-cycle update time" (Netlogic, p. 38).
  - Os algoritmos não exigem circuito adicional no chip (p. 46).
- **Software de gerência** [afirma]: "We also assume a memory manager software that arranges prefixes in the desired order and sends appropriate instructions to the TCAM hardware" (p. 38). Esse software mantém uma trie auxiliar (p. 40; p. 43, §Auxiliary trie data structure).
- **FIB** [afirma]:
  - Prefixos com menos de 8 bits "are typically not found in forwarding tables" (p. 38, legenda da Fig. 2).
  - Menos de 0,1% dos prefixos têm mais de 24 bits (p. 44).
  - D (comprimento máximo de cadeia) "is usually small (at most 5) for even large backbone forwarding tables" (p. 40).
  - L = 32 em IPv4 e 128 em IPv6 (p. 37).
- **Taxa de atualização** [afirma]: "These changes can occur at the rate of approximately 100 to 1,000 prefixes per second.15" (p. 38). A taxa de lookup é "on the order of millions of packets per second" (p. 38).
- **Ocupação** [afirma]: "The algorithms described here assume that the maximum number of entries is almost the same as the TCAM size" (p. 46, parágrafo final).
- **Algoritmos online** [afirma]: tratam cada pedido de update quando ele chega, sem agrupar em lote (p. 37).
- **Tráfego de pacotes**: não é modelado. Não há carga de lookup na avaliação, só traços de update (p. 43) [afirma a ausência; inferência quanto à consequência].

## Proposta

O artigo apresenta dois gerenciadores de layout para a TCAM, ambos com o pool de entradas livres no **centro** da memória (p. 40–41).
- **PLO_OPT** mantém a ordem por comprimento. Os prefixos de comprimento L..L/2 ficam acima do pool e os de L/2−1..1 ficam abaixo. Um insert ou delete troca no máximo L/2 entradas, e os autores dizem que o algoritmo é ótimo online sob essa restrição (p. 40–41, Fig. 7).
- **CAO_OPT** só ordena prefixos da mesma cadeia. As cadeias maximais da trie são distribuídas de forma equilibrada em volta do pool, de modo que cada prefixo fica a no máximo D/2 posições de uma entrada livre (p. 41–43, Figs. 8–12). A trie auxiliar ganha os campos wt, wt_ptr e hcld_ptr, mantidos em O(L) (p. 43).
- A proposta também se estende à classificação de pacotes, usando uma "constraint tree" (p. 46).

## Avaliação

- **Plataforma**: simulação (§Simulation results, p. 43). Linguagem, máquina e simulador não são descritos (não encontrado). Não houve implementação em hardware.
- **Tabelas** [afirma]: "two publicly available routing-table snapshots (at MAE-EAST and MAE-WEST network access points)" (p. 43). Tamanhos na Tabela 1 (p. 43): MAE-EAST 43344 e MAE-WEST 35217 prefixos. **Data dos snapshots: não encontrado.**
- **Workload de update** [afirma]: "three-hour BGP-update traces on these snapshots taken from Merit (www.merit.edu/ipma/routing_table)" (p. 43). Tabela 1: Inserts 34204 / 34114 e Deletes 9140 / 1103 (EAST / WEST). **Data dos traços: não encontrado.**
- **Tráfego de lookup**: nenhum. A métrica é só o número de movimentos de memória por update.
- **Comparação**:
  - Na simulação, a comparação é contra o **L-algorithm**, o esquema de "some TCAM vendors" com até L movimentos (p. 37, que cita a Sibercore Technologies, "www.sibercore.com/scan01_cidr_p03.pdf current Feb. 2000"; p. 39, Fig. 5).
  - O algoritmo ingênuo (O(N)) e o de espaços vazios intercalados (O(X) médio, O(N) pior caso) aparecem só como análise (p. 39, Figs. 3–4).
  - O circuito de máximo e a ref. 14 (Kobayashi et al.) são discutidos, mas não avaliados (p. 37).
- **Quem implementou o concorrente**: não dito. [inferência] Os próprios autores simularam o L-algorithm a partir da descrição do fabricante.

## Números

| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| velocidade de enlace | 40 | Gbps | por fibra instalada (DWDM) | p. 36 |
| porta máxima de roteador | 10 Gbps (OC192) | Gbps | "available now" | p. 36 |
| tamanho de TCAM (M) | 16K to 64K | entradas | "presently" | p. 37 |
| L | 32 / 128 | bits | IPv4 / IPv6 | p. 37 |
| taxa de mudança da FIB | 100 to 1,000 | prefixes per second | cita a ref. 15 | p. 38 |
| taxa de lookup | millions of packets per second | pps | ordem de grandeza | p. 38 |
| update ingênuo | 1.2 | milliseconds | N = 64,000; escrita de 20 ns | p. 39 |
| ciclo de escrita | 20 | ns | premissa do exemplo | p. 39 |
| tempo de lookup | 20 | ns | "lookup engine" do exemplo | p. 39 |
| pior caso, L-algorithm | L (= 32) | memory shifts | ordem por comprimento | p. 39, Fig. 5 |
| pior caso, PLO_OPT | L/2 | memory entries/operations | ordem por comprimento | p. 37; p. 40 |
| pior caso, CAO_OPT | D/2 | memory operations | ordem por cadeia | p. 40; p. 42–43 ("less than D/2") |
| D | at most 5 | prefixos por cadeia | "large backbone forwarding tables" | p. 40 |
| prefixos > 24 bits | less than 0.1% | % | tabelas usadas | p. 44 |
| média L-algorithm (texto) | around eight | movimentos/update | média móvel | p. 44, Fig. 13 |
| média PLO_OPT (texto) | approximately four | movimentos/update | média móvel | p. 44, Fig. 14 |
| cadeias MAE-EAST de comprimento ≤ 2 | 97% | % das cadeias | Fig. 15 | p. 44 |
| comprimento de cadeia | less than six | prefixos | "all chains" (MAE-EAST) | p. 44 |
| média CAO_OPT (texto) | 1.02 to 1.06 | movimentos/update | ambas as tabelas | p. 44; p. 46 |
| Prefixes | 43344 / 35217 | prefixos | MAE-EAST / MAE-WEST | Tabela 1, p. 43 |
| Inserts | 34204 / 34114 | updates | traço de 3 h | Tabela 1, p. 43 |
| Deletes | 9140 / 1103 | updates | traço de 3 h | Tabela 1, p. 43 |
| L-algorithm máx / média / dp | 22.0 / 7.76 / 3.93 | movimentos | MAE-WEST | Tabela 2, p. 46 |
| PLO_OPT máx / média / dp | 13.0 / 3.56 / 1.93 | movimentos | MAE-WEST | Tabela 2, p. 46 |
| CAO_OPT máx / média / dp | 3.0 / 1.05 / 0.02 | movimentos | MAE-WEST | Tabela 2, p. 46 |
| L-algorithm máx / média / dp | 21.0 / 7.27 / 4.09 | movimentos | MAE-EAST | Tabela 3, p. 46 |
| PLO_OPT máx / média / dp | 12.0 / 4.1 / 2.03 | movimentos | MAE-EAST | Tabela 3, p. 46 |
| CAO_OPT máx / média / dp | 3.0 / 1.02 / 0.01 | movimentos | MAE-EAST | Tabela 3, p. 46 |
| ganho do PLO_OPT sobre o L-algorithm | factor of two | — | "over the best-known solution" | p. 44; p. 46 |

## Atualização

- **Unidade** [afirma]: "number of memory movements (memory writes or shifts)" por operação de update (p. 44). Os eixos y das Figs. 13, 14 e 16 dizem "Number of memory movements". Na introdução, a operação é "TCAM's operations (such as move/write/read)" (p. 37). Fora do exemplo ingênuo (p. 39), o artigo não converte movimentos em tempo.
- **Custo de um movimento** [afirma]: só como premissa, "one memory write operation can be performed in a 20-ns clock cycle" (p. 39). Para o CAO_OPT, o texto diz "worst-case updates in a few clock cycles" (p. 40). [inferência] Com 20 ns por escrita, o máximo observado de 3.0 movimentos daria cerca de 60 ns, mas o artigo não faz essa conta.
- **Caso médio** [afirma], conforme as Tabelas 2–3 (p. 46): L-algorithm 7.76 / 7.27; PLO_OPT 3.56 / 4.1; CAO_OPT 1.05 / 1.02 (WEST / EAST).
- **Pior caso observado** [afirma]: 22.0 / 21.0, 13.0 / 12.0 e 3.0 / 3.0 (Tabelas 2–3).
- **Pior caso teórico** [afirma]:
  - ingênuo: O(N) (p. 37; p. 39);
  - espaços vazios intercalados: O(X) no caso médio, O(N) no pior (p. 39);
  - L-algorithm: L = 32 (p. 39);
  - PLO_OPT: L/2. O PLO_OPT com folgas perto de cada P_i tem pior caso "at least L/2 and can become even higher" (p. 40–41);
  - CAO_OPT: D/2 (p. 40);
  - em classificação de pacotes, o PLO_OPT "degenerates to the naive algorithm that requires O(N)" (p. 46).
- **Otimalidade** [afirma]:
  - O PLO_OPT "can be proved to be an optimal online algorithm" (p. 41), mas a prova não aparece no artigo (não encontrado).
  - O CAO_OPT é só conjectura: "Although we haven't proved it, we conjecture..." (p. 43); "Although not proved, this algorithm seems to be optimal" (p. 37).
- **Custo em software** [afirma]: manter os campos da trie auxiliar "takes no more than O(L) time" (p. 43). O tempo de CPU do gerenciador não foi medido (não encontrado).
- **O lookup trava durante o update?**
  - [afirma] O artigo trata os updates lentos como algo que força a bufferizar pacotes: "Slow updates may cause incoming packets to be buffered while an update operation is being carried out ... head-of-line blocking" (p. 38); "a large packet buffer would be required to store incoming packets while an update is being completed" (p. 39).
  - [afirma] Os movimentos do CAO_OPT não violam a restrição de ordem (p. 42), e ele "guarantees correctness at all times" (p. 46).
  - [inferência] Isso sugere que os lookups poderiam se intercalar entre os movimentos. Mas o artigo não descreve a arbitragem lookup/update na porta da TCAM nem a atomicidade de um movimento, então se o lookup para ou não fica sem resposta explícita.
- [inferência] **Como os movimentos são contados**: o CAO_OPT tem máximo observado de 3.0, enquanto D/2 ≤ 2,5, já que todas as cadeias têm menos de seis prefixos (p. 44). A média também nunca fica abaixo de 1 (Fig. 16). Isso indica que a contagem inclui a escrita do próprio prefixo novo (+1) além dos deslocamentos. O artigo não diz isso.

## Memória e energia

- [afirma] A motivação é "full use of the TCAM", sem deixar entradas vazias de reserva, porque isso "leads to wasted space and underutilization" (p. 37; p. 39, "wastes precious CAM space").
- [afirma] As abordagens alternativas custam área ou densidade:
  - o circuito de máximo é caro "in terms of logic area and speed" (p. 37);
  - a ref. 14 consegue updates rápidos "at the cost of slower search time and lower memory density" (p. 37).
- Pegada total da TCAM versus memória da trie auxiliar fora do chip: não encontrado (não há bytes nem entradas para a trie).
- Consumo de energia: não encontrado.
- Custo monetário: não encontrado.

## Limitações

**Admitidas pelo artigo**
- A otimalidade do CAO_OPT não foi provada (p. 37; p. 43).
- A distribuição de espaços livres perto de cada P_i "depends on the distribution of updates and is therefore difficult to determine a priori" (p. 41).
- Supõe ocupação quase total da TCAM. Limites melhores para ocupação de 1/k (d/2 → d/2k) ficam como trabalho futuro, com otimalidade só "under certain assumptions, but not for the general case" (p. 46).
- Não há algoritmo ótimo para o caso médio (trabalho futuro, p. 46).
- Na classificação, o PLO_OPT degenera para O(N). O ganho do CAO_OPT depende da distribuição de cadeias na constraint tree e não foi medido por falta de "large publicly available classifiers" (p. 46).

**Inferidas**
- [inferência] A métrica é só a contagem de movimentos. Não há tempo de relógio, latência de update fim a fim nem custo de CPU da trie. Também não se mede impacto no lookup (vazão ou perda durante o update).
- [inferência] O pior caso do CAO_OPT, D/2, depende dos dados. Uma FIB adversária com cadeias de comprimento perto de L o leva de volta para a ordem de L/2, igual ao PLO_OPT. A vantagem vem da distribuição empírica de cadeias (Fig. 15, p. 45), não de uma garantia independente da tabela.
- [inferência] **Escala**: TCAMs de 16K–64K entradas (p. 37) e tabelas de 35–43K prefixos (Tabela 1). Os outros artigos do corpus usam tabelas uma ordem de grandeza maiores, por exemplo 417.000 prefixos IPv4 no zec12 (resumo) e "BGP full routes is beyond 500K" no asai15 (§1). Ninguém verificou se D continua ≤ 5 e se a média continua perto de 1 nessa escala.
- [inferência] **IPv6**: só aparece na definição de L = 128 (p. 37). Pela fórmula, o pior caso do PLO_OPT iria para L/2 = 64, mas não há avaliação em IPv6.
- [inferência] Os traços cobrem só 3 h. Pela Tabela 1, isso dá cerca de 43344/10800 ≈ 4 e 35217/10800 ≈ 3,3 updates/s, bem abaixo da faixa de 100–1,000/s citada na p. 38. O cenário de rajada que motiva o artigo não foi exercitado.
- [inferência] **Possível inconsistência na Tabela 1**: em ambas as colunas, "Prefixes" é exatamente Inserts + Deletes (34204 + 9140 = 43344; 34114 + 1103 = 35217). O eixo x das Figs. 13, 14 e 16 termina perto de 350 e 430 (×100 updates), o que bate com essas somas. Ou o tamanho da tabela coincide com o número de updates, ou a linha "Prefixes" conta outra coisa. Além disso, numa leitura aproximada da Fig. 15 (escala log), a MAE-EAST tem cerca de 12.000 + 2.600 + 450 + 80 + 6 cadeias, o que comporta bem menos de 43 mil prefixos. Vale tratar o tamanho real da MAE-EAST com cautela.
- [inferência] Pequena divergência sobre os prefixos /16 no PLO_OPT: o texto põe L..L/2 (32..16) acima do pool (p. 40), mas a legenda da Fig. 7 fala em ">16 bits acima, <16 bits abaixo" (p. 41).
- [inferência] O L-algorithm de referência foi reimplementado pelos autores a partir de material do fabricante. Não se compara com nenhum produto real nem com a ref. 14.

## Respostas às afirmações antigas (IA, 31/10)

1. **"CAO_OPT: média de 1,02–1,05 movimentos por update, máximo 3; PLO_OPT: máximo 12–13 (Tabelas 2–3)"**: **CONFIRMADO**.
   - Tabela 2 (MAE-WEST, p. 46): CAO_OPT com média 1.05 e máximo 3.0; PLO_OPT com máximo 13.0.
   - Tabela 3 (MAE-EAST, p. 46): CAO_OPT com média 1.02 e máximo 3.0; PLO_OPT com máximo 12.0.
   - Ressalva: o texto descreve a média móvel como "1.02 to 1.06" (p. 44, p. 46). A unidade é "memory movements (memory writes or shifts)" (p. 44).
2. **"Taxas de 100–1000 updates/s em roteadores"**: **CONFIRMADO**, com ressalva de unidade.
   - Está na p. 38, §Longest prefix matching using TCAMs: "These changes can occur at the rate of approximately 100 to 1,000 prefixes per second.15". A unidade é prefixos por segundo, referindo-se a mudanças na FIB.
   - Fonte: ref. 15, C. Labovitz, G. R. Malan, F. Jahanian, "Internet Routing Instability," IEEE/ACM Trans. Networking, vol. 6, no. 5, Oct. 1999, pp. 515–28 (p. 47). O ano está copiado como impresso; vale conferir na fonte original (não verificado aqui).
3. **"Tabelas de 35–43K prefixos (Tabela 1)"**: **CONFIRMADO** quanto aos tamanhos: MAE-EAST 43344 e MAE-WEST 35217 (Tabela 1, p. 43).
   - Origem: snapshots públicos dos NAPs MAE-EAST e MAE-WEST, mais traços BGP de 3 h, ambos da Merit (www.merit.edu/ipma/routing_table) (p. 43).
   - **Data dos snapshots e dos traços: NÃO ENCONTRADO** (não está impressa).
   - Veja a observação sobre Prefixes = Inserts + Deletes em Limitações.

## Ganchos com outros artigos do corpus

- **shah01 → corpus**: não cita nenhum dos outros seis artigos. São posteriores, e o ruiz01 é contemporâneo (2001). Suas refs. 2–7 são algoritmos de software também cobertos pelo ruiz01: Waldvogel [6], Srinivasan/CPE [7], Gupta/DIR-24-8 [8] e Nilsson/LC-trie [9] (ruiz01, p. 11 em diante; números de referência do ruiz01).
- **ruiz01**: não trata TCAM; não há ocorrência de "TCAM/ternary/content-addressable" no texto extraído. Usa outra fonte de Labovitz (ref. [1], "Scalability of the Internet Backbone Routing Infrastructure") com números diferentes dos do shah01: "bursts of route changes at rates exceeding several hundred prefix updates per second ... on average, route changes occur 100 times/s. Thus, update operations must be performed in 10 ms or less" (ruiz01, p. 11, IEEE Network Mar/Apr 2001). Compare com os "100 to 1,000 prefixes per second" do shah01 (p. 38, ref. 15). A ordem de grandeza é parecida, mas o teto do shah01 é maior.
- **zane03** (CoolCAMs): cita o shah01 como [9]. Em §II "TCAMs for address lookups" (p. 43 impressa): "The sorting requirement makes it difficult to update the routing table—however, recent work [9] has proposed innovative algorithms for performing TCAM updates simply and efficiently". Volta a citar em §VI "Related work" (pág. 10 do PDF). Também cita Kobayashi et al. [4] (prioridade por entrada em hardware), que é a ref. 14 do shah01. [inferência] O zane03 dá o problema do update como resolvido e passa para o problema de energia. O shah01 não mede energia.
- **yang18** (SAIL, ToN 2018): §II Related Work, parágrafo "TCAM-Based Algorithms" (pág. 3 do PDF). Diz que a TCAM "is very expensive, and difficult to update" e que "Devavrat and Pankaj proposed to reduce the movement of prefixes for fast updating [12]". O [12] é a versão **Hot Interconnects 2000** ("Fast incremental updates on Ternary-CAMs for routing lookups and packet classification"), não o artigo da IEEE Micro.
- **eath04** (Tree Bitmap): §2.3.3 "Ternary Content Address Memories (TCAMs)" critica a TCAM por custo, área de placa e energia (">200W", "$4000" para 10M entradas), sem citar o shah01 e sem falar em update. [inferência] Isso reforça que o shah01 só cobre o eixo atualização e deixa de fora os eixos custo e energia.
- **zec12** (DXR) e **asai15** (Poptrie): mencionam a TCAM só na introdução, como "power-hungry" (zec12) ou com "issues in power consumption and heat" e incompatível com NFV (asai15, §1). Nenhum dos dois cita o shah01. Eles fornecem a escala de FIB moderna (417K e >500K) usada acima para criticar a escala do shah01.
