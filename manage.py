import os
import sys
import bll

from django.shortcuts import render, redirect



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# Rotas
def index(request):
    """Página inicial com links para as ações."""
    return render(request, 'index.html')


def search_books(request):
    query = request.GET.get('q', '')
    books = []
    if query:
        books_api = bll.fetch_books(query)
        loans = bll.list_loans()
        loaned_titles = {loan['title'] for loan in loans}
        
        # Adiciona status de empréstimo aos livros
        for book in books_api:
            book['is_loaned'] = book['title'] in loaned_titles
        
        books = books_api
    return render(request, 'search_books.html', {'books': books, 'query': query})


def loan_book(request):
    """View para criar um empréstimo de livro."""
    if request.method == 'POST':
        title = request.POST.get('title', '')
        if title:
            bll.create_loan(title)
            return redirect('list_loans')
    return render(request, 'loan_book.html')


def list_loans(request):
    """View para listar os empréstimos."""
    loans = bll.list_loans()
    return render(request, 'list_loans.html', {'loans': loans})


def renew_loan(request, loan_id):
    """View para renovar um empréstimo."""
    bll.renew_loan(loan_id)
    return redirect('list_loans')


def return_loan(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            bll.return_loan(title)
            return redirect('list_loans')
    return redirect('search_books')



if __name__ == '__main__':
    main()
