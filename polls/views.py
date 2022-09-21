from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Items, Users, Baskets, Roles

def startPage(request):
    return render(request, 'startPage.html', {'data':{
        'date':date.today()
    }})

def getItems(request):
    return render(request, 'items.html',{'data':{
        'date':date.today(),
        'items':Items.objects.all()
    }})

def getItem(request, id):
    return render(request,'itemInfo.html',{'data':{
        'date': date.today(),
        'item':Items.objects.filter(id=id)[0]
    }})

def getUsers(request):
    return render(request, 'users.html',{'data':{
        'date':date.today(),
        'users':Users.objects.all()
    }})

def getUser(request, id):
    return render(request,'userInfo.html',{'data':{
        'date': date.today(),
        'user':Users.objects.filter(id=id)[0],
        'basket': Baskets.objects.filter(user=id),
        'role': Roles.objects.filter(id=id)[0]
    }})
