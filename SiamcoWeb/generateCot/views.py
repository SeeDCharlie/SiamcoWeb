from django.shortcuts import render
from SiamcoWeb import settings
from django.http import JsonResponse
from django.core import serializers
import urllib
import requests
import json

# Create your views here.

def homeLoggin(request):
    return render(request, 'generateCot/homeLoggin.html') 

def mainCot(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        captchaKey = request.POST.get('g-recaptcha-response')
        capt_url = "https://google.com/recaptcha/api/siteverify"
        cap_secretKey = "6Lev1bQZAAAAAMDLb7YJtfLfZIIVJjtdPtl3h4Wj"
        cap_data = {'secret': cap_secretKey, 'response': captchaKey}
        cap_server_response = requests.post(url = capt_url, data = cap_data)
        capJson = json.loads(cap_server_response.text)

        if not capJson['success']:
            return JsonResponse({"valid": False}, status = 200)
        else:
            return render(request, 'generateCot/mainCot.html' )

    else:
        return render(request, 'generateCot/mainCot.html' )