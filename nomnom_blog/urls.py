from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'nomnom_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),

    # base url, no pages clicked
    url(r'^', include('blog.urls')),
	#url(r'^comments/', include('django_comments.urls')),
]
