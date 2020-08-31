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
    datsCot = {'textCot': '<h1>alv! el texto</h1>', 'customerName': 'seed'}
    if request.is_ajax() and request.method == 'POST':
        mot_db = motor_pg()
        dDos = json.loads(request.POST.get('datsCot'))
        datsCot.update(dDos)
        datsCot['idAutor'] = mot_db.getIdUser(datsCot['username'])
        pdf = render_to_string('generateCot/modelCot.html', datsCot)
        datsCot.update({'pdfTemplate': pdf, 'down': False})
        datsCot['dateToday'] = datsCot['dateToday'].split('/')
        datsCot['dateToday'] = datsCot['dateToday'][2] + '-' + \
            datsCot['dateToday'][1] + '-' + datsCot['dateToday'][0]
        mot_db.saveQuotation(datsCot)
        mot_db.commit()
        mot_db.closeDB()
        return JsonResponse({'isRender': True, 'username': datsCot['username']})
    else:
        return redirect('homeLoggin')


def docCotHtml(request):
    if request.method == 'POST' and not request.is_ajax():
        mot_db = motor_pg()
        username = request.POST.get('username')
        id_user = mot_db.getIdUser(username)
        textPdf = mot_db.getTextPdf(id_user)
        mot_db.updatePdfUser(id_user)
        mot_db.commit()
        resp = render_to_pdf_response(request, 'generateCot/docPdf.html', {'content': textPdf},
                                      download_filename='%s_SiamcoCot.pdf' % username, base_url=request.build_absolute_uri())
        mot_db.closeDB()
        return resp
    return redirect('homeLoggin')


def homeLoggin(request):

    dicTemplate = {'captcha_key': settings.CAPTCHA_WEB_KEY}

    return render(request, 'generateCot/homeLoggin.html', dicTemplate)


def mainCot(request, fName='', lName='', usrName=''):
    mot = motor_pg()
    colsUno = ['Cod', 'Descripcion', 'Und', 'Valor Und', 'Cant', '']
    colsDos = ['Actividad', 'Und', 'Cant', 'Valor Und', 'Valor Total', '']
    dictTemplate = {'fname': 'Seed', 'lname': 'C',
                    'listAct': mot.getActivitiesForTable(),
                    'colsUno': colsUno,
                    'colsDos': colsDos
                    }
    print("metodo mainCot() : ")
    if request.method == 'POST' and request.is_ajax():
        print("metodo ajax <---------")
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
            print("metodo post <---------")
            dictTemplate['fname'] = r[0]
            dictTemplate['lname'] = r[1]
            dictTemplate['username'] = username
            return render(request, 'generateCot/mainCot.html', dictTemplate)
        else:
            return redirect('homeLoggin')
    if request.method == 'GET' and usrName != '':
        dictTemplate['fname'] = fName
        dictTemplate['lname'] = lName
        dictTemplate['username'] = usrName
        return render(request, 'generateCot/mainCot.html', dictTemplate)
    mot.closeDB()
    return redirect('homeLoggin')


def manageActivities(request, username=''):
    mot = motor_pg()
    if username != '':
        print("user name : %s" % username)
        existUsr = mot.getStatement(
            "select fname, lname from users where username = %s", (username,)).fetchall()
        listAct = mot.getActivitiesForTable()
        mot.closeDB()
        if existUsr != None:
            dicContex = {
                'fname': existUsr[0][0],
                'lname': existUsr[0][1],
                'username': username,
                'cols': ['', 'Cod', 'Descripcion', 'Und', 'Valor Und'],
                'lActivities': listAct
            }
            return render(request, 'generateCot/manageActivities.html', dicContex)
        else:
            mot.closeDB()
            return redirect('homeLoggin')
    else:
        mot.closeDB()
        return redirect('homeLoggin')

def saveActiviti(request):

    if request.method == 'POST' and request.is_ajax() :
        mot = motor_pg()
        dicRes = {'save': False }
        dats = json.loads(request.POST.get('dats')) 
        try :
            idx = mot.getNewIdActi()
            print("datos : ", dats)
            dats['und'] = mot.getStatement("select id_unid from measurement_units where symbol = %s", (dats['und'],)).fetchall()[0][0]
            mot.executeStatement('insert into activities(cod, description, unit, valueunit) values(%s,%s,%s,%s)',
                             (idx, dats['descrip'], dats['und'], dats['value']))
            dicRes['save'] = True
            mot.commit()
            print("se guardo la actividad")
        except Exception as error:
            dicRes['save'] = False
            print("no se pudo agregar la actividad, error: ", error)
            pass
        mot.closeDB()
        return JsonResponse(dicRes)