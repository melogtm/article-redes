# zec12 — DXR (Zec, Rizzo, Mikuc, CCR 2012)

Arquivo: `ep2_export/2378956.2378961.pdf` (8 páginas). Localizadores usam a paginação impressa da CCR:
p. 29 = Public Review (pág. 1 do PDF); p. 30–36 = artigo (págs. 2–8 do PDF).
Convenção: [afirma] = está no PDF, com localizador; [inferência] = conclusão minha.

## Referência

- Autores: Marko Zec (Univ. of Zagreb), Luigi Rizzo (Università di Pisa), Miljenko Mikuc (Univ. of Zagreb) — p. 30.
- Título: "DXR: Towards a Billion Routing Lookups per Second in Software" — p. 30.
- Veículo: ACM SIGCOMM Computer Communication Review, Volume 42, Number 5, October 2012, pp. 29–36 (rodapé de cada página; p. 29 é a Public Review de Nikolaos Laoutaris, Telefonica Research).
- Ano: 2012.
- DOI: não impresso no PDF (procurei "doi" e "10.1145" no texto extraído e olhei as págs. 29 e 30 renderizadas). [inferência] O nome do arquivo segue o padrão da ACM DL (10.1145/2378956.2378961), mas isso não está impresso.

## Problema e premissas

- [afirma] Problema: LPM em software, em CPU de uso geral, competindo com hardware dedicado (Abstract, p. 30; §1, p. 30).
- FIB:
  - [afirma] Só IPv4: "optimized exclusively for the IPv4 protocol" (§3, p. 31).
  - [afirma] Tabelas BGP completas com "4-500,000 entries" (§1, p. 30), "more than 420,000 IPv4 prefixes" (§1, p. 30).
  - [afirma] A grande maioria dos prefixos é /24 ou menos específica e o número de next hops distintos é pequeno. É isso que sustenta o formato "short" de 16 bits (§3.2, p. 32).
  - [afirma] Limites de codificação: até 2^19 faixas após agregação, até 4096 entradas por chunk e next hop de 16 bits no formato "long" (§3.2, p. 32).
  - [afirma] Precisa de uma base primária separada (a árvore radix do FreeBSD) para reconstruir as estruturas (§3.4, p. 33).
- Tráfego:
  - [afirma] Não usaram traces reais, que "typically exhibit locality". RND (chaves uniformes) é apresentado como "the worst case for a high performance router working in the core of the network" (§4.1, p. 33–34).
  - [afirma] REP corresponde a roteador com poucos fluxos (§4.1, p. 34).
- Hardware:
  - [afirma] CPU multicore com caches grandes e latência de DRAM de "roughly 50 ns" (§1, p. 30).
  - [afirma] A estrutura deve caber em L2/L3 (§1, p. 30).
  - [afirma] CPUs com execução fora de ordem ganham throughput no padrão RND, que é processado em lote (§4.1, p. 34).
- Requisito de velocidade:
  - [afirma] "a single 100 GB/s Ethernet port may receive up to 144 million packets per second" (§1, p. 30). Está impresso "GB/s".
  - [afirma] O lookup deve ser "a small fraction of the packet interarrival time" (§1, p. 30).
- Taxa de atualização:
  - [afirma] "Timescales for incrementally updating lookup structures are significantly longer than for lookups" (§4.4, p. 36).
  - Nenhuma taxa de updates BGP é assumida ou citada: não encontrado.
- TCAM:
  - [afirma] Única menção: "early hardware routing lookup proposals were centered around power-hungry TCAMs or fast SRAMs, rumor has it that most router vendors are turning to reduced latency DRAM chips coupled with ASICs" (§1, p. 30). Não há número nem comparação com TCAM.
- IPv6:
  - [afirma] "Direct lookups [7], which DXR relies on before doing binary search on address ranges, are infeasible with IPv6 due to longer keys and sparsely populated address space (0.026%, vs. 60.36% for IPv4) [1]" (§3, p. 31).
  - [afirma] A ref. [16] (Song et al., IPv6 com Bloom filters) aparece só como exemplo de caching (§2, p. 31).

