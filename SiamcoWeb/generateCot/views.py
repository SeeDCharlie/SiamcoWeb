from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse
from SiamcoWeb import settings
from django.http import JsonResponse
from django.core import serializers
from generateCot.controls.motorDB import motor_pg
from io import BytesIO
import urllib
import requests
import json
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response
import os.path


class HelloPDFView(PDFTemplateView):
    template_name = 'generateCot/modelCot.html'
    download_filename = 'prueba.pdf'
    # base_url=request.build_absolute_uri()

    def get_context_data(self, **kwargs):
        url = os.path.dirname(
            settings.BASE_DIR) + "/SiamcoWeb/generateCot/static/generateCot/filesModelCot"
        # print("la piche ruta : " + url)
        return super(HelloPDFView, self).get_context_data(pagesize='A4', title='Hi there!',
                                                          url=url, **kwargs
                                                          )


def docCotHtml(request):

    context = {}
    resp = render_to_pdf_response(request, 'generateCot/modelCot.html', context,
                                  download_filename='cot.pdf', content_type='application/pdf')

    if request.method == 'POST':
        table = request.POST.get('tabledos')
        print("tabla cot: ", table)

    return resp


def homeLoggin(request):

    dicTemplate = {'captcha_key': settings.CAPTCHA_WEB_KEY}

    return render(request, 'generateCot/homeLoggin.html', dicTemplate)


def mainCot(request):
    mot = motor_pg()
    colsUno = ['Cod', 'Descripcion', 'Und', 'Valor Und', 'Cant', '']
    colsDos = ['Actividad', 'Und', 'Cant', 'Valor Und', 'Valor Total', '']

    dictTemplate = {'fname': 'Seed', 'lname': 'C',
                    'listAct': mot.getActivitiesForTable(),
                    'colsUno': colsUno,
                    'colsDos': colsDos
                    }

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('userpass')

        captchaKey = request.POST.get('captchaCheck')
        capt_url = "https://google.com/recaptcha/api/siteverify"

        cap_data = {'secret': settings.CAPTCHA_SECRET_KEY,
                    'response': captchaKey}
        cap_server_response = requests.post(url=capt_url, data=cap_data)
        capJson = json.loads(cap_server_response.text)
        capJson['userValidate'] = False

        if not capJson['success']:
            mot.closeDB()
            return JsonResponse(capJson)

        else:

            r = mot.existUser(username, password)
            mot.closeDB()

            if r != False:
                dictTemplate['fname'] = r[0]
                dictTemplate['lname'] = r[1]

                return render(request, 'generateCot/mainCot.html', dictTemplate)
            else:

                return JsonResponse(capJson)
    else:
        mot.closeDB()
        return render(request, 'generateCot/mainCot.html', dictTemplate)
