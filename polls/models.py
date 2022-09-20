from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'rip'
        db_table = 'items'