## Proposta

- [afirma] A tabela é projetada em faixas de endereço contíguas e sem sobreposição, e faixas vizinhas com o mesmo next hop são fundidas (§3.1, p. 31–32).
- [afirma] Os k bits iniciais (k = 16..20) indexam uma lookup table de 2^k entradas de 32 bits: 1 bit de formato, 12 de tamanho e 19 de posição (§3.2, p. 32; Fig. 1).
- [afirma] Cada entrada aponta direto para o next hop ou para um chunk da range table. No chunk, a busca é binária sobre os 32−k bits restantes, com entradas de 4 bytes ("long") ou 2 bytes ("short") (§3.2–3.3, p. 32–33).
- [afirma] Configurações DkR (D16R, D18R...) trocam memória por velocidade. O protótipo roda no kernel FreeBSD e é validado contra a radix BSD (Abstract, p. 30).

## Avaliação

- Plataforma:
  - [afirma] Máquina principal: AMD FX-8150, 3,6 GHz, 8 núcleos, 4 GB de RAM. Cada par de núcleos compartilha 2 MB de L2 (8 MB de L2 no total) e os 8 núcleos compartilham 8 MB de L3 (§4.1 "Hardware", p. 34).
  - [afirma] Segunda máquina: Intel Xeon W3530, 2,8 GHz, 4 núcleos, 256 KB de L2 por núcleo e 8 MB de L3 compartilhada (§4.1, p. 34; cabeçalho da Tab. 2: "4x256 kB L2 cache").
  - [afirma] Software: FreeBSD 8.3, amd64, gcc 4.2.2 (§4.1, p. 34).
  - [afirma] Cada teste durou 10 s (mais de 200 milhões de lookups por núcleo), com variância menor que 1%. Mudanças pequenas de código ou compilador "may lose or gain 10-20%" (§4.1, p. 34).
- Tabelas:
  - [afirma] Três snapshots IPv4 de roteadores BGP do routeviews.org: LINX (417523 prefixos, 213 next hops), U. Oregon (421059, 38) e PAIX (412568, 80), além de uma tabela "static" (4 prefixos, 2 next hops) (§4.1, p. 33; Tab. 1, p. 33).
  - [afirma] Só o LINX tem data impressa: "April 2012" (legenda da Fig. 2, p. 33).
  - [afirma] Os resultados de desempenho usam o LINX, escolhido como o caso "most challenging": mais next hops e muitos prefixos mais longos que /24 (§4.1, p. 33).
- Tráfego:
  - [afirma] Sintético: vetores de 256 milhões de chaves IPv4 pré-computadas, uniformes em todo o espaço, excluindo multicast e faixas reservadas. Cada núcleo lê uma seção independente (§4.1, p. 33).
  - [afirma] Três padrões: REP (cada chave consultada 16 vezes), RND (cada chave uma vez, sem dependência entre iterações) e SEQ (dependência de dados artificial, que serializa os lookups) (§4.1, p. 34).
- Comparações e quem implementou:
  - [afirma] "a software implementation of DIR-24-8-BASIC [7]", com o código C mostrado no texto (§4.3, p. 35; Fig. 6).
    - [inferência] O código mostrado sugere que os próprios autores escreveram a implementação; o artigo não diz quem a escreveu.
    - [afirma] A D24R (DXR com k = 24) também entra na Fig. 6.
  - [afirma] Árvore radix BSD, que é o código padrão do kernel FreeBSD, medida no Xeon com HT (tabela sem número, §4.3, p. 35).
  - [afirma] Outros esquemas (Lulea, Lampson-Varghese, LC-trie, Chiueh-Pradhan) só aparecem com números citados da literatura, em hardware de outra época (§2, p. 31). Não foram medidos na mesma máquina.
- Código:
  - [afirma] A implementação, com o código de teste, está em [2] http://www.nxlab.fer.hr/dxr/ (§4, p. 33).

