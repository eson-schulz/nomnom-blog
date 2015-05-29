from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'nomnom_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # WYSIWYG editor
    url(r'^tinymce/', include('tinymce.urls')),

    # base url, no pages clicked
    url(r'^', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "NomNom Administration"
admin.site.site_title = "NomNom admin"
