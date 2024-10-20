from django.urls import path
from . import views

urlpatterns = [
    path('user_form/', views.user_form, name='user_form'),
     
    path('success/', views.success, name='success'),
]

