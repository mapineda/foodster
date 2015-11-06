from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)
    menu_url = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    search_fields = ['name']
    def __str__(self):
    	test = self.name + " " + self.address
    	return test

class Favorite(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    favorite_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.favorite_text