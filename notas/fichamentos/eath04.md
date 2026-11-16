# eath04: Tree Bitmap (Eatherton, Varghese, Dittia, CCR 2004)

Arquivo: `ep2_export/997150.997160.pdf` (26 páginas). Localizadores: seção e **página impressa** (p. 97–122); página impressa = página do PDF + 96.

## Referência

- **Autores**: Will Eatherton (Cisco Systems, Inc.), George Varghese (UCSD), Zubin Dittia (Jibe Networks) (p. 97).
- **Título**: "Tree Bitmap : Hardware/Software IP Lookups with Incremental Updates" (p. 97).
- **Veículo**: ACM SIGCOMM Computer Communications Review, Volume 34, Number 2: April 2004, pp. 97–122 (rodapé de todas as páginas).
- **Ano**: 2004 (rodapé).
- **DOI**: não impresso no PDF. Não há DOI nem bloco de copyright da ACM no texto (busquei "doi", "10.1145" e "copyright"). 10.1145/997150.997160 é só o que o nome do arquivo sugere; não foi conferido.
- Observação: o próprio texto se apresenta como "the journal version of our original idea [24]" (§3, p. 107); [24] = dissertação de mestrado de Eatherton, Washington University, 1998 (p. 122).

## Problema e premissas

- [afirma] Problema: atender ao mesmo tempo (i) escala de velocidade e de tamanho de tabela, (ii) atualização rápida e (iii) caber na arquitetura de memória de um forwarding engine com baixo custo de sistema (Abstract, p. 97).
- [afirma] **Roteador**: plataforma de médio a alto porte que funciona como "swiss-army knives", sem caixas especializadas para accounting, NAT, IDS etc. (§2.1, p. 99). Motor centralizado com n processadores, m controladores de memória de uso geral e um lookup engine que é um "HW block" (§2.1, p. 99; Fig. 1, p. 100). Supõe 64k interfaces lógicas (§2.1, p. 99–100).
- [afirma] **Resultado do lookup**: uma folha por prefixo (ex.: "16 byte of associated data"), não um port id de 8–10 bits (§1, p. 98). Na referência de HW, o resultado é "a 16 Byte leaf with associative data" (§7.2, p. 119).
- [afirma] **FIB**: tabela global IPv4 com "a million or more prefixes" (§2.2, p. 101). Tabela 3 (p. 102–103): Global IPv4 4+32=36 bits/1M; IPv4 VPN por interface 52 bits/5M–10M ("1k VLAN's * 10K prefixes each = 10M"); VPN deaggregation 57 bits/1M; IPv6 unicast 1M; IPv6 multicast 260 bits/512k–1M. Se a memória fosse dedicada a tudo, o total seria "extremely large (10M-20M prefixes)", mas na prática uma instalação "may use a very small number of prefixes (<1M)" (§2.2, p. 102). O prefixo de 4 bits de "table type" vem antes da chave (p. 102).
- [afirma] **Memória**: DRAM de rede (RLDRAM2/FCRAM) em vez de SRAM. A razão de preço por bit entre SRAM e DRAM de rede chega a 36:1 (§2.3.2, p. 104). "Strictly SRAM based solutions are not explicitly considered further in this paper" (§2.3.2, p. 105). Os preços valem para "2005+ time frame" e foram "normalized to each other based on quotes given to a major networking systems vendor" (§2.3, p. 103).
- [afirma] **Hardware**: "Hardware can process complex bitmap representations of up to 256 bits in a single cycle" (§4, p. 110); bitmaps de "up to 512 bits or so" viram lógica combinacional com priority encoder (§4, p. 113).
- [afirma] **Atualização**: "Update rate requirements are high, and memory usage is too high to consider shadowing", e o custo deve ser "deterministic and modest" (§2.4 item 5, p. 106). Atualização incremental e "in-place" (mesmo local).
- [afirma] **Desempenho**: deve ser determinístico e dimensionado pelo pior caso (§2.4 itens 7–8, p. 107).
- [afirma] **Tráfego**: nenhuma premissa sobre o tráfego. O desempenho é sempre de pior caso por pacote (Tabela 5, p. 120). [inferência] Não há modelo de tráfego nem de localidade.

