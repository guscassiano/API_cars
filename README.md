# API Rest Cars

Esta API tem como objetivo o cadastro de veículos e de marcas dos mesmos.
Para isso utilizamos JWT para autenticação, flake8 para boas práticas organização e padrão de código, além de Django RQL para gerar qualquer filtro necessário. 

Segue imagem para exemplo de carro cadastrado:

![image](https://github.com/user-attachments/assets/7c7f37ba-2fe6-42a6-874b-b007b6e5d641)

### Pré-requisitos

- Python 3.12.3 ou acima
- Os depois requirimentos se encontram no arquivo requirements, para instalá-lo:
    ```shell
    pip install -r requirements.txt
    ```

## Passos para rodar a API

1. Iniciando o servidor local:

    ```shell
    python manage.py migrate
    python manage.py runserver
    ```

2. Crie um superusuário para acessar a API e gerar um token de acesso:

    ```shell
    python manage.py createsuperuser
    ```

3. Realize a validação do Token em:
    ```shell
    http://127.0.0.1:8000/api/v1/token/
    ```

4. Acesse com o Token a URL 127.0.0.1:8000/api/v1/ para verificar as APIs de marcas e models de carros com uma ferramenta de validação para APIs, como o Postman.