## Números

Valores copiados como impressos. Salvo indicação, a tabela é LINX, workload RND e máquina AMD FX-8150.

| métrica | valor | unidade | condição | localizador |
|---|---|---|---|---|
| memória D16R | 782 | Kbytes | LINX, 417,000 prefixos, 213 next hops | Abstract, p. 30; Tab. 2, p. 34 |
| bytes por prefixo D16R | less than 2 | bytes/prefixo | idem | Abstract, p. 30 |
| throughput D16R | 490 | MLps | RND uniforme, 8 núcleos | Abstract, p. 30 |
| throughput D16R | 491 | MLps | k=16, 8 núcleos | Tab. 2, p. 34 |
| throughput de outras configs | exceed 700 / exceeds 700 | MLps | 8 núcleos, RND | Abstract e §1, p. 30 |
| throughput D18R | 718 | MLps | k=18, 8 núcleos | Tab. 2, p. 34 |
| REP | exceeding 1100 | MLps | 8 núcleos | §4.2, p. 34 |
| RND | slightly above 700 | MLps | 8 núcleos | §4.2, p. 34 |
| SEQ | approximately 400 | MLps | 8 núcleos | §4.2, p. 34 |
| single-thread | 190, 115 e 61 | MLps | REP, RND, SEQ ([inferência] D18R, porque 115 = Tab. 2 k=18) | §4.2, p. 34 |
| D16R vs D18R | 25% to 50% slower | % | — | §4.2, p. 34 |
| Tab. 2 AMD, k=16/17/18/19/20/21/23/24 — memória | 782 / 1022 / 1512 / 2495 / 4474 / 8449 / 32802 / 65560 | Kbytes | — | Tab. 2, p. 34 |
| Tab. 2 AMD, 1 núcleo | 75 / 95 / 115 / 110 / 100 / 91 / 45 / 43 | MLps | k = 16..24 (mesma ordem) | Tab. 2, p. 34 |
| Tab. 2 AMD, 8 núcleos | 491 / 603 / 718 / 709 / 643 / 499 / 160 / 150 | MLps | idem | Tab. 2, p. 34 |
| Tab. 2 AMD, build time | 89 / 135 / 210 / 314 / 448 / 630 / 1621 / 2929 | ms | idem | Tab. 2, p. 34 |
| Tab. 2 Xeon, 1 núcleo | 64 / 76 / 93 / 115 / 137 / 102 / 57 / 54 | MLps | idem | Tab. 2, p. 34 |
| Tab. 2 Xeon, 4 núcleos | 253 / 303 / 368 / 451 / 531 / 311 / 165 / 153 | MLps | idem | Tab. 2, p. 34 |
| Tab. 2 Xeon, build time | 111 / 174 / 280 / 408 / 552 / 678 / 1380 / 2667 | ms | idem | Tab. 2, p. 34 |
| Tab. 1 D16R total | 800672 / 827204 / 765752 | bytes | LINX / U. Oregon / PAIX | Tab. 1, p. 33 |
| Tab. 1 D16R build | 89.44 / 98.15 / 91.28 | ms | idem (CPU não indicada) | Tab. 1, p. 33 |
| Tab. 1 D18R total | 1548700 / 1574872 / 1522992 | bytes | idem | Tab. 1, p. 33 |
| Tab. 1 D18R build | 210.13 / 227.47 / 210.07 | ms | idem | Tab. 1, p. 33 |
| Tab. 1 static | 262248 / 0.01 (k=16); 1048676 / 0.03 (k=18) | bytes / ms | 4 prefixos | Tab. 1, p. 33 |
| Tab. 1 LINX D16R chunks | 12935 full; 200436 short; 33130 long | entradas | — | Tab. 1, p. 33 |
| match direto (n=0) | .945 / .864 / .757 | fração | D20R / D18R / D16R | Tab. 3, p. 35 |
| lookup por núcleo | between 10 and 50 | MLps | conforme o nº de passos da busca binária | §4.2, p. 35; Fig. 5 |
| interferência entre núcleos | about 15%; speedup 6.9 instead of 8 | % / x | 8 núcleos | §4.2, p. 35 |
| memória DIR-24-8 | about 32 | Mbytes | D24R "twice as big" | §4.3, p. 35 |
| radix BSD RND | 2.2 (1) … 12.7 (8) | MLps | Xeon HT, 1..8 threads | tabela sem número, p. 35 |
| radix BSD REP | 9.6 (1) … 38.4 (8) | MLps | idem | p. 35 |
| entrada da trie radix | about 200 | bytes | máquina de 64 bits | §4.3, p. 35 |
| custo de update | 11.9, 11.0 e 10.2 | µs por prefixo | D16R, "D18" (assim impresso), D20R; LINX; remove e re-adiciona cada prefixo em ordem aleatória | §4.4, p. 36 |
| taxa de update | more than 80,000 | updates/s | sem contar a atualização da radix | §4.4, p. 36 |
| desempenho em 1 núcleo (conclusão) | from 50 million to 200 million | lookups/s | conforme a config e o padrão de consulta | §5, p. 36 |
| range table ingênua | 10^6 elements, about 6 Mbytes, 20 search steps | — | ~500,000 prefixos, pior caso | §3.1, p. 32 |
| literatura | 2 and 5 MLps (1999) [14]; 3 to 20 MLps (2006) [6]; around 88 MLps (Chiueh-Pradhan, Alpha 500 MHz) [18] | MLps | citados, não medidos | §2, p. 31 |
| literatura | 24 (Lampson-Varghese); 4.5 (Lulea) | bytes/prefixo | citados | §2, p. 31 |
| latência DRAM | roughly 50 | ns | — | §1, p. 30 |
| Public Review | 700 million; 500K entries | lookups/s; prefixos | — | p. 29 |

