from django.contrib.auth.models import AbstractUser
from django.db import models

# # Inherits from django's AbstractUser model
class User(AbstractUser):
    # unique email
    email = models.EmailField(unique = True)
    # unique Username
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    # Date of birth
    DOB = models.DateField(null=True)
    # Profile picture
    image = models.ImageField(null=True)



    def __str__(self):
        return self.username

class Item(models.Model):
    # name
    name = models.CharField(max_length=50)
    # description
    desc = models.CharField(max_length=500)
    # Start time
    start_time = models.DateTimeField()
    # End time
    end_time = models.DateTimeField()
    # starting price
    start_price = models.DecimalField(max_digits= 8, decimal_places= 2)
    #current bid
    cur_price = models.DecimalField(max_digits= 8, decimal_places= 2)
    #image of item
    image = models.ImageField()
    #seller of item
    seller = models.ForeignKey(User, on_delete = models.CASCADE )



    def __str__ (self):
        return self.name

    def newBid(self, value):
        cur_price = value

# class Listings(models.Model):

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    asker = models.ForeignKey(User, on_delete= models.SET('Deleted User'))
    #item the question is for
    item = models.ForeignKey(Item, on_delete = models.CASCADE )

    def __str__(self):
        return self.question

    def newAnswer(self, value):
        answer = value
