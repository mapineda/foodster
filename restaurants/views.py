from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
# from django.http import HttpResponse

from .models import Restaurant, Favorite

def index(request):
	latest_restaurant_list = Restaurant.objects.order_by('name')[:6]
	context = {'latest_restaurant_list': latest_restaurant_list}
	return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	return render(request, 'restaurants/detail.html', {'restaurant': restaurant})

def results(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	return render(request, 'restaurants/results.html', {'restaurant' : restaurant})

def vote(request, restaurant_id):
	r = get_object_or_404(Restaurant, pk=restaurant_id)
	try:
		selected_favorite = r.favorite_set.get(pk=request.POST['favorite'])
	except (KeyError, Favorite.DoesNotExist):
		# Redisplay the restaurant voting form.
		return render(request, 'restaurants/detail.html', {'restaurant': restaurant})
	else:
		selected_favorite.votes += 1
		selected_favorite.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with Post Data. This prevents data from being posted twice if a 
		#user hits the Back button
		return HttpResponseRedirect(reverse('restaurants/results', args=(r.id,)))	

	