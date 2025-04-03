# 📚 Bibliotech - Sistema de Gerenciamento de Biblioteca

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![OpenLibrary API](https://img.shields.io/badge/OpenLibrary_API-FF6F00?style=for-the-badge&logo=book&logoColor=white)](https://openlibrary.org/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Fly.io](https://img.shields.io/badge/Fly.io-7B2CBF?style=for-the-badge&logo=fly&logoColor=white)](https://fly.io/)

Sistema de gerenciamento de biblioteca desenvolvido com Django para controle eficiente de empréstimos de livros.

## ✨ Funcionalidades

- 📖 Sistema de registro de empréstimos de livros
- 🌐 Integração com API da OpenLibrary
- 🔄 Suporte a múltiplos bancos de dados (SQLite/MySQL)
	  por conta de acessos ao MySQL tive que optar pelo SQLite.
- 🐳 Deploy containerizado com Docker
- 📱 Interface web responsiva -> Front-end desenvolvido por: https://github.com/vic-3PO
- 🔄 Migrações automatizadas


## 🛠️ Tecnologias Utilizadas

| Categoria        | Tecnologias                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Backend**      | Python 3, Django                                                            |
| **Frontend**     | HTML5, CSS3                                                                 |
| **Banco de Dados** | SQLite (Desenvolvimento), MySQL (So realizei teste pois gera cobrança)                                |
| **APIs**         | OpenLibrary API                                                             |
| **Deploy**       | Docker, Fly.io                                                              |                                                              |

## 🚀 Primeiros Passos

### Pré-requisitos
- Python 3.9+
- Docker (para containerização)
- Fly.io CLI (para deploy) -> Neste caso somente eu para servir.
- https://bibliotech-online.fly.dev/ -> Para acesso como user.

### Instalação
```bash
# Clonar repositório
git clone https://github.com/seuusuario/bibliotech.git
cd bibliotech

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar banco de dados
python manage.py migrate

# Iniciar
python manage.py runserver
```
