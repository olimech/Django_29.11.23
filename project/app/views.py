from django.shortcuts import render
from django.http import HttpResponse


def index(request, name="Bolly", age=10):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'host: {host} <br> browser {user_agent} <br> Path: {path} <br> user: {name} <br> age: {age}',
                        headers={'SecretCode': '1254478'},
                        status=400  # вывод вручную статус станицы
                        )