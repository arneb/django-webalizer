from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(.*)$', 'webalizer.views.proxy', name='webalizer_proxy'),
)