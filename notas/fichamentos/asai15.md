# Fichamento: asai15 (Poptrie)

Arquivo: `ep2_export/2785956.2787474.pdf` (14 páginas).
Convenção dos localizadores: "p." é a página **impressa** no PDF (57 a 70). Página do PDF = p. impressa − 56.
Texto lido por inteiro (pdftotext). Tabela 1, Tabela 3, Figura 8 e Figura 12 conferidas na página renderizada.

## Referência

- Autores: Hirochika Asai (The University of Tokyo); Yasuhiro Ohara (NTT Communications Corporation). p. 57.
- Título: "Poptrie: A Compressed Trie with Population Count for Fast and Scalable Software IP Routing Table Lookup". p. 57.
- Veículo: SIGCOMM '15, August 17-21, 2015, London, United Kingdom. p. 57 (rodapé).
- Ano: 2015. p. 57.
- DOI: `http://dx.doi.org/10.1145/2785956.2787474`. p. 57 (rodapé).
- ISBN: 978-1-4503-3542-3/15/08. p. 57.
- Páginas no volume: 57–70 (numeração impressa).
- Código: implementação de referência em https://github.com/pixos/poptrie (nota 2, p. 63).

## Problema e premissas

- [afirma] Problema: lookup LPM em software, em CPU de uso geral (PC/COTS), rápido o bastante para 100 GbE: 148.8 Mlps para pacotes de tamanho mínimo (§1, p. 57).
- [afirma] Motivo para sair do TCAM: (1) consumo de energia e calor; (2) com NFV, o uso de TCAM pode ficar impossível, porque as funções virtualizadas rodam em software, sem TCAM (§1, p. 57). Em §2 (p. 58) somam-se custo monetário e escalabilidade, citando [4, 16]. Nenhum número de TCAM é medido ou citado.
- [afirma] GPU é descartada por herdar os problemas do TCAM (calor, energia) (§1, p. 57) e por exigir lotes grandes, o que aumenta a latência de pior caso e o jitter (§2, p. 58).
- [afirma] FIB × RIB: o Poptrie serve só para achar um índice de FIB (próximo salto). As rotas ficam numa RIB separada (radix/Patricia), o que permite comprimir agressivamente as rotas com o mesmo next hop (§3, p. 59).
- [afirma] "Route aggregation" (fundir prefixos de mesmo next hop num subárvore sem lacunas) vem ligada em todos os resultados do Poptrie, salvo indicação em contrário. Os autores dizem que ela não é contribuição deles e que vale para outras técnicas (§3, p. 59).
- [afirma] FIB: tabelas BGP com mais de 500K rotas; as tabelas reais incluem rotas de IGP, mais específicas (§1, p. 57; §4.1, p. 63). A maioria dos prefixos fica entre /11 e /24 (§3.4, p. 61). O /24 é o prefixo mais longo e também o mais numeroso no BGP (§4.3, p. 65).
- [afirma] Hardware: CPU x86-64 com instrução `popcnt`, nós de 64 bits (k = 6) para casar com os registradores (§3, p. 59; §3.2, p. 60). O desempenho depende de a estrutura caber no cache da CPU (§3, p. 59).
- [afirma] Atualização: há um único thread de update; o lookup é só leitura; a troca é feita com instrução atômica, sem lock (§3.5, p. 62). Não há premissa de taxa de updates (updates/s).
- [afirma] Tráfego: avaliado com padrões sintéticos (random, sequential, repeated) e com um trace real (§4.2, p. 64). Sobre localidade, só a observação de que o SAIL depende dela (§2, p. 59; §4.5, p. 66).
- [afirma] A distribuição de pacotes entre vários núcleos fica fora do escopo (§4.4, p. 65).

## Proposta

