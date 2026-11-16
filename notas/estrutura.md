# Proposta de tese e estrutura (para o grupo aprovar antes da prosa)

Base: os 7 fichamentos em `notas/fichamentos/`. Todo número citado aqui está lá com localizador.

## Pergunta
Os resultados publicados permitem escolher entre TCAM e lookup algorítmico (e entre os algoritmos) para LPM,
nos eixos velocidade, memória, atualização e energia?

## Tese
Não diretamente. Cada artigo mede com rigor o eixo em que a proposta é forte e trata os outros de forma
qualitativa ou analítica. O resultado é uma matriz com lacunas sistemáticas:
- os trabalhos algorítmicos (DXR, Poptrie, SAIL) justificam o abandono da TCAM por energia e custo, mas
  nenhum mede a própria energia nem cita números de TCAM;
- os trabalhos de TCAM (Shah & Gupta, CoolCAMs) medem o update e a energia por **modelos** (movimentos,
  entradas pesquisadas × 15 W nominais), sem hardware;
- "memória" e "custo de update" significam coisas diferentes em cada artigo (FIB sem RIB, limite on-chip,
  B/prefixo analítico; movimentos, acessos, node copies, µs);
- o vencedor em velocidade muda com o tráfego (localidade, fração > /24), o tamanho do cache e quem implementou o concorrente.
A contribuição da revisão é normalizar esses números lado a lado e dizer em qual cenário cada resultado vale.

## Estrutura (IEEE, ~9–10 páginas + referências)
- **I. Introdução**: LPM no plano de dados; crescimento da FIB; pergunta e tese; contribuições.
- **II. Método da revisão**: bases e critérios; corpus (Tabela I: 7 artigos, plataforma, tabelas, tráfego,
  quem implementou os concorrentes); como a IA foi usada e verificada (agentes, checagem contra o PDF).
- **III. Fundamentos**: LPM, TCAM (prioridade por posição física), tries multibit e compressão, taxonomia do ruiz01 (que não tem ramo TCAM).
- **IV. Análise por eixo**
  - A. **Velocidade**: o caso Poptrie × SAIL. Cada lado vence no próprio benchmark (1,37–2,62× contra
    1,13–1,14× / 1,59–1,72×). A explicação está no tráfego de borda (21,8% > /24) contra backbone, no L3
    (8 MiB × 4 MB), em quem implementou o quê (o viés é dos dois lados), no xorshift dentro da medida e no
    SAIL vencendo com tráfego sequencial nos dados do próprio Poptrie.
  - B. **Memória**: quatro definições (FIB sem RIB; teto on-chip de 2,13 MB × 44,24 MiB medidos pelo
    Poptrie; B/prefixo analítico; entradas de largura fixa na TCAM).
  - C. **Atualização**: tabela de unidades. Contra o requisito de 100/s com rajadas de "several hundred" a
    "a few thousand"/s, todas as médias passam. O que falta em todos é o pior caso e o comportamento em
    rajada: SAIL ilimitado e com lookup bloqueado; Poptrie copiando até 1 MiB; /8 em ms no DXR; 256 + C sem
    prova no Tree Bitmap; CAO_OPT D/2 dependente dos dados.
  - D. **Energia e custo**: CoolCAMs ("cost-effective", modelo linear sem medição) × Tree Bitmap ("extremely
    prohibitive", >200 W condicionado a não limitar bancos, 20 chips que não fecham com 72 bits). A divergência
    vem do cenário e de contas frágeis dos dois lados. Os algorítmicos não medem energia.
- **V. Discussão: onde cada abordagem se aplica melhor** (backbone × borda; hardware com SRAM on-chip × CPU/NFV;
  IPv6; escala; híbridos: SAIL + TCAM para > /24, trie no índice do CoolCAMs). Inclui uma tabela-síntese.
- **VI. Ameaças à validade e limitações da revisão**: corpus até 2018; tabelas antigas (35K–122K) nos trabalhos
  de TCAM; inconsistências internas encontradas nos artigos; uso de IA.
- **VII. Conclusão**: o que um projetista pode concluir hoje e quais medições faltam (pior caso de update, energia comparável, tráfego real público).

## Decisões para o grupo
1. A tese acima serve, ou preferem um enquadramento mais "quem ganha em cada cenário"?
2. A seção de uso de IA fica dentro do artigo (II-C, curta), e o detalhe vai para a declaração (parte III). Ok?
