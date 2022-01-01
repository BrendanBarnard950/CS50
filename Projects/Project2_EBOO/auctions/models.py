from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.files import ImageField
from django.forms.fields import DateTimeField


class User(AbstractUser):
    wishlist = models.ManyToManyField('Listings')

class Catagories(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.name)
        

    
class Listings(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Catagories, on_delete=models.CASCADE)
    starting_bid = models.DecimalField(max_digits=9, decimal_places=2)
    date =  models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=100)
        
    def __str__(self):
        return str(self.title)
                              
                                  
class Bids(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
        
    def __str__(self):
        return str(self.bidder)

class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return str(self.commenter)
    
    
