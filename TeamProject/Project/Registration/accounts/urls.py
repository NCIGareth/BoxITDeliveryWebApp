

from django.urls import path
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("accounts/register", views.register, name="register"),
    path("accounts/login",views.login, name="login"),
    path("accounts/become",views.become, name="become")
    ]
