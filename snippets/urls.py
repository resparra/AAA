from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns('snippets.views',
    url(r'^api/$', 'report_list'),
    url(r'^api_mobile', 'mobile_news'),
    url(r'^api/(?P<pk>[0-9]+)/$', 'report_detail'),
    url(r'^api/(?P<pueblo>\w{0,50})/$', 'report_location'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^images/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))