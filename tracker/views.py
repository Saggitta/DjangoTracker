from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .api.exchange_rate import exchange
from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income


def index(request):
    latest_expense_list = Expense.objects.order_by("-date")[:5]
    latest_income_list = Income.objects.order_by("-date")[:5]

    total_received_usd = sum(
        income.amount for income in Income.objects.filter(currency="USD")
    )
    total_received_uah = sum(
        income.amount for income in Income.objects.filter(currency="UAH")
    )

    total_spent_usd = sum(
        expense.amount for expense in Expense.objects.filter(currency="USD")
    )
    total_spent_uah = sum(
        expense.amount for expense in Expense.objects.filter(currency="UAH")
    )

    total_spent = total_spent_uah + exchange(total_spent_usd)
    total_received = total_received_uah + exchange(total_received_usd)

    current_balance_uah = total_received_uah - total_spent_uah
    current_balance_usd = total_received_usd - total_spent_usd

    total_balance_uah = exchange(current_balance_usd) + current_balance_uah
    total_balance_usd = exchange(current_balance_uah, "UAH", "USD") + float(
        current_balance_usd
    )

    usd = exchange(1)
    eur = exchange(1, base="EUR")

    context = {
        "latest_expenses_list": latest_expense_list,
        "latest_income_list": latest_income_list,
        "total_spent": total_spent,
        "total_received": total_received,
        "current_balance_uah": current_balance_uah,
        "current_balance_usd": current_balance_usd,
        "total_balance_uah": total_balance_uah,
        "total_balance_usd": total_balance_usd,
        "usd": usd,
        "eur": eur,
    }
    return render(request, "index.html", context)


def expenses(request):
    all_expenses = Expense.objects.all()
    return render(request, "expenses.html", {"all_expenses": all_expenses})


def incomes(request):
    all_incomes = Income.objects.all()
    return render(request, "incomes.html", {"all_incomes": all_incomes})


def expense_details(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, "expense_details.html", {"expense": expense})


def income_details(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    return render(request, "income_details.html", {"income": income})


def add_expense(request):
    submitted = False
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense Added")
            return HttpResponseRedirect("add")
        else:
            messages.success(request, "Contact request submitted successfully.")
            messages.error(request, form.errors)
    else:
        form = ExpenseForm

    return render(request, "add_expense.html", {"form": form, "submitted": submitted})


def add_income(request):
    submitted = False
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Income Added")
            return HttpResponseRedirect("add")
        else:
            messages.success(request, "Contact request submitted successfully.")
            messages.error(request, form.errors)
    else:
        form = IncomeForm
    return render(request, "add_income.html", {"form": form, "submitted": submitted})


def edit_income(request, income_id):
    income = Income.objects.get(pk=income_id)
    form = IncomeForm(request.POST or None, instance=income)
    if form.is_valid():
        form.save()
        messages.success(request, "Income Updated")
        return redirect("incomes")
    return render(request, "edit_income.html", {"income": income, "form": form})


def edit_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        messages.success(request, "Expense Updated")
        return redirect("expenses")
    return render(request, "edit_expense.html", {"expense": expense, "form": form})


def delete_income(request, income_id):
    income = Income.objects.get(pk=income_id)
    income.delete()
    return redirect("incomes")


def delete_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    expense.delete()
    return redirect("expenses")
