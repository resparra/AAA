from django.conf.urls import patterns, url


urlpatterns = patterns('snippets.views',
    url(r'^api/$', 'report_list'),
    url(r'^api/(?P<pk>[0-9]+)/$', 'report_detail'),
)
