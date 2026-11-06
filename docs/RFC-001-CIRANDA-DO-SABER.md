# RFC-001: Arquitetura do Sistema Ciranda do Saber

## Status: APROVADO // PROTOCOLO FÁBIO LINHARES
- **Autor Primário:** Fábio Linhares (fabiolinharez@gmail.com)
- **Coautores:** Cristiano Estumano & Luryan Delevati
- **Instituição:** Universidade Federal de Alagoas (UFAL) — PPGI / IC
- **Data:** 05 de Novembro de 2026
- **Alinhamento:** AI4Good / Brazil Conference 2027 (Harvard & MIT)

---

## 1. Visão Geral e Motivação

O **Ciranda do Saber** aborda o abismo educacional brasileiro atacando a restrição material mais severa das famílias vulneráveis: a ausência de dispositivos pessoais e conectividade doméstica.

Historicamente, o *Problema dos 2 Sigmas de Benjamin Bloom* demonstra que a tutoria individualizada ou em pequenos grupos eleva o rendimento escolar em dois desvios-padrão em relação ao ensino expositivo tradicional de massa. Contudo, tutores particulares são economicamente inacessíveis às camadas empobrecidas.

O Ciranda do Saber introduz o paradigma da **Tutoria Coletiva Adaptativa Assistida por IA**:
1. Com apenas 5 a 10 smartphones comunitários em um polo de contraturno (associação, biblioteca, paróquia, escola pública do campo ou periferia), viabiliza-se o atendimento de 20 a 40 crianças simultaneamente.
2. Cada aparelho atende um **microgrupo de 3 a 4 estudantes** agrupados dinamicamente por lacuna cognitiva na Base Nacional Comum Curricular (BNCC).
3. Um monitor voluntário comunitário atua como o facilitador físico ("avatar humano" da IA), desenhando no quadro, entregando materiais táteis e tirando dúvidas sob o comando pedagógico de um tutor inteligente em áudio.

---

## 2. Pilares de Arquitetura

```
                     ┌───────────────────────────┐
                     │    Diagnóstico Inicial    │
                     │  (Mapeamento de Lacunas)  │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │   Algoritmo de Clustering │
                     │  (Microgrupos de 3-4 pax) │
                     └─────────────┬─────────────┘
                                   │
                ┌──────────────────┴──────────────────┐
                ▼                                     ▼
     Microgrupo Português (EF01LP02)        Microgrupo Matemática (EF01MA01)
     ├─ 1 Smartphone (Ciranda Audio)        ├─ 1 Smartphone (Ciranda Audio)
     ├─ 1 Monitor Voluntário                ├─ 1 Monitor Voluntário
     └─ 3 Crianças (papel, lápis, lousa)    └─ 3 Crianças (papel, lápis, lousa)
```

### 2.1 Agrupamento Dinâmico (Adaptive Micro-Clustering)
- O agrupamento não obedece a idade ou série burocrática, mas sim a competência não consolidada da BNCC.
- A cada ciclo de 30-45 minutos, uma microavaliação formativa analisa o progresso e reconfigura as turmas, permitindo progressão contínua por maestria.

### 2.2 Simbiose Tutor IA ↔ Facilitador Humano
- A IA assume a carga cognitiva da preparação da aula, sequência didática, ritmo e explicação conceitual em áudio com linguagem simples e regionalizada.
- O voluntário assume a dimensão socioemocional, acolhimento, disciplina positiva e mediação física com materiais concretos.

### 2.3 Resiliência Offline-First
- Operação em nós locais desconectados da internet (em áreas rurais ou de conectividade instável).
- Sincronização assíncrona periódica quando houver rede disponível via APIs REST leves.

---

## 3. Divisão de Responsabilidades Técnicas (Trio UFAL)

- **Fábio Linhares:** Engenharia de RAG, curadoria pedagógica BNCC, governança e conformidade LGPD da Infância.
- **Cristiano Estumano:** Arquitetura do aplicativo mobile, algoritmos matemáticos de clustering e didática de exatas.
- **Luryan Delevati:** Engenharia de APIs, arquitetura de microsserviços, resiliência offline e metodologia para comunidades do campo.
