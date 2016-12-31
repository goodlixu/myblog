from django.conf.urls import url, include

from views import about_us, contact

urlpatterns = [
    url(r'^about_us$', about_us, name='about_us'),
    url(r'^contact$', contact, name='contact'),
]
