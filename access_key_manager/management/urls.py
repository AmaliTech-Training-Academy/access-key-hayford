from django.urls import path
from .views import *

app_name ='management'

urlpatterns = [
    path('feedback/', ListView.as_view(), name='key_list'),
    path('generate/<str:pk>', generate_key, name='generate_key'),
    path('update/<str:pk>', update_key, name='update_key'),
    path('revoke/<str:pk>', revoke_key, name='revoke_key'),
    # path('---------/', --------, name=''),
]