O Poptrie é uma trie multiway de 64 vias (k = 6). Cada nó interno guarda um `vector` de 64 bits (bit 1 = filho interno, bit 0 = folha) e duas bases (`base1` para nós internos, `base0` para folhas). O índice do filho sai de um `popcnt` sobre o vetor, o que permite omitir os filhos inexistentes e guardar os descendentes em arrays contíguos (§3.1–3.2, p. 59–60). O `leafvec` comprime folhas contíguas iguais e trata o "hole punching" (§3.3, p. 60–61). O "direct pointing" acrescenta uma tabela de topo indexada pelos s bits mais significativos, como no DIR-24-8, no DXR e no SAIL (§3.4, p. 61–62). A atualização incremental reconstrói só a subárvore afetada e troca um ponteiro ou base de forma atômica, sem bloquear o lookup (§3.5, p. 62).
Tamanho do nó: 16 bytes no básico, 24 bytes com leafvec (§3, p. 59). Folha de 16 bits (§5, p. 69).

## Avaliação

- **Plataforma** [afirma] (§4, p. 63): Intel Core i7 4770K, "3.9 GHz, 8 MiB cache", 32 GB DDR3-1866, Ubuntu 14.04 x86_64. L1/L2/L3 de 32 KiB / 256 KiB / 8MiB, com latências de 4-5 / 12 / 36 ciclos; DRAM = 36 ciclos + CAS. Cada avaliação roda dez vezes (exceto §4.6). Os ciclos por lookup (§4.6, p. 66) foram medidos num SO monotarefa dos próprios autores, por PMC, com 2^24 lookups aleatórios e a mesma semente; o overhead de 83 ciclos da leitura do PMC é descontado. Segunda CPU: Xeon X3430 2.40 GHz, 8 MiB cache (§5, p. 69).
- **Tabelas** [afirma] (Tabela 1, p. 63; §4.1, p. 63):
  - 32 RIBs do RouteViews (linx, nwax, paixisc, saopaulo, singapore, sydney, telxatl), snapshots de 2014-12-16/17. Ficaram as que têm ≥ 500K rotas e mais de um next hop. Tamanhos de 508,700 a 532,637 prefixos; de 42 a 530 next hops.
  - 3 tabelas reais: REAL-Tier1-A (531,489 prefixos, 13 nhops; roteador core de backbone de um ISP tier-1 global), REAL-Tier1-B (524,170, 9 nhops; roteador de backbone nacional do mesmo ISP) e REAL-RENET (516,100, 32 nhops; roteador da rede acadêmica do WIDE Project).
  - 4 sintéticas: SYN1-Tier1-A/B (764,847 / 756,406) e SYN2-Tier1-A/B (885,645 / 876,944), feitas dividindo os prefixos ≤ /24, /20 e /16 das REAL-Tier1 e dando um next hop distinto a cada pedaço.
  - IPv6: 1 tabela do mesmo roteador da REAL-Tier1-A, com 20,440 prefixos, mais 13 RIBs públicas do RouteViews de 2014-12-25 (§4.10, p. 69).
- **Tráfego** [afirma] (§4.2, p. 64):
  - random: 2^32 endereços gerados por xorshift logo antes de cada lookup, para não poluir o cache. Overhead medido de 1.22 ns por geração, **não descontado**.
  - sequential: os 2^32 endereços em ordem.
  - repeated: cada endereço aleatório repetido 16 vezes (16 × 2^32).
  - real-trace: trace MAWI [2] de 16/12/2014, 15 minutos, capturado num link de trânsito do mesmo roteador de borda de AS que gerou a REAL-RENET. Exclui um IP que varre o IPv4 inteiro (24.4% dos pacotes IPv4). Sobram 97,126,495 pacotes e 644,790 destinos distintos, pré-carregados num array e consultados em sequência.
  - IPv6: 2^32 endereços aleatórios dentro de 2000::/8, com quatro xorshift de 32 bits por endereço (§4.10, p. 69).
