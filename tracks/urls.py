from django.conf.urls import url

from . import views

app_name = 'Track'
urlpatterns = [
    url(r'^tracks/$', views.track_list, name='track_list'),
    url(r'^track/(?P<track_id>[0-9]+)/$', views.track_detail, name='track_detail'),
    url(r'^genres/$', views.genre_list, name='genre_list'),
    url(r'^genre/(?P<genres_id>[0-9]+)/$', views.genre_detail, name='genre_detail'),
    url(r'^track/add/$', views.add_track, name='tracks-add'),
    url(r'^genre/add/$', views.add_genres, name='genres-add'),
    url(r'^track/(?P<pk>[0-9]+)/edit/$', views.add_track, name='tracks-edit'),
]