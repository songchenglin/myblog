from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$',views.blog_list,name = 'blog_list'),
    url(r'^detail/(?P<id>\d+)$',views.detail, name = 'detail'),
)
