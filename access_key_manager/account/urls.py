from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>', activate, name='activate'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('password_reset/', password_reset, name='reset_page'),
    path('password_reset/doine/', resetPageDone, name='reset_page_done'),
    path('reset/<uidb64>/<token>', reset_password_confirm, name='reset_password_confirm'),
]
