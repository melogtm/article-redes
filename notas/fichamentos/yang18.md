# Fichamento: yang18

Fonte: `ep2_export/Sail_2_ToN_18.pdf` (16 p.; versão "accepted for inclusion in a future issue", paginação provisória 1–16).
Convenção: [afirma] = está no PDF, com localizador; [inferência] = conclusão minha.

## Referência

- Autores: Tong Yang, Gaogang Xie, Alex X. Liu, Qiaobin Fu, Yanbiao Li, Xiaoming Li, Laurent Mathy (p. 1).
- Título: "Constant IP Lookup With FIB Explosion" (p. 1).
- Veículo: IEEE/ACM Transactions on Networking (cabeçalho, p. 1). Volume, número e páginas: não impresso no PDF (cabeçalho: "accepted for inclusion in a future issue ... with the exception of pagination", p. 1).
- Ano: 2018 ("1063-6692 © 2018 IEEE", rodapé p. 1; recebido em 25/09/2017, revisado em 13/04/2018, aceito em 06/06/2018, nota de rodapé p. 1).
- DOI: 10.1109/TNET.2018.2853575 (rodapé p. 1).
- Versão preliminar: "Guarantee IP Lookup Performance with FIB Explosion", SIGCOMM 2014 [61] (nota de rodapé p. 1).

## Problema e premissas

- [afirma] FIB: mais de 700.000 entradas segundo o RIPE NCC [3]; vazão esperada da ordem de 200 Gbps (§I-A, p. 1).
- [afirma] Hardware: a memória on-chip (cache de CPU, block RAM de FPGA) é "about 10 times faster" que a DRAM off-chip [13], mas limitada ("a few MB") e mais cara; seu tamanho cresce pouco em relação à DRAM (§I-A, p. 1).
- [afirma] Requisitos: tempo de lookup constante e uso de on-chip constante à medida que a FIB cresce (§I-A, p. 1).
- [afirma] Tráfego: "on backbone routers, for almost all traffic, the longest matching prefix has a length ⩽ 24". A divisão do SAIL "is based on traffic distribution"; a divisão de Gupta et al. [18] e "Pierluigi et al." [41] "is based on prefix distribution" (99,93% dos prefixos ≤ /24) (§I-C, p. 2).
- [afirma] Escopo: "Our observation may not hold for edge routers ... The scope of this paper is on backbone routers" (§I-C, p. 2). Em roteadores de borda de AS, "there could be more traffic hitting prefixes of length > 24", e o lookup pode ficar mais lento (§VI-A, p. 8).
- [afirma] Prefixos ≥ /25: dá para plugar qualquer esquema ("TCAM ..., hash tables, and next-hop arrays"). A escolha teria "little impact" no desempenho porque a maior parte do tráfego cai em ≤ /24 (§I-D, p. 2).
- [afirma] Raiz: supõe-se que a raiz sempre tem rótulo (next hop default) (§III-B, p. 4).
- [afirma] Largura dos campos: nas FIBs reais medidas, "15 bits are enough for C16[i] and 8 bits for next hop" (§IV-B, p. 6).
- [afirma] Atualização: o router mantém a trie no plano de controle. O custo que interessa é o do plano de dados; o paper "focus[es] on the update of data structures in on-chip memory" (§III-C, p. 5). Em SAIL_L, "most FIB updates require only updates on a leaf node [60]" (§IV-B, p. 6). Não há premissa numérica de taxa de updates (updates/s): não encontrado.
- [afirma] Plataforma: SAIL é limitado se o router tiver "⩾ 4 MB on-chip memory" e "off-chip memory ... ⩾ 4 GB" (§IV-D, p. 7).
- [inferência] A premissa central (quase todo o tráfego real casa ≤ /24) não é quantificada sobre o trace real. O único número de "tráfego > /24" é para tráfego aleatório: 0.021%–0.025% (Fig. 11, §VI-C, p. 10).

## Proposta

