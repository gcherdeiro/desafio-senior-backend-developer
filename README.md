# API Carteira Digital - Prefeitura do Rio de Janeiro

A Prefeitura do Rio de Janeiro oferece aos cidadãos uma **API de Carteira Digital**, onde os usuários poderão armazenar e gerenciar documentos digitais, consultar e carregar créditos do transporte público e acessar serviços municipais via chatbot.

## 🛠️ Decisões Técnicas

As decisões técnicas deste projeto foram tomadas com base em boas práticas de desenvolvimento, escalabilidade e facilidade de manutenção. Abaixo estão os principais pontos:

### Tecnologias Utilizadas

- **FastAPI**:
  - Framework moderno e de alto desempenho para construção de APIs.
  - Suporte nativo para geração de documentação OpenAPI e validação de dados com Pydantic.

- **SQLAlchemy**:
  - ORM robusto para modelagem e interação com o banco de dados relacional (MySQL).
  - Utilizado em conjunto com o Alembic para gerenciar migrações de esquema.

- **Alembic**:
  - Ferramenta de migração de banco de dados para versionamento e controle de alterações no esquema.

- **PyMySQL**:
  - Driver para conectar a aplicação ao banco de dados MySQL.

- **Uvicorn**:
  - Servidor ASGI de alto desempenho para executar a aplicação FastAPI.

- **Passlib e Bcrypt**:
  - Utilizados para hashing seguro de senhas, garantindo a segurança dos dados dos usuários.

- **Python-Jose e Cryptography**:
  - Implementação de JWT para autenticação segura e criptografia de dados sensíveis.

- **Pytest e Httpx**:
  - Ferramentas para testes automatizados, garantindo a qualidade e confiabilidade do código.

### Docker e Docker Compose

- **Docker**:
  - O projeto é containerizado para garantir consistência no ambiente de desenvolvimento e produção.
  - O `Dockerfile` instala todas as dependências necessárias e configura o ambiente para rodar a aplicação.

- **Docker Compose**:
  - Orquestra os containers da aplicação e do banco de dados MySQL.
  - Configura variáveis de ambiente e dependências entre os serviços.

### Decisões de Arquitetura

- **Modularidade**:
  - O código está organizado em módulos (`routers`, `models`, `schemas`) para facilitar a manutenção e escalabilidade.

- **Banco de Dados Relacional**:
  - MySQL foi escolhido por sua robustez e ampla adoção no mercado.

- **Segurança**:
  - Hashing de senhas com Bcrypt.
  - Autenticação baseada em JWT para proteger os endpoints.

- **Testes Automatizados**:
  - Testes foram implementados para validar funcionalidades críticas, como autenticação e manipulação de documentos.

Essas decisões garantem que o projeto seja escalável, seguro e fácil de manter, atendendo aos requisitos do desafio técnico.

## 🗂️ Estrutura do Código

O projeto está organizado de forma modular para facilitar a manutenção e a escalabilidade. Abaixo está uma explicação sobre a divisão dos arquivos e pastas:

### Arquivo Principal
- **`main.py`**:
  - Este é o ponto de entrada da aplicação.
  - Configura a conexão com o banco de dados e registra as rotas definidas na pasta `routers`.
  - Também inclui a configuração básica do FastAPI, como título e descrição da API.

### Pasta `routers`
- Contém os módulos que implementam as funcionalidades principais da API. Cada arquivo é responsável por uma parte específica do sistema:
  - **`auth.py`**: Gerencia autenticação e criação de usuários.
  - **`chatbot.py`**: Implementa o endpoint para o chatbot.
  - **`documents.py`**: Gerencia os documentos digitais dos usuários.
  - **`health.py`**: Fornece o endpoint de verificação de saúde da API e do banco de dados.
  - **`transport.py`**: Gerencia o saldo e recarga do transporte público.
  - **`test_auth.py`**: Contêm testes automatizados para validar as funcionalidades de autenticação.

