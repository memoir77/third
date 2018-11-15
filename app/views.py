from Cython.Shadow import address
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Address

def list(request):
    address = Address.objects.all()
    return HttpResponse(address)

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