## Proposta

Trie multibit com dois bitmaps por nó: um interno, com os prefixos guardados no nó (2^r−1 bits), e outro externo, com os filhos (2^r bits). Os filhos ficam contíguos e são apontados por um único ponteiro. Os next hops ficam num results array separado, lido de forma preguiçosa só no fim da busca (§4, p. 111–113). Não usa leaf pushing, o que permite limitar o custo de update ao tamanho de um nó (§4, p. 110). As otimizações (initial array, end nodes, split e segmented bitmaps, CAM nodes e skip nodes) reduzem o tamanho do nó para casar com o burst da memória e dão um limite de memória de pior caso (§5, p. 114–117; §7.1, p. 118).

## Avaliação

- **Plataforma**:
  - [afirma] Implementação de referência em software: stride 4, nó de 8 bytes, tabela inicial de 8K entradas, trie 13,4,4,4,4,3 (§6, p. 117). Não há nenhum número de desempenho para ela neste artigo. As comparações ficam remetidas a [23]: "More details of early experimental comparisons with other software schemes can be found in [23]" (§6, p. 117).
  - [afirma] Implementação de referência em hardware: é um **projeto** (design) de lookup engine com 4 canais RLDRAM2 e raiz on-chip, visando "up to 25 million worst case lookups per second" (§7.2, p. 118). O texto não diz se foi fabricado ou sintetizado. Só informa que um motor "similar" levou "about 2 man years of effort" e ocupou "only a few percent of the total die size of a proprietary packet processor design" (§7.2, p. 120).
  - [inferência] O motor estaria num ASIC, porque se fala em "die size" de um packet processor proprietário, mas a palavra ASIC não aparece no §7. Para uma implementação em hardware com resultados, o artigo remete a [26] (Taylor et al., Infocom 2002) (§3, p. 107).
- **Tabelas**: Mae-East (40,902 prefixos) e Mae-West (19,229), além de "Random Generated" com 1,000,000 prefixos "of random address of length 36-bits (4-bits of fixed table type)" (Tabela 6, p. 120). O ano das tabelas não está impresso. Para a geração aleatória, o PDF não descreve a distribuição de comprimentos de prefixo (não encontrado). O §5.3 usa Mae-East com initial stride 8 e stride 4, o que dá 2971 trie nodes (p. 116).
  - [inferência] As tabelas devem ser do fim dos anos 1990: o §6 fala em "databases around 5 years ago" (p. 117) e a tese é de 1998. Ainda assim, o tamanho delas (19k–41k) fica muito abaixo dos 1M–10M que o próprio artigo põe como requisito.
- **Tráfego**: nenhum. Não há medição de taxa de lookup. A Tabela 5 (p. 120) é analítica e sai da fórmula de acessos de pior caso (§7.2, p. 119).
- **Comparação**: só qualitativa ou com números copiados da literatura. Ninguém reimplementou os concorrentes neste artigo.
  - Lulea [6]: 200 Kbytes para Mae East (§3.3, p. 108 e p. 110); "two or three" acessos por nó (§1, p. 98); "three memory accesses" (§8, p. 121).
  - Expanded tries [19]: ~500 Kbytes para Mae East e update de ~5 msec (§3, p. 107; §3.2, p. 108).
  - Stony Brook [21]: 87.7 milhões de lookups/s, só com cache hit (§3, p. 107).
  - Stanford [7], multicolumn [12], hash binário [22] e LC-trie [17]: descritos qualitativamente (§3, p. 107).
  - TCAM: cenário analítico (§2.3.3, p. 105–106).