[afirma] O SAIL divide o lookup em duas dimensões. (1) Descobrir o comprimento do prefixo casado, feito com bitmaps on-chip, e descobrir o next hop, feito com arrays off-chip. (2) Separar prefixos ≤ 24 de ≥ 25 por "pivot pushing" no nível 24 (§I-C, §III-A/B, p. 1–4). Há quatro variantes:
- SAIL_B: 25 bitmaps, 4 MB on-chip.
- SAIL_U: expansão para os níveis 6/12/18/24; 1 acesso on-chip por update.
- SAIL_L: expansão para os níveis 16/24/32; 2 acessos on-chip e no máximo 2 off-chip por lookup.
- SAIL_M: sobrepõe as tries de várias FIBs virtuais com leaf pushing.

Para IPv6 grande, o artigo propõe um híbrido: bitmaps para 0–24 e Bloom filters para 25–64, com "pivot inheriting" (§IV, §VII).

## Avaliação

- Plataformas [afirma]:
  - FPGA: Xilinx Virtex 7 XC7VX1140T, 1.880 block RAMs de 36 Kb (8.26MB on-chip). É **simulação** no Xilinx ISE 13.2 (§V-A, p. 7). Só os estágios on-chip foram medidos, porque "off-chip memory lookups are out of the FPGA chip" (§VI-B, p. 9).
  - CPU: Intel Core i7-3520M, 2 núcleos e 4 threads a 2.9 GHz, L1 64KB código + 64KB dados, L2 512KB, L3 4MB, 8GB de DRAM, frequência observada 2.82GHz (§V-B, p. 7). Usa **um núcleo** para todos os algoritmos (§VI-C, p. 10).
  - GPU: DELL T620 com Xeon E5-2630 (2.30 GHz, 6 cores) e NVIDIA Tesla C2075 (1147 MHz, 5376 MB, 448 CUDA cores), CUDA 5.0, processamento em lote (§VI-D, p. 11; §V-C, p. 7–8).
  - Many-core: Tilera TLR4-03680, 36 cores, 256K de L2 por core, CentOS 5.9 (§V-D, p. 8). Usa 35 cores de lookup (§VI-E, p. 11).
  - Implantação no roteador virtual PEARL [53] (§V-E, p. 8).
- FIBs [afirma]:
  - 12 instâncias horárias da FIB de "a tier-1 router in China", obtidas por peering BGP e dump horário com Quagga (§VI-A, p. 8). Tamanho dessas FIBs: não impresso no PDF.
  - 18 snapshots do RIPE: rrc00 em 1º de janeiro de 2008–2013 (FIB2008…FIB2013) e 12 coletores em 08/08/2013 (§VI-A, p. 8).
  - A Tab. IV ("23 IPv4 FIBs", p. 9) vai de 114069 (rrc00-2002) a 495401 (rrc00-2013) prefixos, com 0.25% a 7.55% de prefixos longos.
  - IPv6: as FIBs reais são pequenas. As grandes são sintéticas, derivadas das IPv4 pelo gerador de [51] (§VII-C, p. 13).
- Tráfego [afirma]:
  - Real: capturado numa interface do roteador tier-1 nos primeiros 10 minutos de cada hora, de 22/10/2013 08:00 a 23/10 21:00 (§VI-A, p. 8).
  - 37 traces sintéticos: 25 com "randomly chosen destinations" e 12 "prefix-based", em que cada prefixo é casado com a mesma probabilidade e a ordem segue a FIB. O código está em [4] (§VI-A, p. 8).
  - O aleatório é descrito como "randomly choosing an IP address from the 4GB space" (§VI-C, p. 10). Distribuição exata e número de pacotes por trace: não encontrado.
  - GPU: lotes de 30K, 60K e 90K endereços (§VI-D, p. 11).
- Concorrentes [afirma]: PBF [47], LC-trie [49], Tree Bitmap [52], Lulea [37], DXR na versão D18R [33] e Poptrie [7] (§VI-A, p. 9).
  - O PBF entra só no FPGA, e de forma analítica: memória = 18.755·n e ciclos estimados (§VI-B, p. 9–10).
  - Quem implementou: LC-trie, Tree Bitmap, Lulea e DXR são implementações dos próprios autores, publicadas em [4] (§VIII, p. 14; "For DXR, we implemented its fastest version – D18R", §VI-A, p. 9). Para o Poptrie, "We use their open source codes" (§VI-C, p. 11), sem referência ao repositório.
  - Configuração do Poptrie: só aparece o rótulo "PopTrie₁₈" na Tab. III (p. 8). Parâmetro s e agregação: não encontrado.
  - A correção de todos os algoritmos foi validada contra uma tabela exaustiva de 2³² entradas (§VI-A, p. 9).

