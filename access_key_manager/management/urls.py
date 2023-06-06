from django.urls import path
from .views import *

app_name ='management'

urlpatterns = [
    path('redocs/', ListView.as_view(), name='key_list'),
]