Lido nos gráficos, não impresso [leitura aproximada]:
- Fig. 7: em /8 o update médio fica perto de 3–4 ms (D20R), 1,5 ms (D18R) e 0,5 ms (D16R). Acima de k, fica em torno de 0,01 ms.
- Fig. 6: com 8 núcleos, o DIR-24-8 fica perto de 190 MLps e a D24R perto de 150.

## Atualização

- Unidades:
  - [afirma] Tempo de parede por prefixo, em µs no texto do §4.4 e em ms no eixo da Fig. 7.
  - [afirma] A reconstrução completa é medida em ms (Tab. 1 e Tab. 2).
- Mecanismo:
  - [afirma] Um prefixo com comprimento < k é expandido em entradas de um chunk cada. Cada chunk afetado é reconstruído do zero a partir da radix (§3.4, p. 33).
  - [afirma] É possível juntar vários updates "by delaying the reconstruction for several milliseconds after the first update is received".
  - [afirma] Os chunks podem ser processados em paralelo, mas isso "does not reduce the total work" (§3.4, p. 33).
- Caso médio:
  - [afirma] 11.9 / 11.0 / 10.2 µs por prefixo (D16R / D18 / D20R), o que dá "more than 80,000 updates per second". O número exclui o tempo de atualizar a radix (§4.4, p. 36).
- Pior caso:
  - Nenhum número escrito no texto: não encontrado.
  - [afirma] A Fig. 7 mostra que prefixos curtos custam mais: "less specific IPv4 prefixes was more time consuming" (§4.4, p. 36).
  - [leitura aproximada] Um /8 custa da ordem de ms, até cerca de 3–4 ms na D20R.
- Reconstrução total:
  - [afirma] De 89.44 a 227.47 ms nas três tabelas BGP (Tab. 1). Na Tab. 2 vai até 2929 ms (k=24, AMD).
  - [afirma] "can be done in a fraction of a second, as reported earlier in tables 1 and 2" (§4.4, p. 36).