## Números

| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| Pior caso de update | 256 + C | node copy operations | stride ≤ 8; "C is small" (C não definido) | §4, p. 110 |
| Acessos por lookup (núcleo) | 1 por trie node + "a single memory reference at the end" | acessos | busca com results array preguiçoso | §4, p. 112 |
| Acessos de pior caso (HW ref.) | ⌈(width – 12)/6⌉, depois internal bitmap e depois result | acessos | initial array de 12 bits on-chip, stride 6 | §7.2, p. 119 |
| Busca máxima com j acessos | 12+6*(j-2) | bits | HW ref. | §7.2, p. 119 |
| Tabela 5, 12 MPPS, 1 lookup/pkt | 105 / 207 / 405 | bits de chave | 200M / 400M / 800M Access/sec | Tab. 5, p. 120 |
| Tabela 5, 12 MPPS, 2 lookups/pkt | 57 / 105 / 207 | bits | idem | Tab. 5, p. 120 |
| Tabela 5, 25 MPPS, 1 lookup/pkt | 57 / 105 / 201 | bits | idem | Tab. 5, p. 120 |
| Tabela 5, 25 MPPS, 2 lookups/pkt | 33 / 57 / 105 | bits | idem | Tab. 5, p. 120 |
| Meta do HW ref. | 25 million | worst case lookups per second | 4 canais RLDRAM2 | §7.2, p. 118 |
| Taxa de acesso total | 800M | 16-byte nodes per second | 4 canais, 4 cópias por canal, 5ns por acesso | §7.2, p. 118 |
| Refresh + banda de update | <2% | da banda total ("ignored here") | HW ref. | §7.2, p. 118 |
| Strides do HW ref. | 6-bit stride, 12-bit initial stride | bits | initial array on-chip SRAM, 4k entradas de 128 bits | §7.2, p. 118–119 |
| Strides do SW ref. | 13,4,4,4,4,3 | bits | 8K entry initial table; nó de 8 bytes; bitmaps de 15 e 16 bits | §6, p. 117 |
| Nó do núcleo com stride 8 | 551 bits, arredondado para 1024 bits / 128-bytes | bits/bytes | sem otimizações | §5, p. 114 |
| Initial array (exemplo) | 256 entry, 8-bytes, 2k bytes | — | initial 8 bits + stride 4 | §5.1, p. 114 |
| Initial array com update ruim | 13 bits or higher | bits | — | §5.1, p. 114 |
| Nós sem prefixo interno | 50% of the 2971 trie nodes | — | Mae-East, initial 8 + stride 4 | §5.3, p. 116 |
| CAM nodes | "over half of the next hop pointers" saem dos results arrays | — | CAM node de 1 entrada | §5.5, p. 117 |
| Limite de nós (pior caso) | 2n | nós | com skip nodes; sem contar results arrays | §7.1, p. 118 |
| Limite de memória (pior caso) | 16-bytes per prefix | B/prefixo | nós de 8 bytes | §7.1, p. 118 |
| Mae-East | 40,902 / 28216 / 452 / 11 | prefixos / nós / Kbytes / B por prefixo | HW ref.; sem folha | Tab. 6, p. 120 |
| Mae-West | 19,229 / 15429 / 247 / 13 | idem | idem | Tab. 6, p. 120 |
| Random Generated | 1,000,000 / 1,450,000 / 23,200 / 23 | idem | chave de 36 bits | Tab. 6, p. 120 |
| DRAM física por prefixo | 128 Bytes | B/prefixo | (~16B estrutura + 16B folha) × 4 réplicas | §7.2, p. 120 |
| 10M prefixos | 1.6GB | DRAM | com replicação 4× | §7.2, p. 120 |
| 10M prefixos sem replicação | 400MB; "at least 7" componentes de 576Mbit | DRAM | — | §7.2, p. 120 |
| Esforço de projeto | about 2 man years | pessoa-ano | 1 de design + 1 de verificação | §7.2, p. 120 |
| TCAM disponível | 18Mbit (256k by 72-bit entries) | — | .13um | §2.3.3, p. 105–106 |
| Cenário TCAM | 10 Million entries of 52-bits, 20 TCAM components | — | TCAM de 18Mbit | §2.3.3, p. 106 |
| Custo do cenário TCAM | "could easily exceed $4000" | US$ | idem | §2.3.3, p. 106 |
| Potência do cenário TCAM | ">200W" | W | "if techniques are not employed to limit the components and banks of CAMs that are searched" | §2.3.3, p. 106 |
| SRAM on-chip | 1.5sqmm per 1Mbit; 300-400 Mhz; ~50Mbits por ASIC | — | 90nm | §2.3.1, p. 103 |
| Custo SRAM on-chip × DRAM | ~25x (DRAM de rede); 50x+ (DRAM commodity) | por bit | — | §2.3.1, p. 104 |
| Custo SRAM × DRAM de rede | 36:1 | por bit | mesma banda total | §2.3.2, p. 104 |
| DRAM 4× replicada × SRAM | DRAM ~9x cheaper | por bit | RLDRAM2, tRC 20ns | §2.3.2, p. 105 |
| Custo normalizado por bit (Tab. 4) | SRAM 72-108; DDR2 SDRAM 1; RLDRAM2 2-3 | relativo | — | Tab. 4, p. 105 |
| Update do expanded trie [19] | around 5 msec | ms | sem contar o programa de otimização | §3, p. 107 |
| Memória do Lulea [6] | 200 Kbytes | KB | "current Mae East database" | §3.3, p. 108 |
| Memória do expanded trie [19] | around 500 Kbytes | KB | Mae East, melhor caso | §3.2, p. 108 |
| CAMs | "less than 32000 prefixes" | prefixos | enterprise/access | §3, p. 107 |

