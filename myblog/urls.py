from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls')),
    url(r'^blog/', include('blog.urls', namespace = 'blog')),
    url(r'^comments/',include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
