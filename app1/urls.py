from app1.views import *
from django.urls import path
app_name='Happy'


urlpatterns=[
    path('abc/',abc,name='abc'),
    path('virat/',virat,name='virat'),
]