from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def home_view(request):
    return render(request, 'weather/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'weather/signup.html', {'form': form})

@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        location = request.POST.get('preferred_location')
        temperature_unit = request.POST.get('preferred_temperature_unit')
        user_profile.preferred_location = location
        user_profile.preferred_temperature_unit = temperature_unit
        user_profile.save()
        return redirect('profile')
    return render(request, 'weather/profile.html', {'user_profile': user_profile})
