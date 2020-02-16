from django.shortcuts import render
from django.http import HttpResponse
# from .models import Vendor
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

# def list(request):
#     Data = {"Vendor": Vendor.objects.all()}
#     return render(request, 'pages/home.html', Data)

