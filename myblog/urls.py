"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.core.views import index as site_index
from apps.blog.block.views import index as block_index


urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', site_index, name="index"),
    url(r'^userinfo/', include('apps.userinfo.urls')),
    url(r'^core/', include('apps.core.urls')),    

    #blog
    url(r'^blog/', block_index, name='blog'),
    url(r'^article/', include('apps.blog.article.urls')),
    url(r'^comment/', include('apps.blog.comment.urls')),
]
