from django.shortcuts import render, get_object_or_404
from .forms import RouterForm
from .models import Router
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
import strgen
import random

def routerList(request):

    form = RouterForm()
    routers = Router.objects.all()

    context = {
        'form': form,
        'routers': routers
    }

    return render(request, 'index.html', context)

def createRouter(request, *args, **kwargs):
    form_data = request.POST.dict()
    #print(form_data)
    if form_data['id'] != '':
        try:
            router = get_object_or_404(Router, id=int(form_data['id']))
        except Router.DoesNotExist:
            data = {
                'error': 'router not found'
            }
            return JsonResponse(data, safe=False)
        router.sap_id = form_data['sap_id']

        if form_data['hostname']:
            router.hostname = form_data['hostname']
        if form_data['ip_address']:
            router.ip_address = form_data['ip_address']
        if form_data['mac_address']:
            router.mac_address = form_data['mac_address']
        router.save()

        detail = Router.objects.get(id=router.id)
        data = {
            'id': detail.id,
            'sap_id': detail.sap_id,
            'hostname': detail.hostname,
            'ip_address': detail.ip_address,
            'mac_address': detail.mac_address,
        }
        
        return JsonResponse(data, safe=False)
    

    elif request.method == 'POST':
        if form_data['sap_id'] is not None:
            router = Router()
            router.sap_id = form_data['sap_id']
            if form_data['hostname']:
                router.hostname = form_data['hostname']
            if form_data['ip_address']:
                router.ip_address = form_data['ip_address']
            if form_data['mac_address']:
                router.mac_address = form_data['mac_address']
            router.save()
            detail = Router.objects.get(id = router.id)

        if detail:
            data = {
                'id': detail.id,
                'sap_id': detail.sap_id,
                'hostname': detail.hostname,
                'ip_address': detail.ip_address,
                'mac_address': detail.mac_address
            }

        return JsonResponse(data, safe=False)

def editRouter(request, pk):
    id = request.GET.get('id', None)
    try:
        router = get_object_or_404(Router, id=id)
    except Router.DoesNotExist:

        data = {
            'error': 'router not found'
        }

        return JsonResponse(data, safe=False)

    data = {
        'id': router.id,
        'sap_id': router.sap_id,
        'hostname': router.hostname,
        'ip_address': router.ip_address,
        'mac_address': router.mac_address
    }

    return JsonResponse(data, safe=False)


def deleteRouter(request):
    id = request.POST.get('id', None)

    try:
        router = get_object_or_404(Router, id=id)
    except Router.DoesNotExist:

        data = {
            'error': 'router not found'
        }

        return JsonResponse(data, safe=False)

    router.delete()

    data = {
        'message': 'router deleted'
    }

    return JsonResponse(data, safe=False)

def generateRecords(request):
    id = request.GET.get('id', None)
    id = int(id)

    if id > 1:
        for i in range(id):
            randString = generateString()
            router = Router()
            router.sap_id = randString['sap_id']
            router.hostname = randString['hostname']
            router.ip_address = randString['ip_address']
            router.mac_address = randString['mac_address']
            router.save()

        detail = Router.objects.get(id = router.id)

        data = {
            'id': detail.id,
            'sap_id': randString['sap_id'],
            'hostname': randString['hostname'],
            'ip_address': randString['ip_address'],
            'mac_address': randString['mac_address']
        }

        return JsonResponse(data, safe=False)
        
    else:
        randString = generateString()
        router = Router()
        router.sap_id = randString['sap_id']
        router.hostname = randString['hostname']
        router.ip_address = randString['ip_address']
        router.mac_address = randString['mac_address']
        router.save()
        # data = {
        #     'info': 'Router created'
        # }

        data = {
            'id': router.id,
            'sap_id': randString['sap_id'],
            'hostname': randString['hostname'],
            'ip_address': randString['ip_address'],
            'mac_address': randString['mac_address']
        }

        return JsonResponse(data, safe=False)

def generateString():
    hostname = strgen.StringGenerator("[\w\d]{10}").render()
    num = random.random()
    sap_id = int(num * 100)

    def ipAdd(n):
        ip_add = ''
        for i in range(n):
            num1 = random.random()
            num1 *= 1000
            ip_add += str(int(num1)) +'.'
        
        return ip_add[:-1]
    
    data = {
        'sap_id': sap_id,
        'hostname': hostname,
        'ip_address': ipAdd(4),
        'mac_address': ipAdd(5)
    }

    #print(data)
    return data
