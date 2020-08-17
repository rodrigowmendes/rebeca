# Dados Sociais

Uma aplicação Django para coleta de dados socioeconômicos de usuários da rede pública de saúde

## Instalação local: 

Clone o repositório:

`$ git clone https://github.com/rodrigowmendes/dados-sociais.git`

Mude de diretório:

`$ cd dados-sociais`


Crie seu ambinente virtual:

`$ python3 -m virtualenv venv`

Ative-o:

`$ source /venv/bin/activate`


Instale as dependências:

`$ pip3 install -r requirements.txt`


Crie o arquivo para as variáveis de ambiente:

`$ cp .env.example .env`


Crie o banco de dados (necessário ter o PostgreSQL instalado localmente):

`$ python3 manage.py migrate` 


Crie um superusuário:

`$ python3 manage.py createsuperuser`  

