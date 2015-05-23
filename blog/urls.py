from django.conf.urls import url
from blog import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    # Any page that has a number
    url(r'^(?P<page>[1-9][0-9]*)/$', views.index),
    url(r'^post/', views.post),
]
