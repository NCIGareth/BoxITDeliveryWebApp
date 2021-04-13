

from django.urls import path
from django.conf.urls.static import static


from . import views

urlpatterns = [
     path("", views.index, name="index"),

    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("become",views.become, name="become")
    ]

