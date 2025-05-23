import datetime
import requests
import datetime

from db import add_loan, get_loans, update_loan, delete_loan_by_id, delete_loan_by_title
from time import sleep


def create_loan(title: str, link: str) -> None:
    """Cria um empréstimo com link do livro"""
    due_date = datetime.datetime.now() + datetime.timedelta(weeks=1)
    loan = {"title": title, "due_date": due_date, "id": None, "link": link}
    add_loan(loan)


def list_loans():
    return get_loans()


def renew_loan(loan_id:int=None) -> None:
    """ Verifica se e um novo ou ja existe loan "linha" para inserir na tabela ou dar update

    Parameters
    ----------
    loan_id : int, optional
        ID da linha, by default None
    """
    loans = get_loans()

    try:
        loan_id = int(loan_id)
    except ValueError:
        return
    
    loan = next((l for l in loans if l["id"] == loan_id), None)
    if loan:
        new_due_date = datetime.datetime.now() + datetime.timedelta(weeks=1)
        loan['due_date'] = new_due_date
        update_loan(loan)


def fetch_books(query: str) -> list:
    """Busca livros usando a API do Open Library com links."""
    url = f"http://openlibrary.org/search.json?q={query}"
    sleep(1)
    response = requests.get(url, verify=False, timeout=15)
    
    if response.status_code == 200:
        data = response.json()
        books = []
        
        for doc in data.get("docs", [])[:10]:
            # Extrai identificadores para links
            olid = doc.get("key", "").split("/")[-1]  # ID único do Open Library
            ia_identifier = doc.get("ia", [""])[0]  # Identificador do Internet Archive
            
            # Monta os links
            read_link = (
                f"https://archive.org/details/{ia_identifier}" 
                if ia_identifier 
                else f"https://openlibrary.org/works/{olid}/read"
            )
            
            books.append({
                "title": doc.get("title", "Sem título"),
                "author": doc.get("author_name", ["Desconhecido"])[0],
                "link": read_link,
                "year": doc.get("first_publish_year", "N/A")
            })
        
        return books
    else:
        return []


def get_remaining_time(due_date):
    """Calcula o tempo restante até a data de vencimento."""

    if isinstance(due_date, str):
        due_date = datetime.datetime.fromisoformat(due_date)

    now = datetime.datetime.now()
    delta = due_date - now
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    return f"{days}d {hours}h {minutes}m"


def return_loan(title:str) -> None:
    delete_loan_by_title(title)


def return_loan(loan_id:int) -> None:
    delete_loan_by_id(loan_id)
