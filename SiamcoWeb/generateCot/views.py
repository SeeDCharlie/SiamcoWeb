from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from SiamcoWeb import settings
from django.http import JsonResponse
from django.core import serializers
from generateCot.controls.motorDB import motor_pg
import urllib
import requests
import json



def homeLoggin(request ):

    dicTemplate = {'captcha_key': settings.CAPTCHA_WEB_KEY}

    return render(request, 'generateCot/homeLoggin.html', dicTemplate )

def mainCot(request):
    mot = motor_pg()
    colsUno = ['Cod','Descripcion','Und','Valor Und','Cant', '']
    colsDos = ['Actividad','Und','Cant','Valor Und','Valor Total', '']

    dictTemplate = {'fname':'Seed', 'lname':'C', 
                    'listAct': mot.getActivitiesForTable(), 
                    'colsUno':colsUno,
                    'colsDos':colsDos
                    }

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('userpass')

        captchaKey = request.POST.get('captchaCheck')
        capt_url = "https://google.com/recaptcha/api/siteverify"      

        cap_data = {'secret': settings.CAPTCHA_SECRET_KEY, 'response': captchaKey}
        cap_server_response = requests.post(url = capt_url, data = cap_data)
        capJson = json.loads(cap_server_response.text)
        capJson['userValidate'] = False

        if not capJson['success']:
            mot.closeDB()
            return JsonResponse(capJson)

        else:
            
            r = mot.existUser(username, password)
            mot.closeDB()

            if r != False :
                dictTemplate['fname'] = r[0]
                dictTemplate['lname'] = r[1]
            
                return render(request, 'generateCot/mainCot.html', dictTemplate)
            else:

                return JsonResponse(capJson)
    else:    
        mot.closeDB()
        return render(request, 'generateCot/mainCot.html', dictTemplate )