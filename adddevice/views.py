from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login")
def adddevice_view(request):
    return render(request, 'adddevice/adddevice.html')