### Arquivos de Configuração do Docker
- **`Dockerfile`**:
  - Define como a imagem Docker da aplicação será construída.
  - Inclui a instalação das dependências e o comando para iniciar o servidor FastAPI.
- **`docker-compose.yml`**:
  - Orquestra os containers da aplicação e do banco de dados MySQL.
  - Configura as variáveis de ambiente e as conexões entre os serviços.

### Outros Arquivos Importantes
- **`alembic/`**:
  - Contém as configurações e scripts de migração do banco de dados.
- **`database.py`**:
  - Configura a conexão com o banco de dados usando SQLAlchemy.
- **`models.py`**:
  - Define os modelos do banco de dados.
- **`schemas.py`**:
  - Define os esquemas de validação de dados usando Pydantic.
- **`requirements.txt`**:
  - Lista as dependências do projeto que serão instaladas no ambiente Docker.

Essa estrutura modular facilita a navegação e o entendimento do projeto, permitindo que cada funcionalidade seja desenvolvida e testada de forma independente.

## 🚀 Como Rodar o Projeto com Docker

Este projeto está configurado para ser executado facilmente usando Docker e Docker Compose. Siga os passos abaixo para configurar e iniciar o ambiente:

### Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos para execução

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd desafio-senior-backend-developer
   ```

2. **Configure o arquivo `.database` (opcional)**:
   - O projeto utiliza a variável `DATABASE_URL` para configurar a conexão com o banco de dados.
   - Por padrão, o `docker-compose.yml` já está configurado para usar o MySQL com as credenciais:
     ```
     DATABASE_URL=mysql+pymysql://root:testeSenhaInfinita@db:3306/carteira_digital
     ```
   - Se necessário, ajuste as credenciais no `docker-compose.yml` ou crie um arquivo `.env` com a variável `DATABASE_URL`.

3. **Inicie os containers**:
   - Execute o seguinte comando para construir e iniciar os containers:
     ```bash
     docker-compose up --build
     ```
   - Isso iniciará:
     - O container da aplicação FastAPI na porta `8000`.
     - O container do banco de dados MySQL na porta `3306`.
     
4. **Executar migrações do banco de dados**:
   - Após iniciar os containers, entre no bash da aplicação:
    ```bash
    docker exec -it carteira_digital_app bash
    ```
   - Então aplique e atualize as migrações para criar as tabelas no banco de dados:
     ```bash
     alembic revision --autogenerate -m "criar tabelas"
     alembic upgrade head
     ```

5. **Acesse a aplicação**:
   - Acesse a documentação interativa da API (Swagger UI) em:
     ```
     http://localhost:8000/docs
     ```
   - Ou a interface ReDoc em:
     ```
     http://localhost:8000/redoc
     ```

6. **Parar os containers**:
   - Para parar os containers, use o comando:
     ```bash
     docker-compose down
     ```

### Rodando o Projeto Localmente

Se preferir rodar o projeto localmente, sem o uso de Docker, siga os passos abaixo:

1. **Pré-requisitos**:
   - Certifique-se de ter o Python 3.11 instalado.
   - Instale o MySQL em sua máquina e configure-o com as credenciais desejadas.

2. **Configuração do Banco de Dados**:
   - Crie um banco de dados chamado `carteira_digital` no MySQL:
     ```sql
     CREATE DATABASE carteira_digital;
     ```
   - Crie um usuário e conceda permissões ao banco:
     ```sql
     CREATE USER 'root'@'localhost' IDENTIFIED BY 'testeSenhaInfinita';
     GRANT ALL PRIVILEGES ON carteira_digital.* TO 'root'@'localhost';
     FLUSH PRIVILEGES;
     ```

3. **Configuração do Ambiente**:
   - Clone o repositório e navegue até o diretório do projeto:
     ```bash
     git clone <URL_DO_REPOSITORIO>
     cd desafio-senior-backend-developer
     ```
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configuração da URL do Banco de Dados**:
   - No arquivo `database.py`, configure a variável `DATABASE_URL` com as credenciais do banco local:
     ```python
     DATABASE_URL = "mysql+pymysql://root:testeSenhaInfinita@localhost:3306/carteira_digital"
     ```

5. **Executar Migrações**:
   - Aplique as migrações para criar as tabelas no banco de dados:
     ```bash
     alembic upgrade head
     ```

6. **Iniciar o Servidor**:
   - Execute o servidor FastAPI:
     ```bash
     uvicorn main:app --host 127.0.0.1 --port 8000 --reload
     ```
   - Acesse a aplicação em:
     ```
     http://127.0.0.1:8000/docs
     ```

### Testes Automatizados

Para rodar os testes automatizados, execute o seguinte comando:
```bash
docker exec -it carteira_digital_app pytest
```

### Problemas Comuns

- **Erro de conexão com o banco de dados**:
  - Certifique-se de que o container do banco de dados está rodando corretamente.
  - Verifique as credenciais no `docker-compose.yml` ou no arquivo `.env`.

- **Portas em uso**:
  - Certifique-se de que as portas `8000` e `3306` não estão sendo usadas por outros serviços.

- **Problemas com migrações do Alembic**:
  - Caso encontre problemas ao rodar as migrações (como tabelas inexistentes ou conflitos de versões), siga os passos abaixo para limpar as versões e criar uma nova migração limpa:
    1. **No projeto local**:
       - Apague o conteúdo da pasta `alembic/versions/`.
         ```powershell
         Remove-Item -Path .\alembic\versions\* -Recurse -Force
         ```
       - Certifique-se de que o banco de dados está limpo (sem tabelas ou dados antigos).
       - Exclua o arquivo `alembic_version` do banco de dados, caso exista.
    2. **No container Docker**:
       - Acesse o container da aplicação:
         ```bash
         docker exec -it carteira_digital_app bash
         ```
       - Dentro do container, navegue até a pasta `alembic/versions/` e apague os arquivos:
         ```bash
         rm -rf alembic/versions/*
         ```
       - Certifique-se de que o banco de dados no container também está limpo.
    3. **Criar uma nova migração**:
       - Gere uma nova migração com o comando:
         ```bash
         alembic revision --autogenerate -m "nova migração limpa"
         ```
       - Aplique a migração:
         ```bash
         alembic upgrade head
         ```
    4. **Reinicie os containers**:
       - Pare e reinicie os containers para garantir que tudo está funcionando corretamente:
         ```bash
         docker-compose down
         docker-compose up --build
         ```

## 🔑 Autenticação e Uso dos Endpoints

A maioria dos endpoints desta API requer autenticação. Para acessar esses endpoints, siga os passos abaixo:

1. **Criação de Conta**:
   - Use o endpoint `/auth/` para criar uma conta fornecendo um nome de usuário e uma senha.
   - Exemplo de requisição:
     ```bash
     curl -X POST http://localhost:8000/auth/ \
     -H "Content-Type: application/json" \
     -d '{"username": "seu_usuario", "password": "sua_senha"}'
     ```

2. **Login**:
   - Use o endpoint `/auth/token` para realizar o login com as credenciais criadas.
   - Após o login bem-sucedido, um token de acesso será gerado e armazenado como um cookie no navegador ou cliente HTTP.
   - Exemplo de requisição:
     ```bash
     curl -X POST http://localhost:8000/auth/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d 'username=seu_usuario&password=sua_senha'
     ```

3. **Acesso aos Endpoints Protegidos**:
   - Após o login, o token de acesso será automaticamente enviado como um cookie em todas as requisições subsequentes.
   - Certifique-se de que o cliente HTTP (navegador, Postman, etc.) está configurado para enviar cookies nas requisições.

4. **Logout**:
   - Para encerrar a sessão, basta limpar os cookies do navegador ou cliente HTTP.

Essa abordagem garante que apenas usuários autenticados possam acessar os recursos protegidos da API, como gerenciamento de documentos e saldo de transporte público.
