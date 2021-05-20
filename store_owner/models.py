from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=200, null=True)
    description= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.shop_name
