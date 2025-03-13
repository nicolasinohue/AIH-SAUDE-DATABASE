# AIH-SAUDE-DATABASE

## Descrição
O **AIH-SAUDE-DATABASE** é uma API REST desenvolvida em Python com Flask para o gerenciamento e exportação de dados de Autorizações de Internação Hospitalar (AIH). A API permite realizar operações CRUD em diversas coleções de um banco de dados MongoDB, facilitando a integração com outros sistemas hospitalares e a análise de dados.

## Funcionalidades
- **CRUD completo** para as coleções do banco de dados (pacientes, consultas, médicos, etc.).
- **Exportação de dados** de uma coleção específica ou de todas as coleções em formato JSON.
- **Automação na serialização** de ObjectIds e datas.
- **Tratamento de erros** para evitar falhas em requisições com IDs inválidos.
- **Estrutura modular**, facilitando a manutenção e expansão do sistema.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework:** Flask
- **Banco de Dados:** MongoDB
- **Bibliotecas:** Flask, PyMongo, bson

## Como Executar o Projeto
### Requisitos
- Python instalado (versão recomendada: 3.x)
- MongoDB rodando localmente ou em um servidor
- Dependências instaladas

### Passos para Execução
1. Clone o repositório:
   ```sh
   git clone https://github.com/nicolasinohue/AIH-SAUDE-DATABASE.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd AIH-SAUDE-DATABASE
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate  # Para Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Inicie o MongoDB localmente (caso não esteja rodando).

6. Execute a API:
   ```sh
   python app.py
   ```

## Endpoints da API
- **Criar documento**: `POST /<collection_name>`
- **Obter todos os documentos**: `GET /<collection_name>`
- **Obter um documento por ID**: `GET /<collection_name>/<doc_id>`
- **Atualizar um documento**: `PUT /<collection_name>/<doc_id>`
- **Deletar um documento**: `DELETE /<collection_name>/<doc_id>`
- **Exportar dados de uma coleção**: `GET /export/<collection_name>`
- **Exportar todas as coleções**: `GET /export_all`

## Contribuição
Para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch com a sua feature (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Adicionando nova funcionalidade'`).
4. Faça um push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.