## Números

| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| on-chip SAIL_B (limite) | = 4MB | MB | teórico | Tab. II, §IV-D, p. 7 |
| on-chip SAIL_U (limite) | ≈ 2.03 | MB | teórico | §IV-D, p. 7 |
| on-chip SAIL_L / SAIL_M (limite) | ≈ 2.13 | MB | (2^16 + 2^16∗16 + 2^24) bits | §IV-D, Tab. II, p. 7 |
| on-chip SAIL_M (limite) | 2^16 ∗ 17 + 2^24 = 2.13MB | MB | qualquer número/tamanho de FIBs | §IV-C, p. 7 |
| acessos on-chip por lookup | 25 / 4 / 2 / 2 | acessos | SAIL_B / U / L / M | Tab. II, p. 7 |
| acessos off-chip por lookup (pior caso) | 2 | acessos | todas as SAILs | §IV-D, p. 7 |
| redução de on-chip do SAIL_U vs SAIL_B | 49.2% | % | 4-level pushing | §IV-A, p. 5 |
| on-chip SAIL_L | 0.759MB | MB | rrc00, 476,311 prefixos (FPGA) | §VI-B, p. 9 |
| clock FPGA SAIL_B/U/L | 351MHz, 405MHz, 479MHz | MHz | Virtex 7, simulação | §VI-B, p. 9 |
| vazão FPGA SAIL_B/U/L | 351Mpps, 405Mpps, and 479Mpps | Mpps | 1 ciclo/estágio, só on-chip | §VI-B, p. 9 |
| ciclos por lookup SAIL_L | 4.08 | ciclos | derivado da Fig. 8 (CPU) | §VI-B, p. 10 |
| CPU SAIL_L, tráfego real | 673.22∼708.71 | Mpps | i7-3520M, 1 core, 12 FIBs tier-1 | §VI-C, p. 10; Fig. 8 |
| razão vs LC-trie, TB, Lulea, D18R, Poptrie (real) | 34.53∼58.88, 29.56∼31.44, 6.62∼7.66, 4.36∼5.06, 1.59∼1.72 | × | idem | §VI-C, p. 10 |
| CPU SAIL_L, prefix-based | 589.08∼624.65 | Mpps | 12 FIBs RIPE | §VI-C, p. 10; Fig. 9 |
| razão (prefix-based) | 56.58∼68.46, 26.68∼23.79, 7.61∼7.27, 4.69∼5.04, 1.23∼1.32 | × | mesma ordem; intervalos invertidos como impressos | §VI-C, p. 10 |
| CPU SAIL_L, aleatório | 231.47∼236.08 | Mpps | FIB2013, 25 traces | §VI-C, p. 10; Fig. 10 |
| razão (aleatório) | 46.22∼54.86, 6.73∼6.95, 4.24∼4.81, 2.27∼2.31, 1.13∼1.14 | × | idem | §VI-C, p. 10 |
| tráfego aleatório que casa > 24 bits | 0.021% to 0.025% | % | 25 traces aleatórios | §VI-C, p. 10; Fig. 11 |
| prefixos longos na FIB | 2.3% | % | FIB citada no texto (Tab. IV dá 2.46% para rrc00-2013) | §VI-C, p. 10; Tab. IV, p. 9 |
| SAIL_L com 1%, 5%, 10% de prefixos longos | 448∼467, 357∼380, 271∼296 | Mpps | prefixos longos gerados aleatoriamente | §VI-C, p. 11; Fig. 14 |
| Poptrie com 1%, 5%, 10% | 162∼296, 150∼234, 124∼186 | Mpps | idem | §VI-C, p. 11 |
| SAIL_L / Poptrie | 1.47 ∼ 2.83 | × | Fig. 14 | §VI-C, p. 11 |
| SAIL_M (média) | 132 / 366 | Mpps | aleatório / prefix-based, 2–12 FIBs | §VI-C, p. 10; Fig. 13 |
| acessos por update (média) | 1.854, 2.253 and 1.807 | acessos à memória | rrc00, rrc01, rrc03; 319∗500 updates | §VI-C, p. 10; Fig. 12 |
| acessos por update (pior observado) | 7.88 | acessos à memória | idem | §VI-C, p. 10 |
| GPU SAIL_L, lote 30K / 60K / 90K | 257∼322 / 405∼447 / 442∼547 | Mpps | Tesla C2075, prefix-based, 12 FIBs | §VI-D, p. 11; Fig. 15 |
| GPU latência, lote 30K / 60K / 90K | 90∼124 / 110∼152 / 122∼185 | µs | idem | §VI-D, p. 11; Fig. 16 |
| many-core | escala linear; ≈590M em 35 cores [leitura do gráfico, sem valor no texto] | pps | Tilera, rrc00, prefix-based | §VI-E, p. 11–12; Fig. 17 |
| PEARL | "around 28 times faster" | × | vs path-compressed trie, trace real | §V-E, p. 8 |
| Tab. III (média) | SAIL_L around 700Mpps; Lulea around 100Mpps; D18R around 150Mpps; PopTrie₁₈ around 430Mpps; TreeBitmap around 25Mpps; LC-trie around 16Mpps | Mpps | qualitativa | Tab. III, p. 8 |
| Tab. III (pior caso) | SAIL_L 2; PBF 25; Lulea 12; D18R 13; PopTrie₁₈ 4; TreeBitmap 6; LC-trie 9 | acessos off-chip | idem | Tab. III, p. 8 |
| IPv6 pequeno, on-chip | about 2.2MB | MB | níveis 16/24/32/40/48/64, split em 48 | §VII-A, p. 12 |
| IPv6 grande, on-chip total | 4.40 – 5.04 | MB | 13 FIBs sintéticas; 4 MB de bitmaps + BF | Tab. V, p. 13 |
| IPv6 grande, off-chip adicional | 22.8 MB to 56.9 MB, mean 49.6 MB | MB | pivot inheriting, load factor 0.1 | §VII-C, p. 14; Fig. 21 |
| IPv6 grande, off-chip total | 39.3 MB to 99.3 MB, mean 86.5 MB | MB | idem | §VII-C, p. 14 |
| Tree Bitmap em IPv6 grande | 28.7 MB to 71.1 MB, mean 61.8; "about 71.4 %" do SAIL | MB | idem | §VII-C, p. 14 |
| IPv6, buscas em hash no pior caso | 40 → 12 | buscas | 4 pivot levels (24, 34, 44, 54) | §VII-B, p. 13 |
| IPv6, probabilidade do pior caso | 0.5^{13∗(10−1)} = 2^−117 | prob. | k = 13 | §VII-C, p. 14 |

