# Gerenciar emprétimos

# Instalação
Clone o repositório e dentro dele crie um ambiente virtual

Utilize o pip para baixar as dependências do projeto:
```
pip install -r requirements.txt
```
Navegue até a pasta raiz do seu projeto Django no terminal.

Execute o comando python ``` manage.py migrate ```. Isso criará as tabelas do banco de dados necessárias para o Django e o Django REST framework.

Execute o comando python ``` manage.py createsuperuser ``` para criar um superusuário. Isso permitirá que você faça login na API e acesse as funcionalidades protegidas.

Execute o comando python ``` manage.py runserver ```. Isso iniciará o servidor de desenvolvimento do Django.

Para acessar a API será necessária a criação do token de autenticação, isso será feito pelo Postman, criando uma requisção POST e adicionando no Body a key username, para nome do usuário e a key password para a senha dele. Após isso será gerado um Token de autenticação.

Nas outras requisições dos outros Endpoints, sempre colocar esse token no Headers com a Key sendo Authorization e o value Token valordotoken

Os Endpoints de de listagem de de empréstimos e de saldo devedor é só colocar a URL correspondente, já os de post são necessários os json com as informações que serão inseridas.

Urls:
Criação token
http://127.0.0.1:8000/api-token-auth/
Listagem empréstimos
http://127.0.0.1:8000/api/loans/
Criação de empréstimos
http://127.0.0.1:8000/api/loans/create/
Criação de pagamentos
http://127.0.0.1:8000/api/payments/create/
Listagem de saldo devedor
http://127.0.0.1:8000/api/loan_balance/<int:loan_id>/

Criação de empréstimos, exemplo de body
{
    "client": 1,
    "amount": 1000.0,
    "interest_rate": 0.05,
    "requested_at": "2023-05-06T10:00:00Z",
    "bank": "Banco do Brasil",
    "ip_address": "10101010"
}
Criação de pagamentos, exemplo de body
{
    "date": "2023-05-06",
    "amount": 100.0,
    "loan": 1
}

Para rodar os testes apenas digitar python ``` manage.py test test.test ```