- **Concorrentes e quem implementou** [afirma]: árvore radix binária, Tree BitMap [11], DXR (D16R e D18R) [38] e SAIL (SAIL_L) [36]. "We implemented these algorithms ourselves". A correção foi validada comparando os resultados de todos os algoritmos para todo o espaço IPv4 (§4, p. 63). Ajustes:
  - Tree BitMap usa `popcnt` no lugar da tabela de lookup original (§4, p. 63). Há também a variante 64-ary, contra os 16-ary originais (§4.5, p. 65; Tabela 3).
  - O DXR foi modificado (†) para as SYN: o índice de faixas foi estendido para 2^20, absorvendo o bit do formato "short" (§4.8, p. 68; Tabela 5). Para IPv6, o formato "short" foi desligado e o tamanho ganhou 1 bit, até 2^13 entradas por chunk (§4.10, p. 69).
  - Do SAIL, só a variante SAIL_L; nenhum outro parâmetro é informado. O SAIL fica fora do IPv6 porque não suporta rotas mais específicas que /64 (§4.10, p. 69).
  - Para o Poptrie, s = 16 e s = 18 foram escolhidos "para uma comparação justa", já que SAIL e DXR expandem nesses comprimentos (§4.3, p. 65).

## Números

| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| taxa de linha 100 GbE (pacote mínimo) | 148.8 | Mlps | referência | §1, p. 57 |
| pico de lookup do Poptrie | between 174 and over 240 | Mlps | 1 núcleo, "tables with 500–800k routes" | Resumo, p. 57 |
| ganho sobre todos os concorrentes | 4–578% | % | todos os testes | Resumo, p. 57 |
| Poptrie18 lookup | 240.52 (5.47) | Mlps | random, REAL-Tier1-A | Tabela 2, p. 64; Tabela 3, p. 65 |
| Poptrie18 lookup | 218.97 | Mlps | random, REAL-Tier1-B | Tabela 3, p. 65 |
| Poptrie16 lookup | 198.28 / 191.83 | Mlps | random, REAL-Tier1-A / B | Tabela 3, p. 65 |
| Poptrie0 lookup | 96.27 / 92.99 | Mlps | random, A / B | Tabela 3, p. 65 |
| SAIL lookup | 158.22 / 159.39 | Mlps | random, A / B | Tabela 3, p. 65 |
| D18R lookup | 179.92 / 168.80 | Mlps | random, A / B | Tabela 3, p. 65 |
| D16R lookup | 116.63 / 114.30 | Mlps | random, A / B | Tabela 3, p. 65 |
| Tree BitMap lookup | 56.24 / 62.13 | Mlps | random, A / B | Tabela 3, p. 65 |
| Tree BitMap (64-ary) lookup | 61.61 / 68.82 | Mlps | random, A / B | Tabela 3, p. 65 |
| Radix lookup | 8.82 / 8.92 | Mlps | random, A / B | Tabela 3, p. 65 |
| memória Poptrie18 | 2.40 / 2.25 | MiB | A / B | Tabela 3, p. 65 |
| memória Poptrie16 | 2.75 / 1.87 | MiB | A / B | Tabela 3, p. 65 |
| memória Poptrie0 | 1.49 / 1.32 | MiB | A / B | Tabela 3, p. 65 |
| memória SAIL | 44.24 / 42.62 | MiB | A / B | Tabela 3, p. 65 |
| memória D18R / D16R | 1.91 / 1.16 (A); 1.71 / 0.93 (B) | MiB | | Tabela 3, p. 65 |
| memória Tree BitMap / 64-ary | 2.62 / 3.10 (A); 2.54 / 2.89 (B) | MiB | | Tabela 3, p. 65 |
| memória Radix | 30.48 / 29.34 | MiB | A / B | Tabela 3, p. 65 |
| Poptrie (s=18) nós internos / folhas | 40,760 / 245,034 | nós | REAL-Tier1-A | Tabela 2, p. 64 |
| Poptrie basic s=0 (sem aggregation) | 8.67 | MiB | REAL-Tier1-A | Tabela 2, p. 64 |
| redução de memória pelo leafvec | 69–79% | % | s = 0, 16, 18 | §4.3, p. 64 |
| redução com leafvec + route aggregation | 74–88% | % | contra Poptrie (basic) | §4.3, p. 64–65 |
| folhas eliminadas pelo leafvec | more than 90% | % | | §3.3, p. 60 |
| compilação Poptrie s=0/16/18 | 32.84 (0.29) / 65.91 (0.35) / 33.24 (0.24) | ms | REAL-Tier1-A | Tabela 2, p. 64 |
| speedup Poptrie18 vs Radix, Tree BitMap, SAIL, D18R | 24.5–46.1, 3.52–6.78, 1.37–2.62, 1.04–1.34 | × | random, 35 tabelas | §4.5, p. 65 |
| speedup Poptrie18 vs SAIL | 1.52 / 1.37 | × | random, A / B | §4.5, p. 65 |
| speedup Poptrie18 vs D18R | 1.34 / 1.30 | × | random, A / B | §4.5, p. 65 |
| sequential: SAIL, D16R, D18R, Poptrie16, Poptrie18 | 1264, 628, 911, 955, 1122 | Mlps | REAL-Tier1-B | §4.5, p. 66 |
| repeated: SAIL, D16R, D18R, Poptrie16, Poptrie18 | 492, 382, 454, 470, 480 | Mlps | REAL-Tier1-B | §4.5, p. 66 |
| agregado multinúcleo | 914 | Mlps | 4 núcleos, random | §1, p. 58; §6, p. 69; Fig. 8, p. 65 |
| overhead do xorshift | 1.22 | ns/geração | incluído nas taxas random | §4.2, p. 64 |
| ciclos/lookup Poptrie18 (mean, p50, p75, p95, p99) | 53.59, 46, 48, 150, 169 | ciclos | random, A | Tabela 4, p. 67 |
| ciclos/lookup SAIL (idem) | 57.43, 22, 76, 279, 299 | ciclos | random, A | Tabela 4, p. 67 |
| ciclos/lookup D18R (idem) | 54.84, 46, 48, 154, 207 | ciclos | random, A | Tabela 4, p. 67 |
| ciclos/lookup Poptrie16 / D16R (idem) | 54.58, 43, 48, 150, 192 / 60.92, 44, 49, 189, 255 | ciclos | random, A | Tabela 4, p. 67 |
| ciclos/lookup Poptrie18 / SAIL / D18R | 55.82, 46, 48, 150, 166 / 56.34, 22, 75, 279, 290 / 56.88, 47, 49, 154, 187 | ciclos | random, B | Tabela 4, p. 67 |
| SAIL acima do Poptrie18 no p99 | 124 (74.7%) | ciclos | REAL-Tier1-B | §4.6, p. 67 |
| D18R acima do Poptrie18 no p99 | 21 (12.7%) | ciclos | REAL-Tier1-B | §4.6, p. 67 |
| p95 do Poptrie18 em qualquer profundidade | no more than 172 | ciclos | REAL-Tier1-A; SAIL e DXR "exceed 234" nas profundidades 24 e 25 | §4.6, p. 67; Fig. 11 |
| real-trace: Poptrie18 vs Tree BitMap, D18R, SAIL | 3.02, 1.61, 1.22 | × | REAL-RENET | §4.7, p. 68; Fig. 12 |
| pacotes com profundidade > 18 | 32.5% (trace) vs 22.1% (espaço IPv4) | % | REAL-RENET | §4.7, p. 68 |
| pacotes com profundidade > 24 | 21.8% (trace) vs 1.66% (espaço IPv4) | % | REAL-RENET | §4.7, p. 68 |
| SYN: SAIL | 102.86, 99.98, N/A, N/A | Mlps | SYN1-A, SYN1-B, SYN2-A, SYN2-B; random | Tabela 5, p. 68 |
| SYN: D18R† (modificado) | 115.45, 117.48, 102.59, 104.22 | Mlps | idem | Tabela 5, p. 68 |
| SYN: Poptrie18 | 188.02, 187.69, 174.42, 175.04 | Mlps | idem | Tabela 5, p. 68 |
| updates usados | 23,446 (18,141 announced, 5,305 withdrawn) em 7,824 mensagens | updates | RV-linx-p52, 1 h | §4.9, p. 68 |
| substituições por update: top-level, folha, nó interno | 0.041, 6.05 (12.1 bytes), 0.48 (11.52 bytes) | objetos | média | §4.9, p. 68 |
| tempo total dos updates | 58.90 | ms | 23,446 updates, Poptrie18 | §4.9, p. 69 |
| tempo por update | 2.51 | µs | média | §4.9, p. 69 |
| inserção da tabela cheia em ordem aleatória | 2.71 / 2.40 | s | REAL-Tier1-A / B | §4.9, p. 69 |
| inserção por prefixo | 5.10 / 4.57 | µs | REAL-Tier1-A / B | §4.9, p. 69 |
| IPv6 Poptrie s=0/16/18: memória | 414 / 709 / 1437 | KiB | 20,440 prefixos | Tabela 6, p. 69 |
| IPv6 Poptrie s=0/16/18: taxa | 138.51 (0.08) / 209.84 (0.12) / 211.32 (0.09) | Mlps | random em 2000::/8 | Tabela 6, p. 69 |
| IPv6 D16R / D18R | 163.07 / 169.91 | Mlps | random | §4.10, p. 69 |
| IPv6 Poptrie18 vs D18R | 1.24 | × | random | §4.10, p. 69 |
| IPv6, pior média em 13 RIBs do RouteViews: Poptrie16 / Poptrie18 | 209.98 / 211.32 | Mlps | random | §4.10, p. 69 |
| Xeon X3430: Poptrie18 vs D18R / SAIL | 1.27 / 1.17 | × | random, REAL-Tier1-A | §5, p. 69 |
| capacidade projetada | a hundred million (IPv4) / 7 million (IPv6) | rotas | estimativa sem detalhes | §5, p. 69 |
| DXR original (citado) | 100 | Mlps por núcleo | número do trabalho [38] | §2, p. 58 |
| Rétvári et al. (citado) | 194 ciclos; 12.8 | ciclos; Mlps | IPv4 | §2, p. 58 |

