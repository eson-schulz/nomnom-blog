from django.conf.urls import url
from blog import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    # Main index to link to other pages
    url(r'^/$', views.index),
    # Specific post
    url(r'^post/(?P<post_slug>[\w\-]+)/$', views.post),
]
