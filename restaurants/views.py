from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse


from .models import Restaurant

def index(request):
	latest_restaurant_list = Restaurant.objects.order_by('name')[:5]
	context = {'latest_restaurant_list': latest_restaurant_list}
	return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	return render(request, 'restaurants/detail.html', {'restaurant': restaurant})

def results(request, restaurant_id):
	response = "You're looking at the results of restaurant %s."
	return HttpResponse(response % restaurant_id)

def vote(request, restaurant_id):
	return HttpResponse("You're voting on restaurant %s." % restaurant_id)