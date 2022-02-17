from django.urls import path
from .views import *

urlpatterns=[
path('',Home,name='home'),
path('list/',Display,name='list'),
path('contact/',Contact,name='contact'),
]