[afirma] A Figura 12 (p. 68) não traz rótulos numéricos. [inferência] Lendo as barras, o Poptrie18 fica perto de 255–260 Mlps e o SAIL perto de 210 Mlps no real-trace; é leitura aproximada e não pode ser citada como número do artigo.

## Atualização

- **Unidades** [afirma]: tempo (ms no total, µs por update ou por prefixo inserido) e número de objetos substituídos por update, com bytes entre parênteses (§4.9, p. 68–69). Não há contagem de acessos à memória nem de movimentos de entrada.
- **Origem da sequência** [afirma]: quatro arquivos de update de 15 minutos (1 h no total) do RouteViews, peer RV-linx-p52. São 23,446 updates (18,141 anúncios, 5,305 retiradas) em 7,824 mensagens (§4.9, p. 68).
- **O que é medido** [afirma]: o update vai primeiro para a árvore radix (RIB) e depois uma parte da trie do Poptrie18 é substituída (§4.9, p. 68). O tempo medido é "the time to complete the update": 58.90 ms para os 23,446 updates, isto é, 2.51 µs por update (p. 69). [inferência] O texto não deixa explícito se esses 58.90 ms incluem a atualização da radix. A leitura mais natural é que sim, porque o procedimento descrito começa pela radix. Também não diz se os updates foram aplicados um atrás do outro ou no ritmo original; 58.90 ms para uma hora de updates indica aplicação em sequência, sem pausa.
- **Caso médio** [afirma]: 2.51 µs por update. Por update, substituem-se em média 0.041 do array de topo, 6.05 folhas (12.1 bytes) e 0.48 nós internos (11.52 bytes) (§4.9, p. 68–69). A inserção da tabela cheia em ordem aleatória custa 5.10 µs (A) e 4.57 µs (B) por prefixo (p. 69). Recompilar do zero leva menos de 70 ms (§3.5, p. 62); com s=18, 33.24 ms (Tabela 2, p. 64).
- **Pior caso**: não medido. [afirma] Pela estrutura: se o nó marcado mais alto estiver a uma profundidade menor que s, **o array de topo inteiro, com 2^s entradas, é substituído** (§3.5, p. 62). Esse array tem até 4×2^s bytes (§3.4, p. 62). [inferência] Com s = 18 são 1 MiB copiados nesse caso. Se "0.041" quer dizer substituições do array inteiro, cerca de 4% dos updates pagariam essa cópia, e a média de 2.51 µs esconde essa cauda. O texto não traz distribuição nem máximo.
- [afirma] O update é lock-free com um único escritor. A memória antiga só é liberada "after ensuring no lookup procedure is referring to it", sem explicar como (§3.5, p. 62). O alocador buddy reduz a fragmentação (§3, p. 59; §3.5, p. 62).
- [inferência] Ninguém mediu a taxa de lookup durante rajadas de update, nem o impacto da cópia no cache.

