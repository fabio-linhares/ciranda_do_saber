# Portão de Segurança e Privacidade: Threat Modeling & Conformidade LGPD

## 1. Conformidade Rigorosa com a LGPD (Art. 14 - Crianças e Adolescentes)

O tratamento de dados pessoais de crianças e adolescentes no projeto **Ciranda do Saber** rege-se pelos princípios da necessidade, melhor interesse do menor e segurança por design (*Privacy by Design*):

1. **Pseudonimização e Anonimização:**
   - Nenhuma biometria ou dado sensível de identificação facial/vocal é gravado ou transmitido para servidores remotos.
   - O estudante é identificado localmente por apelido ou token alfanumérico não correlacionável publicamente (ex.: `ALUNO-AL-042`).
2. **Dados Restritos ao Progresso Pedagógico:**
   - Armazenam-se unicamente os vetores de competências e lacunas da BNCC (ex.: `EF01MA01: 0.85`).
3. **Consentimento dos Responsáveis:**
   - Termo de consentimento simplificado e físico obtido na matrícula comunitária, arquivado na associação ou escola parceira.

---

## 2. Threat Modeling (AppSec & Dispositivos Compartilhados)

| Vetor de Risco | Impacto | Mitigação Adotada |
|---|---|---|
| **Acesso Indevido no Dispositivo Comunitário** | Médio | Modo Kiosk/Pin para monitores; sessão de microgrupo isolada sem expor histórico pessoal entre turnos |
| **Tampering de Métricas de Progresso** | Baixo | Assinatura local dos pacotes de avaliação antes do sync com a API |
| **Injeção de Prompt / Alucinação em Conteúdo Didático** | Alto | Curadoria determinística de matrizes da BNCC com RAG estritamente ancorado em fontes oficiais |
| **Queda de Conectividade em Área Rural** | Alto | Banco de dados local (SQLite / offline-first); a tutoria em áudio funciona 100% offline |
