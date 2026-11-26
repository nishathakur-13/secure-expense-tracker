from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
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


@login_required
def expense_edit(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, owner=request.user)
    if request.method == "POST":
        expense.description = request.POST["description"]
        expense.amount = request.POST["amount"]
        expense.category = request.POST["category"]
        expense.date = request.POST["date"]
        expense.save()
        return redirect("expense_list")
    return render(request, "expense_edit.html", {"expense": expense})


@login_required
def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, owner=request.user)
    if request.method == "POST":
        expense.delete()
    return redirect("expense_list")


@login_required
def expense_search(request):
    q = request.GET.get("q", "")
    expenses = Expense.objects.filter(owner=request.user).filter(
        Q(description__icontains=q) | Q(category__icontains=q)
    )
    total = expenses.aggregate(Sum("amount"))["amount__sum"]
    return render(request, "expense_list.html", {"expenses": expenses, "total": total, "q": q})