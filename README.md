# Bibliotech
    Lib engine


    django-admin startproject app .
    python manage.py migrate
    python manage.py runserver


no MYSQL :
CREATE DATABASE IF NOT EXISTS room;
USE room;



flyctl proxy 13306:3306 -a bibliotech


Cadastro de empréstimo de livro - "como se fosse uma biblioteca"


Fontes utilizadas:
	ChatGPT -> Para estrutura do código e estilização do README.md
	Deepseek -> Para a configuração correta do docker e toml para o fly.io
	stackoverflow -> Para duvidas sobre instalação do MySQL, validação de "rotas" endpoints Django.


Tecnologias utilizadas:
	Python -> Back end, logica do projeto.
	Django -> Framework web para endpoints.
	HTML, CSS -> Estilização do front end.
	MYSQL -> Banco de dados, criei um cloud em my sql no FLY.IO
	sqlalchemy -> Utilizado para manipulação do banco e conexão.
	Requests -> API "openlibrary" para ter insumo de títulos.
	Docker -> Para configuração do deploy no fly.io
	requirements -> Para listar as libs, e para o deploy funcionar corretamente ele e necessário na estrutura.
    