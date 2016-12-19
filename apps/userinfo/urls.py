from django.conf.urls import url, include

from views import register
from views import activate


urlpatterns = [
    url(r'^register$', register, name='user_register'),
    url(r'^activate/(?P<activate_code>\w+)', activate, name='activate'),
]
