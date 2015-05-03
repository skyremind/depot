
from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    def __unicode__(self):
        return u"%s %s %s" %(self.name,self.address,self.email)
    
class Product(models.Model):
    title          = models.CharField(max_length=100,unique=True)
    description     = models.TextField()
    image_url     = models.URLField(max_length=200)
    price          = models.DecimalField(max_digits=8,decimal_places=2)
    date_available = models.DateField()
    orders = models.ManyToManyField(Order,through='LineItem')
    def __unicode__(self):
        return u"%s %s %s %s" %(self.title,self.description,self.price,self.date_available)




class LineItem(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.IntegerField()
    def __unicode__(self):
        return u"%s %s %s %s" %(self.product,self.order,self.unit_price,self.quantity)
    
class Cart(object):
    def __init__(self, *args, **kwargs):
        self.items = []
        self.total_price = 0
    def add_product(self,product):
        self.total_price += product.price
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += 1 
                return
        self.items.append(LineItem(product=product,unit_price=product.price,quantity=1))
