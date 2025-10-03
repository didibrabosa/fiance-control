# Finance Control

Projeto para controle financeiro pessoal.

## Estrutura do Projeto

- **Dockerfile:** Configura a imagem da API.
- **docker-compose.yml:** Define os serviços para a API e o banco de dados.
- **main.py:** Arquivo principal da API implementado com FastAPI.
- **requirements.txt:** Dependências do projeto.
- **configs/migrations/V1_create_finances_tables.sql:** Script SQL para criação das tabelas no banco de dados.
- **.env.example:** Exemplo de configuração das variáveis de ambiente.

## Pré-requisitos

- Docker
- Docker Compose

## Setup

1. **Clone o Repositório**

2. **Configure as Variáveis de Ambiente**

   Renomeie o arquivo `.env.example` para `.env` e preencha os valores:
   ```bash
   cp .env.example .env
   ```
   
   Atualize com:
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`

3. ***Inicialize os Containers com Docker Compose**
   Execute:
   ```bash
   docker-compose up --build
   ```

   - A API ficará disponível em: `http://localhost:8000`
   - O PostgreSQL estará disponível na porta: `5432`

### Uso
- A API é desenvolvida com FastAPI.
- Utilize os endpoints da API para gerenciar suas finanças pessoais.
- O script SQL de migração (`V1_create_finances_tables.sql`) configura automaticamente as tabelas no banco de dados.

### Desenvolvimento Local
Para rodar a API localmente sem containers:

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute a API:**
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ``` 

### Licença
Este projeto está licenciado sob a Licença MIT.
Veja o `LICENSE.txt` para mais detalhes.
