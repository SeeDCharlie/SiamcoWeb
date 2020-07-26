from django.shortcuts import render
from SiamcoWeb import settings
from django.http import JsonResponse
from django.core import serializers
import urllib
import requests
import json

# Create your views here.

def homeLoggin(request):
    return render(request, 'generateCot/homeLoggin.html', {'captcha_key': settings.CAPTCHA_WEB_KEY}) 

def mainCot(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        captchaKey = request.POST.get('g-recaptcha-response')
        capt_url = "https://google.com/recaptcha/api/siteverify"
        
        cap_data = {'secret': settings.CAPTCHA_SECRET_KEY, 'response': captchaKey}
        cap_server_response = requests.post(url = capt_url, data = cap_data)
        capJson = json.loads(cap_server_response.text)
        print("captcha json : ", capJson)


        if not capJson['success']:
            return JsonResponse(capJson)
        else:
            return render(request, 'generateCot/mainCot.html' )

    else:
        return render(request, 'generateCot/mainCot.html' )