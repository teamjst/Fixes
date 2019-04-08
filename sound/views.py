from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login")
def sound_view(request):
    return render(request, 'sound/sound.html')
