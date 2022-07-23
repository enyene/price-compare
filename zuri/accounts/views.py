from django.shortcuts import render
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required

# Create your views here.

# landing page
def home(request):
    return render(request, 'accounts/home.html')

#login page
@unauthenticated_user
def user_login(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/login.html', context)


# register page
@unauthenticated_user
def register(request):
    return render(request, 'accounts/register.html')

# logout page
def logout(request):
    return render(request, 'accounts/logout.html')


 # profile page
@login_required(login_url='/')
def profile(request):
    return render(request, 'accounts/profile.html')