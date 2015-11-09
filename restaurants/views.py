from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
# from django.http import HttpResponse

from .models import Restaurant, Favorite

class IndexView(generic.ListView):
	template_name = 'restaurants/index.html'
	context_object_name = 'latest_restaurant_list'

	def get_queryset(self):
		"""Return the last six published restaurants."""
		return Restaurant.objects.order_by('-name')[:6]

class DetailView(generic.DetailView):
	model = Restaurant
	template_name = 'restaurants/detail.html'

class ResultsView(generic.DetailView):
	model = Restaurant
	template_name = 'restaurants/results.html'

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

	