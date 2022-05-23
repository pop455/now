from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from customer.views import Index, Order

urlpatterns = [
path('', Index.as_view(), name='index'),

path('order/', Order.as_view(), name='order'),
    ]