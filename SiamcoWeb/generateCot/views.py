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



def homeLoggin(request, msj = ""):

    dicTemplate = {'captcha_key': settings.CAPTCHA_WEB_KEY, 'msj': msj}

    return render(request, 'generateCot/homeLoggin.html', dicTemplate )

def mainCot(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['pass']

        captchaKey = request.POST.get('g-recaptcha-response')
        capt_url = "https://google.com/recaptcha/api/siteverify"
        
        cap_data = {'secret': settings.CAPTCHA_SECRET_KEY, 'response': captchaKey}
        cap_server_response = requests.post(url = capt_url, data = cap_data)
        capJson = json.loads(cap_server_response.text)

        if not capJson['success']:
            return redirect(homeLoggin)

        else:
            mot = motor_pg()
            r = mot.existUser(username, password)
            mot.closeDB()

            if r != False :
                dictMain = {'fname': r[0], 'lname': r[1]}
                return render(request, 'generateCot/mainCot.html', dictMain)
            else:
                return redirect( homeLoggin )
    else:    
        
        return redirect(homeLoggin)