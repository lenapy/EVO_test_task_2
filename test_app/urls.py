from django.conf.urls import url

from test_app import views

urlpatterns = [url(r'^add/$', views.add_name, name='add'),
               url(r'^del/$', views.delete_name, name='del'),
               url(r'^get_random_names/$', views.get_random_names, name='get_random_names')
               ]
