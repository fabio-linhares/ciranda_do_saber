# 🪅 Ciranda do Saber: Roda Viva da Aprendizagem Coletiva

<div align="center">

### **Universidade Federal de Alagoas (UFAL)**
#### **Instituto de Computação (IC) — Programa de Pós-Graduação em Informática (PPGI)**
#### *Iniciativa Submetida ao Programa AI4Good // Brazil Conference 2027 (Harvard & MIT)*

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status: RFC-001 Approved](https://img.shields.io/badge/Status-RFC--001%20Approved-blue.svg)](docs/RFC-001-CIRANDA-DO-SABER.md)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11+-brightgreen.svg)](pyproject.toml)
[![LGPD Compliant](https://img.shields.io/badge/LGPD-Art.%2014%20Compliant-success.svg)](docs/THREAT_MODEL_LGPD.md)

</div>

---

> *"Se a educação sozinha não transforma a sociedade, sem ela tampouco a sociedade muda."*  
> — **Paulo Freire**

---

## 📌 1. A Tese do Ciranda do Saber

No Brasil profundo, milhões de crianças frequentam a escola pública sem aprender a ler, escrever ou calcular o básico. Famílias de classe média e alta contratam professores particulares e garantem computadores em casa. Crianças de comunidades periféricas e rurais não têm nem uma coisa, nem outra.

A pedagogia científica (*Problema dos 2 Sigmas de Benjamin Bloom*) comprova que a **tutoria individual ou em microgrupos** eleva o rendimento escolar em dois desvios-padrão acima da aula expositiva convencional. No entanto, as soluções digitais de IA cometem a falácia de exigir que cada criança vulnerável possua um smartphone pessoal.

O **Ciranda do Saber** inverte essa lógica:
- **Dispositivo Coletivo:** Com apenas **5 a 10 smartphones** em um polo comunitário (associação de moradores, igreja, biblioteca comunitária ou escola aberta no contraturno), criamos um polo capaz de atender dezenas de alunos.
- **Microgrupos Adaptativos:** Cada aparelho atende um microgrupo de 3 a 4 crianças reunidas pela mesma dificuldade real na BNCC (e não pela idade biológica).
- **Simbiose IA + Monitor Voluntário:** A IA assume a pedagogia, a preparação e a explicação em áudio. O monitor voluntário da comunidade atua como os braços e o afeto da sala: desenha na lousa, distribui lápis e papel e orienta as crianças em tempo real.

---

## 🏗️ 2. Arquitetura do Sistema

```
                  ┌─────────────────────────────────────────┐
                  │      Diagnóstico Inicial Adaptativo     │
                  │   (Identificação de Lacunas na BNCC)    │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │   Algoritmo Dinâmico de Micro-Clustering │
                  │     (Agrupamento em trios ou quartetos) │
                  └────────────────────┬────────────────────┘
                                       │
         ┌─────────────────────────────┴─────────────────────────────┐
         ▼                                                           ▼
 ┌───────────────────────────────┐           ┌───────────────────────────────┐
 │   Microgrupo A: Alfabetização │           │   Microgrupo B: Frações/Geom. │
 ├───────────────────────────────┤           ├───────────────────────────────┤
 │ • 1 Aparelho Móvel (Ciranda)  │           │ • 1 Aparelho Móvel (Ciranda)  │
 │ • 1 Monitor Comunitário       │           │ • 1 Monitor Comunitário       │
 │ • 3 a 4 Crianças na bancada   │           │ • 3 a 4 Crianças na bancada   │
 │ • Áudio dialogado e exercícios│           │ • Áudio dialogado e exercícios│
 └───────────────────────────────┘           └───────────────────────────────┘
```

---

## 👥 3. Equipe de Pesquisadores (UFAL / PPGI)

Nossa equipe reúne pesquisadores com vivência nas dores do Nordeste e sólida formação multidisciplinar:

| Pesquisador | Formação Primária | Especialidades Técnicas | Papel no Projeto |
|---|---|---|---|
| **Fábio Linhares** | Bacharel em Direito (Ex-advogado) | Mestrando UFAL, Bancos de Dados, RAG/LLM, Políticas Públicas | Coordenação Geral, Pipeline RAG, Curadoria Curricular BNCC e Governança/LGPD |
| **Cristiano Estumano** | Professor de Matemática | Mestrando UFAL, Desenvolvimento Mobile, Algoritmos de Otimização | Aplicativo Mobile dos Polos, Algoritmos de Clustering Dinâmico e Didática de Exatas |
| **Luryan Delevati** | Engenheiro Agrônomo | Mestrando UFAL, Engenharia de APIs, Microsserviços e Extensão | Infraestrutura de Back-end/APIs, Resiliência Offline-First e Metodologia para Escolas Rurais |

---

## 📂 4. Estrutura do Repositório

```bash
ciranda_do_saber/
├── docs/
│   ├── RFC-001-CIRANDA-DO-SABER.md    # Especificação arquitetural formal
│   ├── THREAT_MODEL_LGPD.md           # Modelagem de ameaças e privacidade
│   └── SUBMISSAO_BRAZIL_CONFERENCE.md # Dossiê de submissão do edital
├── src/
│   └── ciranda/
│       ├── __init__.py
│       ├── bncc_catalog.py            # Catálogo de matrizes e habilidades
│       ├── clustering.py              # Algoritmo de agrupamento dinâmico
│       └── tutor_engine.py            # Motor de orquestração Tutor IA ↔ Monitor
├── tests/
│   ├── test_clustering.py             # Testes do agrupador adaptativo
│   └── test_tutor_engine.py           # Testes da sessão pedagógica em áudio
├── pyproject.toml                     # Metadados e dependências
├── LICENSE                            # Licença MIT (Open Source)
└── README.md
```

---

## 🚀 5. Instalação e Execução Local

```bash
# Clone o repositório
git clone https://github.com/fabio-linhares/ciranda_do_saber.git
cd ciranda_do_saber

# Instale as dependências com pytest
pip install -e ".[dev]"

# Execute a suíte de testes unitários
pytest -v
```

---

## 📜 6. Licença e Governança

Distribuído sob a licença **MIT** como projeto open source de utilidade pública e impacto social.  
Desenvolvido com o compromisso inegociável da soberania de dados, ética algorítmica e proteção integral da infância (LGPD).
