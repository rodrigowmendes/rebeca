# Rebeca

Uma aplicação Django para coleta de dados socioeconômicos

## Instalação: 

Clone o repositório:

`$ git clone https://github.com/rodrigowmendes/rebeca.git`

Mude de diretório:

`$ cd rebeca`

Altere a branch:

`$ git checkout develop`


Inicie a aplicação usando docker-compose (necessário ter o Docker e o docker-compose instalados):

`$ sudo docker-compose up`


Crie o banco de dados:

`$ sudo docker-compose run web python3 manage.py migrate` 


Crie um superusuário:

`$ sudo docker-compose run web python3 manage.py createsuperuser`  

