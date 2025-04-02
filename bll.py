import datetime
import requests
import datetime

from db import add_loan, get_loans, update_loan
from db import delete_loan_by_title


def create_loan(title):
    due_date = datetime.datetime.now() + datetime.timedelta(weeks=1)
    loan = {"title": title, "due_date": due_date, "id": None}
    add_loan(loan)


def list_loans():
    return get_loans()


def renew_loan(loan_id):
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


def fetch_books(query):
    """Busca livros usando a API do Open Library."""
    url = f"http://openlibrary.org/search.json?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        books = [{"title": doc.get("title", "Sem título")} for doc in data.get("docs", [])[:10]]
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


def return_loan(title):
    delete_loan_by_title(title)