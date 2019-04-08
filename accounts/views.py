from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:userhome')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def user_homepage(request):
    return render(request, 'accounts/userhome.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('accounts:userhome')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def user_homepage(request):
    username = request.user
    context = {
        "Uname": username
    }
    return render(request, 'accounts/userhome.html', context)
