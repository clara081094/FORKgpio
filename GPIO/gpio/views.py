from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
#import RPi.GPIO as GPIO
import time
from random import randint

@csrf_exempt
def login_user(request):
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/gpio/')

    logout(request)
    state = "Registrese en la parte superior"
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gpio/')
            else:
                state = "Su cuenta no existe, contacte con el administrador"
        else:
            state = "Su username y/o password son incorrectos."

    return render_to_response('gpio/login.html',{'state':state, 'username': username})


@csrf_exempt
@login_required(login_url='/login/')
def index(request):
	#estados=GPIO.input(23)
    #estado+
    if 'action1' in request.POST.keys():
       encender()
    if 'action2' in request.POST.keys():
       apagar()

    #GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(13, GPIO.OUT)
    #GPIO.setup(15, GPIO.OUT)
    #GPIO.setup(16, GPIO.IN)
    #estado = GPIO.input(16) # 0 --> prendido #ACA LEEE
    estado=0
    return render_to_response('gpio/indexCalc.html',
    	{'estado':estado,}
     )

def encender():
    print("encendiendo")
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.output(13,True)
    time.sleep(1) 
    #GPIO.output(13,False)
	
def apagar():
    print("apagando")
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(15,GPIO.OUT)
    #GPIO.output(15,True)
    time.sleep(1) 
    #GPIO.output(15,False)
	
    