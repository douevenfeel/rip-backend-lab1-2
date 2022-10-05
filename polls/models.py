from pyexpat import model
from django.db import models

# Create your models here.
class Baskets(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, db_column='item', verbose_name="Устройство")
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user', verbose_name="Пользователь")

    def __str__(self):
        return f'{self.user}'

    class Meta:
        managed = False
        app_label = 'polls'
        db_table = 'baskets'
        verbose_name = 'Корзина'
        verbose_name_plural = "Корзины"
class Items(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    price = models.IntegerField(verbose_name="Стоимость")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = False
        app_label = 'polls'
        db_table = 'items'
        verbose_name = 'Устройство'
        verbose_name_plural = "Устройства"


class Roles(models.Model):
    title = models.CharField(max_length=30, verbose_name="Роль")

    def __str__(self):
        return f'{self.title}'
    class Meta:
        managed = False
        app_label = 'polls'
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = "Роли"

        
class Users(models.Model):
    username = models.CharField(max_length=30, verbose_name="Имя пользователя")
    password = models.CharField(max_length=30, verbose_name="Пароль пользователя")
    role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='role', verbose_name="Роль")

    def __str__(self):
        return f'{self.username}'
    class Meta:
        managed = False
        app_label = 'polls'
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
