import datetime

from dal_sqlite import SqliteDal



db = SqliteDal(db_name='bibliotech.db', db_folder='database')

if not db.table_exists('loans'):
    create_table_query = """
    CREATE TABLE loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date DATETIME NOT NULL,
        link TEXT NOT NULL
    )
    """
    db.run_query(create_table_query)


def add_loan(loan_data: dict) -> None:
    """ Aciona linha na tabela loans no caso adiciona um loan rs

    Parameters
    ----------
    loan_data : dict
        Dicionario com dados a ser inseridos
    """
    query = "INSERT INTO loans (title, due_date, link) VALUES (?, ?, ?)"
    parameters = (loan_data["title"], loan_data["due_date"].isoformat(), loan_data["link"])
    db.run_query(query, parameters)


def get_loans() -> dict:
    """ Faz a leitura da tabela loans

    Returns
    -------
    dict
        Retorna um dicionario com os dados da tabela loans
    """
    query = "SELECT id, title, due_date, link FROM loans"
    result = db.run_query(query)
    return [{
        "id": row[0],
        "title": row[1],
        "due_date": datetime.datetime.fromisoformat(row[2]),
        "link": row[3]
    } for row in result]


def update_loan(loan_data:dict) -> None:
    """ Atualiza a data da tabela loans

    Parameters
    ----------
    loan_data : dict
        Dicionario com nova data para atualizar na tabela loans
    """
    query = "UPDATE loans SET due_date = ? WHERE id = ?"
    parameters = (loan_data["due_date"].isoformat(), loan_data["id"])
    db.run_query(query, parameters)


def delete_loan_by_title(title:str) -> None:
    """ Deleta um loan da tabela de acordo com a coluna title

    Parameters
    ----------
    title : str
        Titulo para poder filtrar no delete da linha
    """
    query = "DELETE FROM loans WHERE title = ?"
    parameters = (title,)
    db.run_query(query, parameters)


def delete_loan_by_id(loan_id:int) -> None:
    """ Deleta um loan da tabela de acordo com a coluna id

    Parameters
    ----------
    loan_id : int
        ID para poder filtrar no delete da linha
    """
    query = "DELETE FROM loans WHERE id = ?"
    parameters = (loan_id,)
    db.run_query(query, parameters)