- [inferência] O §4.4 não mede updates e lookups ao mesmo tempo, e o artigo não descreve como os lookups convivem com uma reconstrução em curso (sincronização ou troca de ponteiros): não encontrado.

## Memória e energia

- Pegada:
  - [afirma] 782 KB (D16R) e 1512 KB (D18R) no LINX; até 65560 KB com k=24 (Tab. 2, p. 34).
  - [afirma] A memória "grows exponentially for large k" (§4.2, p. 34).
- On-chip:
  - [afirma] A estrutura toda fica na DRAM, mas é pequena o bastante para "reside entirely in L2 or L3 CPU caches" (§1, p. 30). D19R e D20R só valem em máquinas com L3 muito grande ou muito rápida (§4.2, p. 34).
  - [inferência] A linha "static" da Tab. 1 (262248 B com k=16, 1048676 B com k=18) é quase exatamente 2^k × 4 B. Ou seja, a lookup table fixa já ocupa 256 KB (k=16) e 1 MB (k=18): cerca de 1/3 da pegada da D16R e 2/3 da D18R no LINX.
- DRAM:
  - [afirma] DXR "requires less DRAM bandwidth" que o DIR-24-8 (Abstract, p. 30).
  - [afirma] Os 32 MB do DIR-24-8 saturam a DRAM quando há várias threads (§4.3, p. 35).
- Energia: não encontrado. O único termo de energia no artigo é "power-hungry TCAMs" (§1, p. 30), sem número.
- Custo (US$, área): não encontrado.

## Limitações

Admitidas pelo artigo:
- [afirma] Só IPv4. O lookup direto é inviável em IPv6 (§3, p. 31).
- [afirma] O benchmark sintético isola o lookup. Num datapath real, outras etapas disputam a cache e o k ótimo seria menor (§4.2, p. 34). O estudo com netmap fica como trabalho futuro (§5, p. 36).
- [afirma] Sensibilidade de 10–20% a código, compilador e configuração de memória (§4.1, p. 34).
- [afirma] Há interferência no L2 compartilhado (escada na Fig. 4, p. 35) e uma desaceleração de cerca de 15% por thread com 8 núcleos (§4.2, p. 35).
- [afirma] A latência de update não inclui a atualização da radix (§4.4, p. 36). Paralelizar a reconstrução não reduz o trabalho total (§3.4, p. 33).
- [afirma] Limites de formato: 2^19 faixas e 4096 entradas por chunk (§3.2, p. 32).

Inferidas:
- [inferência] RND uniforme sobre o espaço de endereços favorece o DXR: 75,7% (D16R) a 94,5% (D20R) das chaves resolvem no índice direto (Tab. 3). Tráfego real se concentra em regiões roteadas e densas, com mais chunks longos, e não foi testado. Chamar RND de "worst case" (§4.1) é discutível.
- [inferência] Só o LINX entra na avaliação de desempenho. U. Oregon e PAIX aparecem apenas na Tab. 1 (pegada e build).
- [inferência] A Tab. 1 não diz em qual CPU o build foi medido. O valor 89.44 bate com o 89 da Tab. 2 (AMD). No Xeon, os builds de k=16 e k=18 são 111 e 280 ms (Tab. 2).
- [inferência] Os concorrentes são só o DIR-24-8 em software, sem implementador declarado, e a radix BSD. Não houve comparação medida com Lulea, LC-trie ou Tree Bitmap; os números deles vêm de máquinas de 1999/2006.
- [inferência] O "80,000 updates/s" é uma média dominada por prefixos ≥ /17. Updates de prefixos curtos levam ms (Fig. 7). O pior caso e a variância não aparecem.
- [inferência] Mede lookups/s, não pacotes encaminhados. Não há I/O no laço.
- [inferência] Não há análise de energia nem de custo, embora o artigo argumente contra TCAMs "power-hungry".

## Ganchos com outros artigos do corpus

