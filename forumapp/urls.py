from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.thread_list, name='thread_list'),
    url(r'^thread/new/$', views.thread_new, name='thread_new'),
    url(r'^thread/(?P<pk>\d+)/$', views.thread, name='thread'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^thread/(?P<pk>\d+)/post/new/$', views.post_new, name='post_new'),
    url(r'^thread/(?P<th_pk>\d+)/post/delete/(?P<pk>\d+)$', views.delete_post, name='delete_post'),
]