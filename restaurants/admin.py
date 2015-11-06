from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Favorite, Restaurant

class FavoriteInline(admin.TabularInline):
	model = Favorite
	extra = 3

class RestaurantAdmin(admin.ModelAdmin): 
  inlines = [FavoriteInline]
  list_display = ('name', 'address', 'logo_url', 'website_url', 'menu_url', 'description', 'pub_date')
  list_filter = ['pub_date']
  search_fields = ['name']

admin.site.register(Restaurant, RestaurantAdmin)