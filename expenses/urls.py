from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("<int:expense_id>/edit/", views.expense_edit, name="expense_edit"),
    path("add/", views.expense_add, name="expense_add"),
    path("", views.expense_list, name="expense_list"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("search/", views.expense_search, name="expense_search"),
    path("<int:expense_id>/delete/", views.expense_delete, name="expense_delete"),
]