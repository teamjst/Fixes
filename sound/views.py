from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import winsound

# Create your views here.
@login_required(login_url="/accounts/login")
def sound_view(request):
    if request.method == 'GET':
        option = request.GET.get('sounds')
        if option == 'Wind Blowing':
            winsound.PlaySound('sound/WavFiles/Wind.wav', winsound.SND_LOOP | winsound.SND_ASYNC)
        if option == 'Rain Drops':
            winsound.PlaySound('sound/WavFiles/Rain.wav', winsound.SND_LOOP | winsound.SND_ASYNC)
        if option == 'Fire Crackling':
            winsound.PlaySound('sound/WavFiles/Fire.wav', winsound.SND_LOOP | winsound.SND_ASYNC)
        if option == 'Birds Chirping':
            winsound.PlaySound('sound/WavFiles/Birds.wav', winsound.SND_LOOP | winsound.SND_ASYNC)
    return render(request, 'sound/sound.html')

