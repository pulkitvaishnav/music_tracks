from django.conf.urls import url

from . import views

app_name = 'Track'
urlpatterns = [
	# music track listing
    url(r'^tracks/$', views.track_list, name='track_list'),
    # track details
    url(r'^track/(?P<track_id>[0-9]+)/$', views.track_detail, name='track_detail'),
    # genre listing
    url(r'^genres/$', views.genre_list, name='genre_list'),
    # genre detail
    url(r'^genre/(?P<genres_id>[0-9]+)/$', views.genre_detail, name='genre_detail'),
    # add track
    url(r'^track/add/$', views.add_track, name='tracks-add'),
    # add genre
    url(r'^genre/add/$', views.add_genres, name='genres-add'),
    # edit track
    url(r'^track/(?P<pk>[0-9]+)/edit/$', views.add_track, name='tracks-edit'),
]