from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from gpio.models import Nombre
from django.contrib import messages
#import RPi.GPIO as GPIO
import time
from random import randint

@csrf_exempt
def login_user(request):
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/gpio/')

    logout(request)
    state = "Ingrese su usuario y password"
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(60)
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
    if 'action3' in request.POST.keys():
        return HttpResponseRedirect('/conf/')
    if 'action1' in request.POST.keys():
       encender()
    if 'action2' in request.POST.keys():
       apagar()

    #GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(13, GPIO.OUT)
    #GPIO.setup(18, GPIO.IN)
    #estado = GPIO.input(18) # 0 --> prendido #ACA LEEE
    estado=0
    planta=Nombre.objects.get(pk=1)
    return render_to_response('gpio/indexCalc.html',
    	{'estado':estado,'planta':planta}
     )

@csrf_exempt
@login_required(login_url='/login/')
def conf_user(request):

    state="Marque las opciones que desea cambiar"

    if request.POST:
        Nplanta = request.POST['Nplanta']
        Apassword = request.POST['Apassword']
        Ppassword = request.POST['Ppassword']
        try:
            option=request.POST['vehicle']
        except Exception,e:
            option="op"

        if option=="op":
            return HttpResponseRedirect('/gpio/')

        us = authenticate(username=request.user.username, password=Apassword)
        if option=="nom":
            if us is not None:
                plant=Nombre.objects.get(pk=1)
                plant.nombre_text = Nplanta
                plant.save()
                return HttpResponseRedirect('/gpio/')     
            else:
                state = "Su password es incorrecto."
        if option=="pass":
            if us is not None :
                request.user.set_password(Ppassword)
                request.user.save()
                state="Password cambiado correctamente, loguese para ingresar"
                return render_to_response('gpio/login.html',{'state':state})
            else:
                state = "Su password es incorrecto."      

    planta=Nombre.objects.get(pk=1)
    return render_to_response('gpio/conf.html',{'state': state,'planta': planta})

def encender():
    print("encendiendo")
   # GPIO.setmode(GPIO.BOARD)
    
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.output(13,True)
	
def apagar():
    print("apagando")
    #GPIO.setmode(GPIO.BOARD)
    
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.output(13,False)
	
    