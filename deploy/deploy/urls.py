from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns