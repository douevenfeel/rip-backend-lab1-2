from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Items

# def getItems(request):
#     return render(request, 'items.html',{'data':{
#         'date':date.today(),
#         'items':[
#             {'id':1, 'title':'Iphone 11', 'price': 49900},
#             {'id':2, 'title':'Iphone 12', 'price': 54900},
#             {'id':3, 'title':'Iphone 13', 'price': 59900},
#         ]
#     }})

# def getItem(request, id, title = 'none', price = 0):
#     return render(request,'itemInfo.html',{'data':{
#         'date': date.today(),
#         'id': id,
#         'title': title,
#         'price': price
#     }})

def getItems(request):
    return render(request, 'items.html',{'data':{
        'date':date.today(),
        'items':Items.objects.all()
    }})

def getItem(request, id, title = 'none', price = 0):
    return render(request,'itemInfo.html',{'data':{
        'date': date.today(),
        'item':Items.objects.filter(id=id)[0]
    }})
