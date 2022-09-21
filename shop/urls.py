from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.startPage),
    path('item/<int:id>/',views.getItem, name='item_url'),
    path('shop/',views.getItems),
    path('users/',views.getUsers),
    path('user/<int:id>/',views.getUser, name='user_url'),
]
