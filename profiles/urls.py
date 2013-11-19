from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
    url(r'^$', views.index_login, name='index_login'),
    url(r'^logout/$', views.logout_view, name='logout_view')
)