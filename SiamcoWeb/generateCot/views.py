from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse
from SiamcoWeb import settings
from django.http import JsonResponse
from django.core import serializers
from django.core.files.storage import default_storage
from generateCot.controls.motorDB import motor_pg
from io import BytesIO
import urllib
import requests
import json
from django.core import serializers
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response, html_to_pdf, render_to_pdf
import os.path
from weasyprint import html



def genCot(request):
    print("valor ajax : ", bool(request.is_ajax()),
          "\nvalor post : ", request.method)
    datsCot = {'otherStyle': "*{margin:4px;}",
                   'textCot': '<h1>alv! el texto</h1>', 'customerName': 'seed'}
    #resp = render_to_pdf_response(request, 'generateCot/modelCot.html', datsCot,
    #                                  download_filename='cot.pdf', content_type='application/pdf')
    
    if request.is_ajax() and request.method == 'POST':
        mot_db = motor_pg()
        print("method ajax rendering templates!!")
        dDos = json.loads(request.POST.get('datsCot'))
        datsCot.update(dDos)      
        datsCot['idAutor'] = mot_db.getIdUser(datsCot['username'])
        pdf = render_to_string('generateCot/modelCot.html', datsCot)
        datsCot.update({'pdfTemplate': pdf, 'down': False })
        datsCot['dateToday'] = datsCot['dateToday'].split('/')
        datsCot['dateToday'] = datsCot['dateToday'][2] + '-' + datsCot['dateToday'][1] + '-' + datsCot['dateToday'][0]
        #print("datscot de mierda : ", datsCot)
        mot_db.saveQuotation(datsCot)
        mot_db.commit()
        mot_db.closeDB()
        #print("dats : ", datsCot)
        return JsonResponse({'isRender': True, 'username':datsCot['username'] })
    else :
        print("no se reconocio la peticion ajax")
        return redirect('homeLoggin')

def docCotHtml(request):
    print("docCotHtml--> valor ajax : ", bool(request.is_ajax()),
          "\nvalor post : ", request.method)
    if request.method == 'POST' and not request.is_ajax():
        print("method no ajax !!")
        mot_db = motor_pg()
        username = request.POST.get('username')
        print("method no ajax !! ",username )
        id_user = mot_db.getIdUser(username)  
        textPdf = mot_db.getTextPdf(id_user)
        mot_db.updatePdfUser(id_user)
        mot_db.commit()
        print("username : ", id_user, " ", username, "\ntemplateText : \n")
        resp = render_to_pdf_response(request, 'generateCot/docPdf.html', {'content':textPdf},
                                      download_filename='cotizacion.pdf', base_url=request.build_absolute_uri() )
        mot_db.closeDB()
        return resp 
    print("pal loggin")
    return redirect('homeLoggin')



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
    if request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('userpass')
        captchaKey = request.POST.get('captchaCheck')
        capt_url = "https://google.com/recaptcha/api/siteverify"
        cap_data = {'secret': settings.CAPTCHA_SECRET_KEY,
                    'response': captchaKey}
        cap_server_response = requests.post(url=capt_url, data=cap_data)
        capJson = json.loads(cap_server_response.text)
        capJson['userValidate'] = False
        r = mot.existUser(username, password)
        capJson['userValidate'] = r
        mot.closeDB()       
        return JsonResponse(capJson)
    else:
        username = request.POST.get('Username')
        password = request.POST.get('Userpass')
        r = mot.existUser(username, password)
        mot.closeDB()
        if request.method == 'POST' and not request.is_ajax() and r != False:
            dictTemplate['fname'] = r[0]
            dictTemplate['lname'] = r[1]
            dictTemplate['username'] = username
            return render(request, 'generateCot/mainCot.html', dictTemplate)
        else:
            return redirect('homeLoggin')
    
    mot.closeDB()
    return redirect('homoLoggin')
