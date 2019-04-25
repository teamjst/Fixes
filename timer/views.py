from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adddevice.models import AddDevice
from yeelight import Bulb, discover_bulbs
import datetime

# Create your views here.
@login_required(login_url="/accounts/login")
def timer_view(request):
    user = request.user
    ip = AddDevice.objects.get(owner=user).ip
    bulb = Bulb(ip)
    startpause = False
    if request.GET.get('timerstart'):
        timeone = request.GET.get('timepicker-one')
        timetwo = request.GET.get('timepicker-two')
        def delZero(time):
            intver = int(time[0])
            if intver < 10:
                return "0" + time
            else:
                return time
        timeone = delZero(timeone)
        timetwo = delZero(timetwo)
        while timetwo != datetime.datetime.now().strftime("%I : %M %p"):
            if timeone == datetime.datetime.now().strftime("%I : %M %p") and startpause is False:
                bulb.turn_on()
                startpause = True
        bulb.turn_off()
    return render(request, 'timer/timer.html')
