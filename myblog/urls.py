from django.conf.urls import url, include
from django.contrib import admin
from apps.core.views import index as site_index


urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', site_index, name="index"),
    url(r'^userinfo/', include('apps.userinfo.urls')),
    url(r'^core/', include('apps.core.urls')),    

    #blog
    url(r'^blog/', include('apps.blog.core.urls')),
    url(r'^article/', include('apps.blog.article.urls')),
    url(r'^comment/', include('apps.blog.comment.urls')),
]
