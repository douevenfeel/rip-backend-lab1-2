from pyexpat import model
from django.db import models

# Create your models here.
class Baskets(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, db_column='item')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        app_label = 'rip'
        db_table = 'baskets'
class Items(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'rip'
        db_table = 'items'


class Roles(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        managed = False
        app_label = 'rip'
        db_table = 'roles'

        
class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='role')

    class Meta:
        managed = False
        app_label = 'rip'
        db_table = 'users'
