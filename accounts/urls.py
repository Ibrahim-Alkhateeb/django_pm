from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.urls import path , include
from accounts.forms import UserLoginForm
from accounts import views
from accounts.views import RegisterView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', views.edit_profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
]