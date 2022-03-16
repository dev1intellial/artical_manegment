from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('register',views.register,name='register'),
    path('logut',views.logout_view,name='logout')
]