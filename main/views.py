from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, name):
    # ls = ToDoList.objects.get(id=id)
    ls = ToDoList.objects.get(name=name)
    # return HttpResponse("<h1>tech with tim!</h1>")
    # return HttpResponse("<h1>%s</h1>" % id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

def v1(response):
    return HttpResponse("<h1>view 1</h1>")

def home(response):
    pass