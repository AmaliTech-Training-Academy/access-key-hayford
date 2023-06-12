from django.urls import path
from .views import *
from django.urls import reverse_lazy

app_name ='management'

urlpatterns = [
    path('feedback/', ListView.as_view(), name='key_list'),
    path('<str:pk>/generate', generate_key, name='generate_key'),
    path('<str:pk>/update', update_key, name='update_key'),
    path('<str:pk>/revoke', revoke_key, name='revoke_key'),
    path('api/', AccessKeyViewAPI.as_view(), name='access_key_view_api'),
    #school_view
    path('school/', school_dashboard, name='school'),
    #Request
    path('<int:pk>/request/',key_request, name='key_request'),
    #acess_key_list
    path('<int:pk>/list/', School_key_view, name='school_key_view'),
]