## Atualização

- Unidade [afirma]: "update speed in terms of the total number of memory accesses per update" (§VI-A, p. 9). O eixo da Fig. 12 diz "# of memory accesses per update" (p. 11), sem dizer se é on-chip ou off-chip. Tempo em µs ou ms por update: não encontrado.
- SAIL_B e SAIL_U [afirma]: 1 acesso on-chip por update (Tab. II, p. 7). No SAIL_U, um update afeta no máximo 2^6 = 64 bits, alinhados à palavra de 64 bits (§IV-A, p. 5).
- SAIL_L e SAIL_M [afirma]:
  - Pior caso "Unbounded", na coluna "# on-chip mem acc per update" da Tab. II e em §IV-D (p. 7); "the update speed in the worst case is unbounded" (§IV-E, p. 7).
  - Média medida: 1.854, 2.253 e 1.807; pior observado: 7.88 (§VI-C, p. 10; Fig. 12).
  - §IV-E (p. 7) descreve a mesma medida como "2 off-chip memory access per update (see Figure 12)", o que contradiz o rótulo on-chip da Tab. II.
- O que entra na conta [afirma]: só as estruturas do plano de dados ("FIB update performance of SAIL_L on the data plane", §VI-C, p. 10). A atualização da trie no plano de controle não é medida (§IV-B, p. 6). §III-C (p. 5) diz que o foco é a estrutura on-chip, mas fala do SAIL_B. No SAIL_L, um update também altera os arrays off-chip (N16, N24, C24, N32) (§IV-B, p. 6).
- Sobre a origem dos updates, o texto diz só "rrc00, rrc01, and rrc03 ... 319 ∗ 500 updates". Origem dos traces e taxa: não encontrado.
- Consistência durante o update [afirma]: enquanto a estrutura on-chip muda, "no lookup can be performed ... and therefore may cause packet losses". Para a estrutura off-chip, a sugestão é manter duas cópias (§III-C, p. 5).

