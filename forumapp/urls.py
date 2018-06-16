from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.thread_list, name='thread_list'),
    url('^thread/new/$', views.thread_new, name='thread_new'),
    url('^thread/(?P<pk>\d+)/$', views.thread, name='thread'),

]