from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page or any other page
