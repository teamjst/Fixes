from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adddevice.models import AddDevice
from yeelight import Bulb, discover_bulbs
import datetime

# Create your views here.
@login_required(login_url="/accounts/login")
def timer_view(request):
    user = request.user
    ip = AddDevice.objects.filter(owner=user).first().ip
    bulb = Bulb(ip)
    startpause = False
    if request.GET.get('timerstart'):
        timeone = request.GET.get('timepicker-one')
        timetwo = request.GET.get('timepicker-two')
        print(timetwo)
        def delZero(time):
            intver = int(time[0])
            print(time[1])
            if intver < 9 and time[1] is " ":
                return "0" + time
            else:
                return time
        timeone = delZero(timeone)
        timetwo = delZero(timetwo)
        print(timetwo)
        while timetwo != datetime.datetime.now().strftime("%I : %M %p"):
            if timeone == datetime.datetime.now().strftime("%I : %M %p") and startpause is False:
                bulb.turn_on()
                startpause = True
        bulb.turn_off()
    return render(request, 'timer/timer.html')
