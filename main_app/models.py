from django.db import models
from django.urls import reverse


# Create your models here.


class Sport(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sports_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    age=models.IntegerField()

    sports=models.ManyToManyField(Sport)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'dog_id':self.id})    




class Bid(models.Model):
    customer=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateField('bidding date')

    dog=models.ForeignKey(Dog,on_delete=models.CASCADE)

    class Meta:
      ordering = ['-date']

    def __str__(self):
        return f"{self.customer} bid {self.price} on {self.date}"

