# Rebeca

Uma aplicação Django para coleta de dados socioeconômicos de usuários da rede pública de saúde

## Instalação local: 

Clone o repositório:

`$ git clone https://github.com/rodrigowmendes/rebeca.git`

Mude de diretório:

`$ cd rebeca`


Suba a aplicação usando docker-compose (necessário ter o Docker e o docker-compose instalados):

`$ sudo docker-compose up -d`


Crie o banco de dados:

`$ sudo docker-compose run web python3 manage.py migrate` 


Crie um superusuário:

`$ sudo docker-compose run web python3 manage.py createsuperuser`  

