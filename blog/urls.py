from django.conf.urls import url
from blog import views

urlpatterns = [

	# Base url
	url(r'^$', views.index, name='index'),
	# Contact page
	url(r'^contact/$', views.contact, name='contact'),
	# Main blog page
    url(r'^blog/$', views.blog, name='blog'),
    # Static about page
    url(r'^about/$', views.about, name='about'),
    # Specific post
    url(r'^blog/post/(?P<post_slug>[\w\-]+)/$', views.post, name='post'),
]