## Atualização

- **Unidade**: "node copy operations" (§4, p. 110). Em §2.4 o requisito é dado em memória e banda de datapath (p. 106). No §7.2 aparece em fração de banda: refresh e update somam "<2%" (p. 118).
- **Pior caso**: [afirma] "update times are bounded by the size of a trie node; since we only use trie nodes of stride of no more than 8, this requires only 256 + C node copy operations in the worst case where C is small" (§4, p. 110). O limite é só afirmado: não há derivação e C não é definido.
- **Caso médio**: não encontrado.
- **Medições**: nenhuma neste artigo. Não há tempo de update, updates/s nem traço de BGP. O §6 diz apenas que testes anteriores "[23]" mostraram vantagem em "lookup speed, or insertion/deletion speed, and total size" (p. 117).
- **Updates por segundo**: não há valor numérico. O texto diz só que "Update rate requirements are high" (§2.4, p. 106) e que taxas altas importam para "fast restart/boot-up scenarios, certain IP/MPLS tunnel movement scenarios, as well as for fast routing table convergence" (§6, p. 117).
- **Contraste com Lulea**: [afirma] "in the Lulea scheme, a single update can cause almost the entire table to be rewritten" (§1, p. 98). No exemplo do §3.3, um prefixo novo na raiz tem de ser empurrado para "thousands of leaf nodes" (p. 110).
- **O que o limite 256 + C não cobre**, todos [inferência]:
  - A expansão no initial array, de 4k entradas no HW e 8K no SW, quando entra um prefixo mais curto que o initial stride. O próprio §5.1 admite "poor update times" para arrays de 13 bits ou mais (p. 114), e o SW ref. usa justamente 13 bits (p. 117).
  - O pushdown por controlled prefix expansion no segmented bitmap (§5.4, p. 116).
  - O custo do alocador de blocos de tamanho variável (§4, p. 111).
  - Com o stride 6 do HW ref., o mesmo raciocínio daria 64 + C.

