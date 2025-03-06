from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.urls import path , include
from accounts.forms import UserLoginForm
from accounts import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]