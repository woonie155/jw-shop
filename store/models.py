from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200)  
  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=200)
  price = models.FloatField()
  digital = models.BooleanField(default=False, null=True, blank=True)
  image = models.ImageField(null=True, blank=True)
  
class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  dated_ordered = models.DateTimeField(default=False, null=True, blank=True)
  comlete = models.BooleanField(default=False)
  transation_id = models.CharField(max_length=200, null=True)

  def __str__(self):
    return str(self.id)

class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  dated_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
  address = models.CharField(max_length=200, null=True)
  city = models.CharField(max_length=200, null=True)
  state = models.CharField(max_length=200, null=True)
  zipcode = models.CharField(max_length=200, null=True)
  dated_added = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.address
