from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    return HttpResponse('hello') # это класс, который на вход принимает байт (строчка тоже подойдет).
    # Этот HttpResponse улетит пользователю, когда его запрос должна обработать функция hello_view


def index_view(request):
    return HttpResponse('Вы попали на главную страницу')