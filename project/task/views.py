from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META('HTTP_HOST')
    user_info = request.META('HTTP_USER_AGENT')
    ip_user = request.META('REMOTE_ADDR')

    return HttpResponse(f"Host: {host} <br> User: {user_info}, <br> IP: {ip_user}")


def error(request):
    return HttpResponse("К сожалению произошла ошибка", status=400, reason="Incorrect data")


def info_user(request, login='Vladislav', name_dir='Boock', num_post=10):
    return HttpResponse(f"Ваш логин: {login} <br> Имя вашей папки: {name_dir} <br> Номер поста: {num_post}")