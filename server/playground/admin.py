from django.contrib import admin
from django.http import HttpResponse
# Register your models here.


def say_hello(request):
    return HttpResponse('Hello world ')