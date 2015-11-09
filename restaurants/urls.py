from django.conf.urls import url

from . import views

urlpatterns = [
# ex: /restaurants/
	url(r'^$', views.IndexView.as_view(), name='index'),
# ex: /restaurants/1	
	url(r'^specifics/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
# ex: /restaurants/1/results/
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
# ex: /restaurants/1/vote/
	url(r'^(?P<restaurant_id>[0-9]+)/vote/$', views.vote, name='vote'),
]