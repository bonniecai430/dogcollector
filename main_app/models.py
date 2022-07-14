from django.db import models
from django.urls import reverse


# Create your models here.
class Dog(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    age=models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'dog_id':self.id})    




class Bid(models.Model):
    customer=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateField('bidding date')

    dog=models.ForeignKey(Dog,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} bid {self.price} on {self.date}"


class Meta:
    ordering = ['-date']