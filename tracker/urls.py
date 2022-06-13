from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("expenses", views.expenses, name="expenses"),
    path("expenses/<int:expense_id>", views.expense_details, name="expense"),
    path("expenses/add", views.add_expense, name="add_expense"),
    path("incomes", views.incomes, name="incomes"),
    path("incomes/<int:income_id>", views.income_details, name="income"),
    path("incomes/add", views.add_income, name="add_income"),
    path("edit_incomes/<int:income_id>", views.edit_income, name="edit_income"),
    path("edit_expense/<int:expense_id>", views.edit_expense, name="edit_expense"),
    path("delete_incomes/<int:income_id>", views.delete_income, name="delete_income"),
    path(
        "delete_expense/<int:expense_id>", views.delete_expense, name="delete_expense"
    ),
]