## Memória e energia

- **Pegada total**: estrutura de busca de 11/13/23 B por prefixo (Tab. 6, p. 120), sem contar a folha. Para Mae-East/West a folha "is actually more bytes per prefix of storage then for the search structures" (p. 120). O resumo "marketing" dá 128 B de DRAM física por prefixo com replicação 4×: 1.6GB para 10M prefixos, ou 400MB sem replicação (§7.2, p. 120). O limite de pior caso é de 16 B/prefixo com nós de 8 bytes (§7.1, p. 118).
  - [inferência] Com os nós de 16 bytes do HW ref., o mesmo limite de 2n nós dá 32 B/prefixo.
  - [inferência] 128 B × 10M = 1.28 GB, não 1.6GB. Os 1.6GB (e os 400MB = 1.6GB/4) correspondem a 160 B/prefixo, e a diferença não é explicada. O número de 7 componentes fecha com 400MB se a sobrecarga de ECC (36/32) for contada: 3600 Mbit / 576 Mbit = 6.25.
- **On-chip**: initial array de 12 bits em SRAM on-chip, com 4k entradas de nós de 128 bits (§7.2, p. 118–119). [inferência] Isso dá 64 KB on-chip. O artigo não informa esse total em bytes.
- **Energia**: a potência do Tree Bitmap ou da DRAM não foi encontrada. Para TCAM, há ">200W" condicional (§2.3.3, p. 106) e "Power can be extremely high" (p. 106).
- **Custo**:
  - Tree Bitmap: só custos relativos por bit (Tab. 4, p. 105; §2.3.1–2.3.2, p. 104–105) e a contagem de componentes DRAM (p. 120). Custo em US$: não encontrado.
  - TCAM: "could easily exceed $4000" (p. 106).
  - Projeto: área "a few percent" do die e 2 pessoas-ano (p. 120).

## Limitações

Admitidas pelo artigo:
- [afirma] Nó de stride 8 sem otimizações tem 128 bytes e "would require several memory interfaces and so drive up the cost and pin count" (§5, p. 114).
- [afirma] Os "null nodes" desperdiçam espaço ("irritating feature"); são mitigados, não eliminados em geral (§5.2, p. 114–115).
- [afirma] O alocador "must, of course, now deal with larger and variable sized allocation chunks" (§4, p. 111).
- [afirma] Initial arrays de 13 bits ou mais "could, however, have poor update times" (§5.1, p. 114).
- [afirma] CAMs levam vantagem na garantia de capacidade em prefixos (§7.1, p. 118). Os skip nodes "do not result in much savings in practice" nas bases atuais (§7.1, p. 118).
- [afirma] Com skip nodes há "modest degradation of density" para chaves mais longas (p. 120). 1.6GB é "still more then desired"; evitar a replicação "requires more sophisticated memory management and layout" (§7.2, p. 120).
- [afirma] 10M prefixos "would seemingly not be the common case" (§7.2, p. 120).

