from django.conf.urls import url, include
from django.contrib import admin

from test_app import urls as name_urls
from test_app import views

urlpatterns = [url(r'^admin/', include(admin.site.urls)),
               url(r'^name/', include(name_urls, namespace='name')),
               url(r'^main/', views.main, name='main'),
               url(r'', views.index, name='')]