## Memória e energia

- **Pegada total** [afirma]: a FIB do Poptrie18 tem 2.40 MiB (REAL-Tier1-A) e 2.25 MiB (REAL-Tier1-B) (Tabela 3, p. 65). O Poptrie16 tem 2.75 / 1.87 MiB. A tabela IPv6 ocupa de 414 a 1437 KiB (Tabela 6, p. 69). O artigo não traz a pegada nas 32 tabelas do RouteViews nem nas SYN.
- **On-chip** [afirma]: aqui "on-chip" é o cache da CPU. O argumento central é que Poptrie e DXR cabem no L3 de 8 MiB e o SAIL (44.24 MiB) não; daí cache miss e DRAM (§4.5, p. 65; §4.6, p. 67). O primeiro nível do Poptrie18 e do D18R ocupa 1 MiB (4×2^18), acima do L2; o do Poptrie16 e do D16R ocupa 256 KiB, dentro do L2; o topo do SAIL tem 128 KiB (§4.6, p. 67).
- [inferência] A pegada informada é só da FIB. A RIB em radix, necessária para os updates (§3, p. 59; §3.5, p. 62), fica fora da conta. Como lookup, a radix ocupa 30.48 MiB (Tabela 3), o que dá a ordem de grandeza do custo escondido. Para comparar com TCAM, onde a tabela fica no próprio dispositivo, isso tem que entrar.
- **Energia / custo**: não encontrado. O artigo usa energia e calor do TCAM como motivação (§1, p. 57; §2, p. 58), mas não mede o consumo de nenhuma solução nem dá custo em dinheiro.

