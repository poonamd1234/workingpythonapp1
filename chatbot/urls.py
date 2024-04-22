from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.chatbot, name = 'chatbot'),
    path('custom_login', views.custom_login, name = 'custom_login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
]
