from django.conf.urls import patterns, url

from reports import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map_list, name='map_list'),
)
