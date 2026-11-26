from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Profile, Expense


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, plain_password=password)
        return redirect("login")
    return render(request, "register.html")


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(owner=request.user)
    total = expenses.aggregate(Sum("amount"))["amount__sum"]
    return render(request, "expense_list.html", {"expenses": expenses, "total": total})


@login_required
def expense_add(request):
    if request.method == "POST":
        Expense.objects.create(
            owner=request.user,
            description=request.POST["description"],
            amount=request.POST["amount"],
            category=request.POST["category"],
            date=request.POST["date"],
        )
        return redirect("expense_list")
    return render(request, "expense_form.html")