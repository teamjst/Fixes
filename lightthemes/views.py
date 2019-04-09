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
    RGBTransition(23, 80, 91, duration=duration, brightness=brightness),
    RGBTransition(11, 64, 87, duration=duration, brightness=brightness),
    RGBTransition(5, 52, 85, duration=duration, brightness=brightness),
    RGBTransition(0, 38, 79, duration=duration, brightness=brightness),
    RGBTransition(0, 25, 78, duration=duration, brightness=brightness),
    RGBTransition(0, 38, 79, duration=duration, brightness=brightness),
    RGBTransition(5, 52, 85, duration=duration, brightness=brightness),
    RGBTransition(11, 64, 87, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=5,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')

@login_required(login_url="/accounts/login")
def sun_theme(request):

    duration = 1000
    brightness = 100

    transitions = [
    RGBTransition(100, 96, 48, duration=duration, brightness=brightness),
    RGBTransition(100, 89, 41, duration=duration, brightness=brightness),
    RGBTransition(100, 80, 32, duration=duration, brightness=brightness),
    RGBTransition(99, 69, 20, duration=duration, brightness=brightness),
    RGBTransition(98, 59, 11, duration=duration, brightness=brightness),
    RGBTransition(98, 53, 3, duration=duration, brightness=brightness),
    ]

    flow = Flow(
    count=5,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')
