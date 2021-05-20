from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=200, null=True)
    description= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.shop_name

class Product(models.Model):
    CATEGORY = (
        ('בגדים לגבר', 'בגדים לגבר'),
        ('נעליים גברים', 'נעליים גברים'),
        ('בגדים לאישה', 'בגדים לאישה'),
        ('נעליים נשים', 'נעליים נשים'),
        ('אקססוריז', 'אקססוריז'),
    )
    SIZE = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True, choices=SIZE)
