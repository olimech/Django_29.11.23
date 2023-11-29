from django.urls import path
from . import views


urlpatterns = [
    path("user/<str:name>/<int:age>", views.index, name="home"), #http://127.0.0.1:8000/app/user/name'
    path("user/<str:name>", views.index, name="home"),
    path("user", views.index, name="home"),
]