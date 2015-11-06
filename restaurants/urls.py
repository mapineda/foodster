from django.conf.urls import url

from . import views

urlpatterns = [
# ex: /restaurants/
	url(r'^$', views.index, name='index'),
# ex: /restaurants/1	
	url(r'^(?P<restaurant_id>[0-9]+)/$', views.detail, name="detail"),
# ex: /restaurants/1/results/
	url(r'^(?P<restaurant_id>[0-9]+)/results/$', views.results, name="results"),
# ex: /restaurants/1/vote/
	url(r'^(?P<restaurant_id>[0-9]+)/vote/$', views.vote, name="vote"),		
]