## Memória e energia

- On-chip [afirma]: os limites estão na tabela acima. Em FPGA/ASIC, ficam on-chip BCN (ou BC16) e B24. Em CPU, GPU e many-core, B24 e N24 são combinados em BN24 por causa da cache (§IV-B, p. 6). Só a implementação FPGA teve o tamanho on-chip avaliado (§VI-A, p. 9).
- Pegada total off-chip em IPv4 (N16, N24, C24, N32): não encontrado. Há só o requisito "⩾ 4 GB" (§IV-D, p. 7). Para IPv6 sintético, ver Fig. 21.
- Energia e potência: não medidas. Sobre TCAM, o texto é apenas qualitativo: "consumes a huge amount of power ... generates a lot of heat, is very expensive, and difficult to update" (§II, p. 2–3).
- Custo: só qualitativo. On-chip "much more expensive than DRAM" (§I-A, p. 1); "off-chip memory is cheap" (§VII-C, p. 14). O artigo cita "Modern ASICs have 50∼100MB on-chip memory [35]" (§VII-C, p. 13).

## Limitações

Admitidas [afirma]:
- Em roteadores de borda, ou de borda de AS, mais tráfego > /24 deixa o lookup mais lento, mas o pior caso continua em 2 acessos off-chip (§I-C, p. 2; §VI-A, p. 8).
- O pior caso de update do SAIL_L é ilimitado (§IV-E, p. 7; Tab. II).
- O SAIL_L "currently does not support multi-core platforms" (§IV-E, p. 7).
- O chunk ID de 15 bits não basta para FIB muito grande. A correção proposta (16 bits + flag separada de 2^16 bits) é chamada de "tiny problem" (§VI-C, p. 11).
- O lookup cai com a fração de prefixos longos (Fig. 14, §VI-C, p. 11).
- Não houve comparação de vazão com o PBF em FPGA, por falta de detalhes de implementação (§VI-B, p. 9).
- Um update on-chip bloqueia o lookup e pode perder pacotes (§III-C, p. 5).
- No IPv6 híbrido, o pior caso tem 12 acessos off-chip (§VII-C, p. 14), e as FIBs IPv6 grandes são sintéticas (§VII-C, p. 13).

Inferidas:
- [inferência] O FPGA é simulado e só mede estágios on-chip. Os 479 Mpps são um teto do pipeline, não vazão ponta a ponta com DRAM.
- [inferência] Na CPU, "on-chip" é a cache: os 2.13 MB cabem na L3 de 4 MB do i7-3520M, e o trace real tem a melhor localidade (o artigo admite o efeito da localidade, §VI-C, p. 10). A vantagem sobre o Poptrie cai de 1.59–1.72× (real) para 1.13–1.14× (aleatório).
- [inferência] Quatro dos cinco concorrentes de CPU foram implementados pelos próprios autores, o mesmo viés que eles atribuem à implementação do SAIL feita pelos autores do Poptrie. A configuração do Poptrie não é descrita.
- [inferência] As maiores FIBs IPv4 testadas têm 495401 prefixos (Tab. IV), abaixo dos ">700,000" citados em §I-A. A queixa do Poptrie sobre FIBs grandes não é testada.
- [inferência] O custo de update é medido em "acessos", sem tempo e sem a reconstrução da trie de controle. A rotulagem on-chip/off-chip é contraditória (Tab. II × §IV-E).
- [inferência] Next hop de 8 bits em BCN (§IV-B, p. 6) limita a 255 next hops nesse layout.
- [inferência] Inconsistências internas que enfraquecem a reprodutibilidade:
  - "12 FIBs" listadas como rrc00, 01, 03–07, 10–15, que são 13 nomes (§VI-A, p. 8; a Fig. 9 tem 13 grupos).
  - A Tab. IV se diz de "23 IPv4 FIBs" e tem 24 linhas.
  - O tamanho do rrc00 aparece como 476,311 (§VI-B, p. 9), 455 900 (§VII-C, p. 13) e 495401 (Tab. IV, rrc00-2013).
  - As FIBs IPv6 reais aparecem como "around 14,000" (§VII-A, p. 12), "around 13K" e "around 10K" (§VII-C, p. 13).
  - O texto remete o IPv6 grande à "see Table IV" (§VII-C, p. 13), mas a Tab. IV é de IPv4.
