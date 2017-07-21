from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.track, name='tracks'),
    url(r'track/add/$', views.add_track, name='tracks-add'),
    url(r'genre/add/$', views.add_genres, name='genres-add')
]