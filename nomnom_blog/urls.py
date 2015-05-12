from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'nomnom_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # WYSIWYG editor
    (r'^tinymce/', include('tinymce.urls')),

    # base url, no pages clicked
    url(r'^', include('blog.urls')),
]