- [inferência] Há citações erradas:
  - "Poptrie [11]": [11] é Pao et al., bit-shuffled trie.
  - "Lulea [36]": [36] é Ruiz-Sanchez et al. (§VI-C, p. 11).
  - "Lulea Lulea [37]" (§VI-A, p. 9).
  - "Pierluigi et al." (§I-C, p. 2) e "Devavrat and Pankaj" (§II, p. 3) usam prenomes no lugar do sobrenome.
  - [54]–[56], citados como evidência do crescimento da memória on-chip (§VI-C, p. 11), são artigos sobre tensores e anomalias de tráfego.
- [inferência] A Tab. III põe o Tree Bitmap na plataforma "FPGA", mas ele foi medido na CPU (§VI-C).

## Ganchos com outros artigos do corpus

- **ruiz01** (Ruiz-Sánchez, Biersack, Dabbous, IEEE Network 2001) = ref. [36]. É citado para binary trie e binary range search e como literatura geral (§II, p. 2). Aparece também, por erro, como "Lulea [36]" (§VI-C, p. 11).
- **shah01** (Shah & Gupta, "Fast updating algorithms for TCAMs") não é citado diretamente. O artigo cita a versão Hot Interconnects 2000 [12]: "Devavrat and Pankaj proposed to reduce the movement of prefixes for fast updating" (§II, p. 3). [inferência] É o mesmo trabalho em versão de conferência. O SAIL não compara custo de update com TCAM.
- **zane03** (CoolCAMs) = ref. [15]. É citado como TCAM de lookup constante cuja memória on-chip cresce com a FIB (§I-B, p. 1) e como redução de potência por ativação parcial de bancos (§II, p. 3). O SAIL não traz números de potência para contrapor.
- **eath04** (Tree Bitmap, CCR 2004) = ref. [52]. É concorrente na CPU, com implementação dos autores do SAIL em [4]: 29.56∼31.44× mais lento no tráfego real (§VI-C, p. 10). Na Tab. III aparece com "around 25Mpps", 6 acessos off-chip e plataforma "FPGA". No IPv6 grande, usa 71.4% da memória do SAIL (§VII-C, p. 14).
- **zec12** (DXR, CCR 2012) = ref. [33]. A versão D18R foi implementada pelos autores do SAIL (§VI-A, p. 9). Resultado: 4.36∼5.06× (real), 2.27∼2.31× (aleatório); Tab. III: "around 150Mpps", 13 acessos off-chip.
- **asai15** (Poptrie, SIGCOMM 2015) = ref. [7] (citado também, por erro, como [11]). É o ponto de contradição direta:
  - Os autores do SAIL dizem que o Poptrie não usou a implementação aberta do SAIL e que a deles "probably introduces some unnecessary overhead" (§VI-C, p. 11).
  - Respondem à alegação de que o SAIL "cannot compile due to its structural limitation" com a correção de 16 bits + flag, sem medição.
  - Apontam quatro "weaknesses" do Poptrie: sem limite de memória; mais lento; dependente de POPCNT, portanto inviável em Tilera e FPGA; e degradação "linear" com o número de FIBs virtuais. A última não é medida.
- **yang18** é o próprio artigo. A versão SIGCOMM 2014 é a ref. [61].

## Conferência das afirmações antigas (IA, 31/10)