- ruiz01:
  - [afirma] Citado como [14]: survey de soluções em software até 2001 (§2, p. 31).
  - [afirma] A comparação de tempos de execução do ruiz01 é considerada "Especially important"; o artigo usa dele o pico de "2 and 5 MLps on 1999 machines" (§2, p. 31).
- shah01: não citado. [inferência] O contraste é de unidade: o shah01 mede custo de update em movimentos de entradas da TCAM; o DXR mede em µs de CPU por prefixo.
- zane03: não citado. [inferência] O "power-hungry TCAMs" (§1, p. 30) bate com a motivação do zane03, mas o DXR não traz número de potência.
- eath04: não citado. [afirma] O esquema compacto de referência é o Lulea [4] (4.5 bytes/prefixo, §2, p. 31).
- asai15 e yang18: posteriores, então não são citados. [verificação cruzada, só contagem] O texto de 2785956.2787474.pdf (asai15) tem 30 ocorrências de "DXR|Zec" e o de Sail_2_ToN_18.pdf (yang18) tem 5. Quem implementou o DXR nas comparações deles deve ser conferido nos fichamentos respectivos.

## Conferência das afirmações antigas (IA, 31/10 e 01/11)

1. Resumo com 490 Mlps em 8 núcleos, chaves IPv4 uniformes e 782 KB: **CONFIRMADO**.
   - Abstract, p. 30: "D16R, distills a real-world BGP snapshot with 417,000 IPv4 prefixes and 213 distinct next hops into a structure consuming only 782 Kbytes, less than 2 bytes per prefix, and achieves 490 million lookups per second (MLps) in synthetic tests using uniformly random IPv4 keys on a commodity 8-core CPU."
   - O "840 Mlps" do preprint: **NÃO ENCONTRADO** nesta versão; "840" não aparece no PDF. A versão publicada diz 490 MLps (D16R) e "exceed 700 MLps" para outras configs (Abstract; §1, p. 30). A Public Review (p. 29) fala em 700 milhões.
2. §4.4 e Fig. 7, eixo de 0,001 a 10 ms: **CONFIRMADO** (Fig. 7, p. 36, eixo "Average update time (ms)", log de 0.001 a 10).
   - Médias "11,9, 11,0 e 10,2 ms": **DIVERGENTE**. A unidade impressa é **µs**, não ms. O texto impresso também diz "D18" e não "D18R" (§4.4, p. 36).
3. Mais de 80.000 updates/s: **CONFIRMADO**, e coerente com µs (1/11,9 µs ≈ 84.000/s).
   - A frase na página renderizada (p. 36, conferida também a 300 dpi): "On average, updating lookup structures took 11.9, 11.0, and 10.2 µs per prefix for D16R, D18 and D20R respectively, which corresponds to more than 80,000 updates per second (latencies do not include the time required for updating the primary database, i.e. the BSD radix tree)."
   - Eixo da Fig. 7: "Average update time (ms)".
   - O pdftotext extrai o glifo µ como "m" e produz "10.2 ms". O erro antigo vem daí.
   - [inferência] As médias em µs também batem com a Fig. 7: para prefixos > k, a curva fica em torno de 0,01 ms = 10 µs.
4. Reconstrução completa de 89 a 227 ms nas três tabelas BGP (Tab. 1, D16R e D18R): **CONFIRMADO**.
   - Valores impressos: 89.44 (LINX, D16R) a 227.47 (U. Oregon, D18R) ms (Tab. 1, p. 33).
   - Ressalva: a Tab. 1 não diz a CPU. No Xeon, k=18 leva 280 ms (Tab. 2, p. 34).
5. "Conclusão (§5) fala em reconstrução em fração de segundo": **DIVERGENTE** quanto ao local.
   - A frase está no fim do §4.4, p. 36: "Rebuilding all lookup structures corresponding to a full sized BGP feed from scratch is much faster and can be done in a fraction of a second, as reported earlier in tables 1 and 2."
   - O §5 (p. 36) não fala em reconstrução.
6. DOI: **NÃO ENCONTRADO**; não está impresso no PDF.
