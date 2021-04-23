

from django.urls import path
from django.conf.urls.static import static


from . import views

urlpatterns = [
     path("", views.index, name="index"),

    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("route", views.route, name="route"),
	path("map", views.map, name="map"),
    path("become",views.become, name="become")
    ]