1. **CONFIRMADO, com ressalva.** O 99.93% é atribuído a "Gupta et al. [18] and Pierluigi et al. [41]" e se refere à distribuição de prefixos. O texto diz "Pierluigi", mas a ref. [41] é de P. Crescenzi, L. Dardini e R. Grossi. A divisão do SAIL "is based on traffic distribution" (§I-C, p. 2). O artigo não quantifica a fração ≤ /24 no trace real.
2. **CONFIRMADO.** "may not hold for edge routers ... The scope of this paper is on backbone routers" (§I-C, p. 2). Em §VI-A (p. 8) o termo é "AS border routers": "there could be more traffic hitting prefixes of length > 24".
3. **CONFIRMADO.** 1.13∼1.14 (aleatório) e 1.59∼1.72 (real) estão em §VI-C, p. 10. A crítica ao Poptrie está em §VI-C, p. 11, mas é hedgeada: "we believe their implementation probably introduces some unnecessary overhead". Há também um terceiro número, 1.47 ∼ 2.83×, com prefixos longos sintéticos (Fig. 14, p. 11).
4. **CONFIRMADO em parte.** O SAIL e quatro concorrentes (LC-trie, Tree Bitmap, Lulea, DXR) foram implementados pelos autores (§VIII, p. 14; §VI-A, p. 9). O Poptrie usa "their open source codes" (§VI-C, p. 11). Configuração: só o rótulo "PopTrie₁₈" na Tab. III (p. 8). [inferência] Sugere s = 18. Agregação: **NÃO ENCONTRADO**.
5. **CONFIRMADO para CPU, núcleos e L3** (i7-3520M, "two cores with four threads", L3 4MB; §V-B, p. 7). "Notebook": **NÃO ENCONTRADO** (o PDF diz só "our computer"). Acréscimo: só 1 core é usado nos testes (§VI-C, p. 10).
6. **CONFIRMADO.** "a tier-1 router in China" (§VI-A, p. 8). A palavra "backbone" não qualifica esse roteador no trecho; o resumo diz "a major ISP in China". O tráfego aleatório são 25 traces "with randomly chosen destinations" (§VI-A, p. 8), "randomly choosing an IP address from the 4GB space" (§VI-C, p. 10), usados sobre a FIB2013. Distribuição e tamanho dos traces: não encontrado.
7. **CONFIRMADO, com ressalva de natureza.** 2.13MB é o limite superior de on-chip do SAIL_L e do SAIL_M, não um limite do hardware (§IV-D e Tab. II, p. 7; também §IV-C, p. 7, como 2^16∗17 + 2^24). O requisito de hardware declarado é "⩾ 4 MB on-chip" (§IV-D, p. 7).
8. **CONFIRMADO.** "For random traffic, SAIL_L achieves a lookup speed of 231.47∼236.08 Mpps" (§VI-C, p. 10; Fig. 10, FIB2013, i7-3520M, 1 core).
9. **DIVERGENTE.**
   - Os valores conferem: 1.854, 2.253, 1.807 e pior observado 7.88 (§VI-C, p. 10; Fig. 12, p. 11).
   - O PDF não diz "on-chip" na medição. A unidade é "total number of memory accesses per update" (§VI-A, p. 9), no plano de dados.
   - §IV-E (p. 7) chama a mesma média de "2 off-chip memory access per update", enquanto a Tab. II rotula a coluna como on-chip.
   - O pior caso ilimitado está na Tab. II, em §IV-D e em §IV-E (p. 7), não na Fig. 12.
   - §III-C (p. 5) diz que o foco é a estrutura on-chip, mas para o SAIL_B. No SAIL_L, os arrays off-chip também são modificados (§IV-B, p. 6), e a trie de controle não é contada.
10. **CONFIRMADO, como opção.** TCAM é um dos esquemas plugáveis para ≥ /25 ("we can use TCAM or next hop arrays", §I-D, p. 2). A implementação usa next-hop arrays (§III-B, p. 4; §IV-B, p. 6), sem TCAM.
11. **DIVERGENTE / NÃO ENCONTRADO.** O número "~880K rotas" não aparece no PDF. O texto diz que "the Poptrie paper claims that SAIL cannot compile due to its structural limitation" e chama a falha de "tiny problem" (não "small"), propondo 16 bits + 2^16 bits de flag (§VI-C, p. 11). Medição com a correção aplicada: **NÃO ENCONTRADO**. Só os limites teóricos (17 bits por entrada, §IV-C e §IV-D, p. 7) a incorporam, enquanto §IV-B (p. 6) ainda descreve BCN de 16 bits (1 + 15).
12. **CONFIRMADO.** "Digital Object Identifier 10.1109/TNET.2018.2853575" (rodapé, p. 1).
