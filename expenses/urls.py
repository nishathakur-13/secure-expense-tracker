from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]