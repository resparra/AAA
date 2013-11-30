from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
    url(r'^$', views.index_login, name='index_login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^supervisor/$', views.supervisor_view, name='supervisor_view'),
    url(r'^employee/$', views.employee_view, name='employee_view'),
    url(r'^register/$', views.register, name='register_view'),

)