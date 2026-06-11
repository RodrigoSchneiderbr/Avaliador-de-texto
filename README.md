# 📝 Avaliador de Redações com IA (LangGraph + Streamlit)

Este projeto é um sistema automatizado para avaliação e correção de redações em Língua Portuguesa. Ele utiliza uma arquitetura baseada em grafos com **LangGraph** para criar um fluxo condicional de avaliação passo a passo, a API da **OpenAI (GPT-4o-mini)** para a análise textual profunda e o **Streamlit** para fornecer uma interface gráfica simples e intuitiva de upload de arquivos do Microsoft Word (`.docx`).

---

## 🚀 Guia Rápido de Execução

Siga os passos abaixo para configurar e rodar o projeto localmente.

### 📋 Pré-requisito
Certifique-se de ter o **Python 3.10+** instalado em sua máquina.

---

### Passo 1: Criar e Configurar o Arquivo `.env`
O arquivo `.env` serve para armazenar sua chave da OpenAI com segurança.

1. Na raiz do projeto, crie um arquivo de texto comum.
2. Nomeie o arquivo **exatamente** como `.env` (sem extensão `.txt`).
3. Abra o arquivo e cole a sua chave da seguinte maneira:

```text
OPENAI_API_KEY="sk-proj-SuaChaveSecretaDaOpenAiAquiSemEspacosEsemAspas"
```
---

### Passo 2: Criar e Configurar ambiente virtual
Na pasta onde esta o projeto

```text
python -m venv venv
```
---
ativar o ambiente virtual

```text
.\venv\Scripts\Activate.ps1
```
---

### Passo 3: Instalar dependencias

```text
pip install -r requirements.txt
```
----

### Passo 4: Executar o aplicativo

```text
streamlit run app.py
```

### Estrutura do código

```text
projeto_ai_avaliador_texto/
│
├── venv/                      # Pasta do ambiente virtual (gerada no Passo 2)
├── .env                       # Chave secreta da API da OpenAI (gerada no Passo 5)
├── .gitignore                 # Arquivos ignorados pelo Git (gerado na seção Segurança)
├── requirements.txt           # Lista de dependências do projeto
├── avaliador_de_redacao.py    # Motor principal / Backend (LangGraph)
└── app.py                     # Interface Web / Frontend (Streamlit)
```
