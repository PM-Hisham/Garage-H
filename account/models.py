from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.

class Services(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    description=models.CharField(max_length=300)
    rating=models.IntegerField(default='5')



class Book(models.Model):
    services=models.ForeignKey(Services,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    fuel_type=models.CharField(max_length=100)
    date=models.DateField(null=True)
    options=(
        ('8:00 am - 10:00 am','8:00 am - 10:00 am'),
        ('10:00 am - 12:00 pm','10:00 am - 12:00 pm'),
        ('12:00 am - 2:00 pm','12:00 am - 2:00 pm'),
        ('3:00 am - 5:00 pm','3:00 am - 5:00 pm'),
        ('5:00 am - 7:00 pm','5:00 am - 7:00 pm'),
    )
    timeslot=models.CharField(max_length=300,choices=options,default='8:00 am - 10:00 am')
   




