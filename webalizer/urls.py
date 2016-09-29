from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(.*)$', 'webalizer.views.proxy', name='webalizer_proxy'),
)
