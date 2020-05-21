from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from attendFellowship import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^new_family/', views.new_family, name='new_family'),
    url(r'^show_up/(\w)/', views.show_up, name='show_up'),
    url(r'^intermediate_record/', views.intermediate_record, name='intermediate_record'),
    url(r'^reset_record/', views.reset_record, name='reset_record'),
]
