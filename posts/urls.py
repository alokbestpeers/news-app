from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news/(?P<pk>\d+)/$', views.news, name='news'),
]