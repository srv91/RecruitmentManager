from django.conf.urls import patterns, url

from galaxy import views

urlpatterns = patterns('',
    url(r'^$', views.multiform, name='multiform'),
)


