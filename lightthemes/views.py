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
    TemperatureTransition(1700, duration=1000),
    SleepTransition(duration=1000),
    TemperatureTransition(6500, duration=1000)
    ]

    flow = Flow(
    count=2,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')
