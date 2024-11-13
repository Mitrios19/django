# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profile_view, change_username, change_password

app_name = "user"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/change-username/', change_username, name='change_username'),
    path('profile/change-password/', change_password, name='change_password'),
]