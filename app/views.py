from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import Address
# Create your views here.
from app.models import Address

@csrf_exempt

def save(request,id):
    address = request.POST['address']
    a = Address.objects.get(id=id)
    a.address = address
    a.save()

    return HttpResponse('GG')

def edit(request,id):
    address = Address.objects.get(id=id)
    return render(request,
                  'app/edit.html',
                  {'address':address})

def list(request):
    address = Address.objects.all()
    return render(
        request,
        'app/list.html',
        {'address' : address}
    )

def index(request):
    address = ''
    try:
        address = request.GET['address']

        add = Address(address=address)
        add.save()
    except MultiValueDicKeyError:
        pass
    return HttpResponse(
        '{"Hello":"'+address+'"}')