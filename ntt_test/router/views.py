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
    
    if form_data['id'] != '':
        try:
            router = get_object_or_404(Router, id=int(form_data['id']))
        except Router.DoesNotExist:
            data = {
                'error': 'router not found'
            }
            return JsonResponse(data, safe=False)
        router.name = form_data['name']

        if form_data['ip_add']:
            router.ip_address = form_data['ip_add']
        router.save()

        detail = Router.objects.get(id=router.id)
        data = {
            'id': detail.id,
            'name': detail.name,
            'ip_add': detail.ip_address
        }
        
        return JsonResponse(data, safe=False)
    

    elif request.method == 'POST':
        if form_data['name'] is not None:
            router = Router()
            router.name = form_data['name']
            if form_data['ip_add']:
                router.ip_address = form_data['ip_add']
            router.save()
            detail = Router.objects.get(id = router.id)

        if detail:
            data = {
                'id': detail.id,
                'name': detail.name,
                'ip_add': detail.ip_address
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
        'name': router.name,
        'ip_add': router.ip_address
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
            router.name = randString['text']
            router.ip_address = randString['id']
            router.save()

        detail = Router.objects.get(id = router.id)

        data = {
            'id': detail.id,
            'name': detail.name,
            'ip_add': detail.ip_address
        }

        return JsonResponse(data, safe=False)
        
    else:
        randString = generateString()
        router = Router()
        router.name = randString['text']
        router.ip_address = randString['id']
        router.save()
        # data = {
        #     'info': 'Router created'
        # }

        data = {
            'id': router.id,
            'name': randString['text'],
            'ip_add': randString['id']
        }

        return JsonResponse(data, safe=False)

def generateString():
    randomString = strgen.StringGenerator("[\w\d]{10}").render()
    num = random.random()
    num = int(num * 100)
    data = {
        'id': num,
        'text': randomString
    }
    return data
