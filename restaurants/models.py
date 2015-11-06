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
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def __str__(self):
    	test = self.name + " " + self.address
    	return test

class Favorite(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    favorite_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.favorite_text