## Limitações

Admitidas pelo artigo:
- [afirma] A folha tem 16 bits, então o número de entradas de FIB fica limitado a 2^16. Dá para estender, ao custo de mais memória (§5, p. 69).
- [afirma] A capacidade projetada (100 milhões de rotas IPv4, 7 milhões IPv6) é estimativa cujos detalhes ficaram de fora por falta de espaço (§5, p. 69).
- [afirma] Com tráfego sequential e repeated, o SAIL é mais rápido, porque o Poptrie precisa de instruções de bit e o SAIL acessa um array contíguo (§4.5, p. 66).
- [afirma] O DXR ganha em algumas profundidades (mediana na profundidade 21) (§4.6, p. 68).
- [afirma] No real-trace, Poptrie e DXR caem em relação ao random por causa das rotas de IGP mais específicas (§4.7, p. 68). O mesmo trace é aplicado a todas as RIBs, embora "should be a different pattern from the real traffic on the other RIB datasets" (§4.7, p. 68).
- [afirma] A avaliação IPv6 é "less interesting" porque só há 20,440 prefixos, e o overhead dos quatro xorshift é "non-negligible" (§4.10, p. 69).
- [afirma] O escalonamento de pacotes entre núcleos fica fora do escopo (§4.4, p. 65). O update supõe um único thread (§3.5, p. 62).

