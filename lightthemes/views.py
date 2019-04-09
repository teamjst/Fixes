from django.shortcuts import render, redirect
from yeelight import Bulb
from yeelight import *
from django.contrib.auth.decorators import login_required

bulb = Bulb("192.168.0.10")

# Create your views here.
@login_required(login_url="/accounts/login")
def lighttheme_list(request):
    return render(request, 'lightthemes/lighttheme_list.html')

@login_required(login_url="/accounts/login")
def fire_theme(request):

    transitions = [
    TemperatureTransition(1700, duration=4000),
    TemperatureTransition(6500, duration=4000)
    ]

    flow = Flow(
    count=10,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def rain_theme(request):

    duration = 1000
    brightness = 100

    transitions = [
    RGBTransition(0, 0, 139, duration=duration, brightness=brightness),
    RGBTransition(65, 105, 255, duration=duration, brightness=brightness),
    RGBTransition(0, 0, 205, duration=duration, brightness=brightness),
    RGBTransition(65, 105, 255, duration=duration, brightness=brightness),
    RGBTransition(0, 0, 255, duration=duration, brightness=brightness),
    RGBTransition(65, 105, 255, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=5,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')
