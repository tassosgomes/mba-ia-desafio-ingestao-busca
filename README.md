# RAG com pgVector e LangChain

Este projeto demonstra a implementação de um sistema de Retrieval-Augmented Generation (RAG) utilizando pgVector para armazenamento e busca de vetores, e LangChain para orquestração do fluxo de dados. O sistema é capaz de ingerir um documento PDF, processá-lo em chunks, gerar embeddings e armazená-los em um banco de dados PostgreSQL com a extensão pgVector. Posteriormente, um script de chat permite que o usuário faça perguntas em linguagem natural, que são respondidas com base no conteúdo do documento PDF.

## Pré-requisitos

Antes de começar, certifique-se de que você tem as seguintes ferramentas instaladas em seu sistema:

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)
*   [Python 3.10+](https://www.python.org/downloads/)
*   [pip](https://pip.pypa.io/en/stable/installation/)

## Instalação e Setup

Siga os passos abaixo para configurar e executar o projeto.

### 1. Clone o Repositório

Clone este repositório para a sua máquina local:

```bash
git clone https://github.com/tassosgomes/mba-ia-desafio-ingestao-busca.git
cd mba-ia-desafio-ingestao-busca
```

### 2. Crie e Configure o Arquivo de Ambiente

Crie um arquivo `.env` na raiz do projeto, você pode copiar o arquivo de exemplo `.env.example`:

```bash
cp .env.example .env
```

Agora, edite o arquivo `.env` com os seus dados. As variáveis de ambiente são as seguintes:

*   `POSTGRES_USER`: Nome de usuário para o banco de dados PostgreSQL. O padrão é `postgres`.
*   `POSTGRES_PASSWORD`: Senha para o banco de dados PostgreSQL. O padrão é `postgres`.
*   `POSTGRES_DB`: Nome do banco de dados. O padrão é `rag`.
*   `DATABASE_URL`: URL de conexão com o banco de dados. O formato é `postgresql+psycopg://USER:PASSWORD@HOST:PORT/DATABASE`. Substitua as variáveis com os valores correspondentes.
*   `PDF_PATH`: Caminho para o arquivo PDF que será ingerido. O padrão é `document.pdf`.
*   `PG_VECTOR_COLLECTION_NAME`: Nome da coleção no pgVector onde os embeddings serão armazenados.
*   `OPENAI_API_KEY`: Sua chave de API da OpenAI.
*   `OPENAI_EMBEDDING_MODEL`: Modelo de embedding da OpenAI a ser utilizado. O padrão é `text-embedding-3-small`.
*   `OPENAI_CHAT_MODEL`: Modelo de chat da OpenAI a ser utilizado. O padrão é `gpt-4`.

**Exemplo de arquivo `.env`:**

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=rag
DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/rag"
PDF_PATH="document.pdf"
PG_VECTOR_COLLECTION_NAME="my_collection"
OPENAI_API_KEY="sua-chave-de-api-da-openai"
OPENAI_EMBEDDING_MODEL="text-embedding-3-small"
OPENAI_CHAT_MODEL="gpt-4"
```

### 3. Instale as Dependências

Instale as dependências do projeto utilizando o `pip` e o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Uso

Siga a ordem de execução abaixo para garantir o funcionamento correto do sistema.

### 1. Inicialize os Serviços com Docker Compose

Com o Docker em execução, inicialize os serviços do banco de dados PostgreSQL com pgVector:

```bash
docker-compose up -d
```

Este comando irá criar e iniciar um container com o PostgreSQL e a extensão pgVector habilitada.

### 2. Execute o Script de Ingestão

Após a inicialização bem-sucedida do banco de dados, execute o script de ingestão para processar o PDF e popular o banco de dados com os embeddings:

```bash
python src/ingest.py
```

Este script irá ler o PDF especificado em `PDF_PATH`, dividi-lo em chunks, gerar os embeddings e armazená-los na coleção do pgVector.

### 3. Inicie o Script de Chat

Com os dados ingeridos, você pode iniciar o script de chat para interagir com o sistema:

```bash
python src/chat.py
```

O script solicitará que você digite uma pergunta. A resposta será gerada com base no conteúdo do documento PDF.

## Estrutura do Projeto

```
.
├── .env.example
├── .gitignore
├── docker-compose.yml
├── document.pdf
├── README.md
├── requirements.txt
└── src
    ├── chat.py
    ├── ingest.py
    └── search.py
```

*   `docker-compose.yml`: Define o serviço do PostgreSQL com pgVector.
*   `document.pdf`: Documento de exemplo para ingestão.
*   `src/ingest.py`: Script para ingestão do PDF, geração de embeddings e armazenamento no banco de dados.
*   `src/search.py`: Contém a lógica para buscar informações no banco de dados e interagir com o modelo de linguagem.
*   `src/chat.py`: Script para simular um chat no terminal, utilizando as funções de `search.py`.