Inferidas:
- [inferência] Todos os concorrentes foram reimplementados pelos autores, sem código original e sem tuning documentado. Do SAIL só há a variante SAIL_L, sem parâmetros. O artigo não diz se a route aggregation, ligada por padrão no Poptrie (§3, p. 59), também foi aplicada aos concorrentes.
- [inferência] O overhead do xorshift (1.22 ns), mantido na medida, comprime as razões a favor do Poptrie. Por exemplo, 240.52 Mlps são 4.16 ns por lookup, dos quais ~29% são o gerador. Descontado, a razão Poptrie18/SAIL na REAL-Tier1-A sobe de 1.52 para ~1.74. É conta minha; o artigo não a faz.
- [inferência] O benchmark é um laço de lookup puro num núcleo, sem E/S de pacotes. Num roteador real o L3 é dividido com buffers e outras tarefas, o que pode tirar do Poptrie a vantagem de "caber no cache".
- [inferência] As tabelas reais têm poucos next hops (9, 13, 32; Tabela 1), o que favorece a compressão de folhas. As sintéticas mais difíceis (SYN2) foram construídas de um jeito que estoura justamente o campo de 15 bits do SAIL.
- [inferência] O update só tem média de uma hora de um único peer; não há pior caso, distribuição nem rajada.
- [inferência] Nada sobre energia, apesar de a motivação ser energia do TCAM.

## Ganchos com outros artigos do corpus

Lista de referências conferida (p. 70).
- **ruiz01** (Ruiz-Sánchez et al., survey): não citado.
- **shah01** (Shah & Gupta, update em TCAM): não citado. [inferência] O artigo não discute o custo de update no TCAM; não há contraponto de update entre TCAM e Poptrie.
- **zane03** (CoolCAMs): citado como [37] só como exemplo de que TCAM é comum (§2, p. 58). [inferência] O artigo usa o consumo do TCAM como argumento, mas não discute as técnicas do CoolCAMs para reduzir esse consumo, que é o assunto do próprio artigo citado.
- **eath04** (Tree Bitmap, CCR 2004): citado como [11]. Foi reimplementado com `popcnt` e numa variante 64-ary (§4, p. 63; §4.5, p. 65). Busca dentro do nó em O(k), contra O(1) no Poptrie (§4.5, p. 66). Chega a 1/3 do desempenho dos outros "even in the most favourable situation" (§2, p. 58). [inferência] O Tree Bitmap foi pensado também para hardware ("Hardware/Software ... with Incremental Updates"), e só o software foi comparado.
- **zec12** (DXR): citado como [38]. Aparece como D16R/D18R reimplementados e depois modificados para SYN e IPv6 (§4.8, p. 68; §4.10, p. 69). O artigo atribui o gargalo à busca binária para prefixos longos (§2, p. 59; §4.6, p. 67) e reconhece um limite estrutural de 2^19 faixas (§4.8, p. 68). Cita o número do próprio DXR, 100 Mlps por núcleo (§2, p. 58).
- **yang18** (SAIL, ToN 2018): o Poptrie cita o SAIL do SIGCOMM 2014 [36], não a versão de 2018, que é posterior. O artigo afirma três coisas sobre o SAIL: passa do cache e depende de localidade (§2, p. 59; §4.5, p. 65–66); falha em SYN2 porque C16[i] não cabe nos 15 bits de BCN[i] (§4.8, p. 68); não suporta prefixos IPv6 mais longos que /64 (§4.10, p. 69). Isso contradiz o título "Guarantee IP Lookup Performance with FIB Explosion". [inferência] Vale conferir no yang18 se os 15 bits e o limite de /64 foram corrigidos e se lá o Poptrie é medido com outra implementação ou outros números.

## Conferência das afirmações antigas (IA, 31/10)

1. **CONFIRMADO.** "Poptrie18 is ... 1.37–2.62 ... times faster than ... SAIL", random, 35 tabelas (§4.5, p. 65). A legenda da Fig. 9 (p. 66) diz "RouteViews' tables", mas o gráfico e o texto incluem as 3 REAL.
2. **CONFIRMADO.** 1.22× sobre o SAIL no real-trace, **na REAL-RENET** (§4.7, p. 68; Fig. 12). Nas demais RIBs o artigo só diz que o Poptrie18 "outperforms", sem número.
3. **CONFIRMADO.** "We implemented these algorithms ourselves" (§4, p. 63), com validação contra todo o IPv4. Configurações:
   - Radix binária.
   - Tree BitMap com `popcnt` em vez de tabela, mais a variante 64-ary (§4, p. 63; §4.5, p. 65).
   - DXR em D16R e D18R. Para as SYN, modificado para 2^20 faixas (§4.8, p. 68). Para IPv6, sem o formato "short" e até 2^13 entradas por chunk (§4.10, p. 69).
   - SAIL só na variante SAIL_L, sem outros parâmetros informados.
