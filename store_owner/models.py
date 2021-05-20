from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=200, null=True)
    description= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.shop_name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('בטיפול', 'בטיפול'),
        ('בדרך ללקוח', 'בדרך ללקוח'),
        ('הגיע אל הלקוח', 'הגיע אל הלקוח'),
    )
    customer = models.ForeignKey(Customer,null=True, on_delete= models.SET_NULL)    #one to many relationship
    product = models.ForeignKey(Product,null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name

