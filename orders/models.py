from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=64)
    small = models.FloatField(null=True)
    large = models.FloatField(null=True)
    type = models.CharField(max_length=64,default=None)
    def __str__(self):
        return f"{self.name},'small'-{self.small},'large'-{self.large}"

class toppings(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class pasta_salads(models.Model):
    n = models.CharField(max_length=64)
    price = models.FloatField(null=True)
    def __str__(self):
        return f"{self.n},{self.price}"

class base(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    topping = models.CharField(max_length=64, null=True)
    second_topping = models.CharField(max_length=64, null=True)
    third_topping = models.CharField(max_length=64, null=True)
    subs = models.CharField(max_length=64, null=True)
    pasta_salads = models.CharField(max_length=64, null=True)
    item_number = models.FloatField(null=True)
    p_s_number = models.FloatField(null=True)
    subs_number =models.FloatField(null=True)
    price =  models.FloatField(null=True)
    comment = models.CharField(max_length=64, null=True)
    user = models.CharField(max_length=64, null=True)
    class Meta:
        abstract = True
class plates(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"
class carts(base):
    mark = models.CharField(max_length=64, null=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.name},{self.type},{self.size},{self.topping},{self.second_topping},{self.third_topping},{self.subs},{self.pasta_salads},"
class orders(base):
    def __str__(self):
        return f"{self.name},{self.type},{self.size}"
