
from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login),
    url(r'^authin/', views.authin),
    url(r'^index/', views.index),
    url(r'^idc/', views.idc),
    url(r'^addidc/', views.addidc),
    #url(r'^mac/', views.mac),
]
