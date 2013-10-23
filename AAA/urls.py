from django.conf.urls import patterns, include, url
from reports import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AAA.views.home', name='home'),
    # url(r'^AAA/', include('AAA.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^reports/', include('reports.urls')),
<<<<<<< HEAD
=======
    #url(r'^grappelli/', include('grappelli.urls')),
>>>>>>> 32460bbd876a6c690e9b0e224de82f43ffd433c4
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^$', views.index, name='index'),
)
