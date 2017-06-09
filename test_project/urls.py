from django.conf.urls import url, include
from django.contrib import admin

from test_app import urls as name_urls

urlpatterns = [url(r'^admin/', include(admin.site.urls)),
               url(r'^name/', include(name_urls, namespace='name'))]