Inferidas:
- [inferência] Update, lookup e energia não foram medidos. O limite 256 + C é uma afirmação sem prova, e a Tabela 5 é analítica.
- [inferência] **Tabela 5 × fórmula**: os 12 valores da Tabela 5 (p. 120) ficam exatamente +9 bits acima de 12+6*(j-2) (p. 119). Exemplo: 25 MPPS, 1 lookup, 200M acessos/s dá j = 8, logo 48 bits pela fórmula, contra 57 na tabela. Por isso a afirmação de que o caso VPN deaggregation (57 bits) cabe em 25% da banda (p. 119) só se sustenta pela tabela, não pela fórmula.
- [inferência] **Conta das TCAMs**: com chips de 256k × 72 bits, 10M entradas de 52 bits pedem cerca de 39 chips. O número 20 só fecha com entradas de 36 bits (512k por chip), nas quais 52 bits não cabem; é exatamente o problema de "granular sizing" que o próprio texto aponta (p. 106). O erro subestima a TCAM, então não enfraquece a conclusão contra ela, mas o número publicado não é reprodutível.
- [inferência] **Rótulo do cenário TCAM**: o texto chama 52 bits de "VPN deaggregation width from Table 3" (p. 106). Na Tabela 3, porém, 52 bits é "IPv4 VPN databases per Router interface" (5M–10M), e VPN deaggregation é 57 bits com 1M (p. 102–103).
- [inferência] **Comparação assimétrica**: para a TCAM o artigo dá US$ e W; para o Tree Bitmap dá bytes e número de chips DRAM, sem US$ nem W. Além disso, a TCAM é dimensionada para 10M entradas, um caso que o próprio artigo diz não ser o comum.
- [inferência] **Memória "comparable (and sometimes slightly better)" que a do Lulea** (§4, p. 110): não há dado neste artigo que sustente isso. A Tabela 6 dá 452 KB para Mae-East com nós de 16 B, sem folha, contra os 200 KB do Lulea (§3.3). As configurações são diferentes e a data da base não é informada.
- [inferência] **Tensão interna sobre TCAM**: o artigo descarta as ideias de economia de energia do CoolCAMs ("do not appear to be reflected in practice", §3, p. 107), mas os >200W do §2.3.3 dependem justamente de não usar técnicas de limitar os bancos pesquisados.
- [inferência] **Erros de citação e de texto**:
  - §8 cita o Lulea como "[5]", que na lista é um livro de SONET; o Lulea é [6] (p. 120–121).
  - §8 diz "thesis form ... in [23]"; na lista, a tese é [24] e [23] é Crescenzi et al. (p. 121–122).
  - §4 remete a "Section 2.2" para memória; o assunto está na 2.3 (p. 110).
  - O texto dá o bitmap externo como "00011001", e a Fig. 6 dá "00001101" (p. 111–112). O correto, pelas folhas 5, 6 e 8, é 00001101.
  - O comentário do struct diz "16-bit bitmap" para um campo de 64 bits (p. 119).
  - O §1 diz que o Lulea faz "two or three" acessos por nó (p. 98); o §8 diz "three" (p. 121).

## Ganchos com outros artigos do corpus

- **zane03 (CoolCAMs)**: citado como [27] (p. 122). Frase: "Finally, [27] presents some ideas for reducing power consumption in TCAMs but these ideas do not appear to be reflected in practice." (§3, p. 107). [inferência] Isso contradiz o próprio §2.3.3, que condiciona os >200W a não limitar os bancos pesquisados (p. 106). Também é o ponto de atrito direto com zane03.
- **shah01 (updates em TCAM)**: não citado. [inferência] O eath04 trata CAMs como referência de determinismo: os algoritmos "need to exhibit some of the determinism in update and lookup times that CAMs provide" (§3, p. 107). O custo de update em TCAM, que é o tema de shah01, não é discutido. A confrontar no fichamento de shah01.
- **ruiz01 (survey)**: não citado. Pela busca de texto no PDF do survey, ele cita a tese de Eatherton de 1999 ("Full Tree Bit Map", ref. [13]) e diz que "Leaf pushing is avoided, so incremental updates are allowed". Localizador ainda não conferido.
- **zec12 (DXR)**: posterior. A busca de texto não encontrou "Tree Bitmap" nem "Eatherton" no PDF; não cita, salvo verificação.
- **asai15 (Poptrie)**: posterior. Cita como [11] e, pela busca de texto, diz que "even in the most favourable situation Tree BitMap only achieved 1/3 of the performance of other modern algorithms". Também diz que usa popcnt "rather than the lookup table used in the original Tree BitMap implementation", o que remete ao §6 do eath04 ("byte lookup table", p. 117). Seção e página ainda não conferidas.
- **yang18 (SAIL)**: posterior. Cita como [52] ("ACM SIGCOMM Comput. Commun. Rev., vol. 34, no. 2, pp. 97–122, 2004") e compara velocidade e memória com Tree Bitmap, inclusive em FIBs sintéticas grandes. Localizador ainda não conferido.