4. **CONFIRMADO.** "Intel(R) Core i7 4770K (3.9 GHz, 8 MiB cache)", L3 de "8MiB" (§4, p. 63).
5. **CONFIRMADO, com localizador corrigido.** Os 21.8% (> 24) contra 1.66% estão em §4.7, p. 68. A origem do trace está em §4.2, p. 64: MAWI [2], "transit link of the same AS border router that produced the REAL-RENET RIB dataset". A REAL-RENET vem de um roteador da rede acadêmica do WIDE Project (§4.1, p. 63).
6. **CONFIRMADO.** xorshift (§4.2, p. 64); "we did not exclude this overhead from the results", 1.22 ns por geração.
7. **CONFIRMADO, com arredondamento.** Os valores exatos são 44.24 MiB e 158.22 Mlps na **REAL-Tier1-A**, tráfego random. Na REAL-Tier1-B são 42.62 MiB e 159.39 Mlps (Tabela 3, p. 65).
8. **CONFIRMADO.** Sequential: SAIL 1264 contra Poptrie18 1122 Mlps. Repeated: 492 contra 480 Mlps. Ambos na REAL-Tier1-B (§4.5, p. 66).
9. **DIVERGENTE.** O artigo não dá limiar em número de rotas. O SAIL não compila SYN2-Tier1-A (885,645) nem SYN2-Tier1-B (**876,944**, abaixo de 880K) e compila SYN1 (764,847 e 756,406) (§4.8, p. 68; Tabela 5). A causa é estrutural: "C16[i] in SAIL is encoded in the 15 bits of BCN[i], but it exceeds 2^15". Ou seja, depende do número de chunks, não do total de rotas. O §1 (p. 58) fala em "more than 800K routes where ... SAIL does not work".
10. **CONFIRMADO.** "58.90 milliseconds for all 23,446 updates, i.e., only 2.51 microseconds per update" (§4.9, p. 69). A sequência vem de 4 arquivos de update de 15 min (1 h) do RouteViews RV-linx-p52: 18,141 anúncios e 5,305 retiradas em 7,824 mensagens (p. 68). O que se mede é o tempo para completar os updates no Poptrie18 (radix da RIB, depois substituição parcial da trie). É só média, sem pior caso.
11. **CONFIRMADO.** "DOI: http://dx.doi.org/10.1145/2785956.2787474" (p. 57).

Pedidos extras:
- **Tamanho do Poptrie por tabela** (só há números para estas):
  - REAL-Tier1-A: 1.49 / 2.75 / 2.40 MiB para s = 0/16/18 (Tabela 2, p. 64; Tabela 3).
  - REAL-Tier1-B: 1.32 / 1.87 / 2.25 MiB (Tabela 3, p. 65).
  - IPv6: 414 / 709 / 1437 KiB (Tabela 6, p. 69).
  - Para as 32 RIBs do RouteViews e as SYN: não encontrado.
- **IPv6** (§4.10, p. 69): o Poptrie é suportado. Teste numa tabela de 20,440 prefixos: Poptrie18 a 211.32 Mlps, 1.24× o D18R. O SAIL fica fora porque não suporta prefixos além de /64. O DXR foi adaptado. A projeção é de 7 milhões de rotas IPv6 (§5).
- **TCAM**: só motivação qualitativa (energia, calor, custo, escalabilidade, incompatível com NFV) (§1, p. 57; §2, p. 58). Nenhum número, nenhuma comparação experimental. Cita [23, 37 (CoolCAMs), 39] como uso comum de TCAM.
