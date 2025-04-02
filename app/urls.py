from django.contrib import admin
from django.urls import path
from manage import index, search_books, loan_book, list_loans, renew_loan, return_loan



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('search/', search_books, name='search_books'),
    path('loan/', loan_book, name='loan_book'),
    path('loans/', list_loans, name='list_loans'),
    path('renew/<int:loan_id>/', renew_loan, name='renew_loan'),
    path('return/', return_loan, name='return_loan'),
]