## Conferência das afirmações antigas (IA, 31/10)

1. **"Atualização: limite analítico de 256 + C cópias de nó; nada medido neste artigo (§4)."** CONFIRMADO. §4, p. 110: "update times are bounded by the size of a trie node; since we only use trie nodes of stride of no more than 8, this requires only 256 + C node copy operations in the worst case where C is small".
   - Ressalva 1: "analítico" é generoso. O limite é afirmado sem derivação e C não é definido.
   - Ressalva 2: de fato nada é medido. O único número ligado a update é a estimativa "<2%" de banda (refresh + update, §7.2, p. 118), e a comparação experimental fica remetida a [23] (§6, p. 117).

2. **"Custo da TCAM 'extremely prohibitive'; descarta CoolCAMs como algo que não aparece na prática (§2.3.3, §3)."** CONFIRMADO, com localizador mais preciso.
   - §2.3.3, p. 106, terceiro item da lista de desvantagens: "Cost is extremely prohibitive given cost of goods (COGs) targets of routers today".
   - §3, p. 107: "Finally, [27] presents some ideas for reducing power consumption in TCAMs but these ideas do not appear to be reflected in practice." [27] = Zane, Narlikar, Basu, "CoolCAMs: Power-Efficient TCAMs for Forwarding Engines," Infocom 2003 (p. 122).
   - Ressalva 1: a menção a CoolCAMs está só no §3, não no §2.3.3.
   - Ressalva 2: o próprio §2.3.3 admite técnicas que limitam os bancos pesquisados, ao custo de interfaceamento mais complexo.
   - Ressalva 3: o §8 reconhece que "CAM technology will continue to improve as continued attention is devoted to decreasing cost and power consumption" (p. 121).

3. **"10M entradas de 52 bits (VPN), roteador 'canivete suíço'; daí 20 chips, >US$ 4000, >200 W (§2.1, §2.3.3)."** Números e localizadores CONFIRMADOS; DIVERGENTE em dois pontos.
   - "swiss-army knives" está no §2.1, p. 99.
   - §2.3.3, p. 106: "10 Million entries of 52-bits (VPN deaggregation width from Table 3). WIth 18Mbit TCAMs this would require 20 TCAM components. The cost could easily exceed $4000, the board space becomes very large, and power could easily be >200W if techniques are not employed to limit the components and banks of CAMs that are searched".
   - (a) DIVERGENTE: os >200 W são condicionais, valem só sem técnicas de limitar os bancos pesquisados.
   - (b) DIVERGENTE: o "daí" não está no texto. Os 10M vêm da Tabela 3 (p. 102: "1k VLAN's * 10K prefixes each = 10M"), não da figura do roteador "canivete suíço". O próprio artigo diz que 10M "would seemingly not be the common case" (p. 120) e que na prática se usa "<1M" (p. 102).
   - Obs. [inferência]: o rótulo "VPN deaggregation" não bate com a Tabela 3, em que 52 bits é a linha de VPN por interface. Além disso, 20 chips não fecha com entradas de 72 bits (daria cerca de 39).

4. **"O Tree Bitmap tem nós CAM (§5.5)."** CONFIRMADO. §5.5 "CAM Nodes", p. 116–117: nós com poucos prefixos internos trocam o internal bitmap e o ponteiro de resultado por "a simple CAM type entry that has match bits, match length, and next hop pointers". O HW ref. usa "CAM optimization for end nodes and internal nodes" (§7.2, p. 118).
   - Ressalva: é uma otimização opcional de codificação de nó em DRAM, não um chip CAM/TCAM. Não é correto dizer que o Tree Bitmap usa TCAM.
