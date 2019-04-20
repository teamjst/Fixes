from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login")
def adddevice_view(request):
    if request.method == 'POST':
        form = forms.AddNewDevice(request.POST)
        if form.is_valid():
            #save article db
            return render(request, 'adddevice/adddevice.html')
    else:
        form = forms.AddNewDevice()
    return render(request, 'adddevice/adddevice.html', {'form':form})
