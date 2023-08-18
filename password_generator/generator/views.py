from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def index(request):
    return render(request,'generator/index.html')

def password(request):
    charachters=[]
    length=int(request.GET.get('length',12 ))# get length from index.html through request ,12 is defualt value
    thepassword=''
    
    if request.GET.get('lowercase'):
        charachters.extend(list('abcdefghigklmnopqrstuvwxyz'))

    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        charachters.extend(list('0123456789'))

    if request.GET.get('special'):
        charachters.extend(list('!@#$%&*?'))    
        
    if len(charachters)== 0:
        return render(request,'generator/index.html')
               
    for i in range(length):
        thepassword+=random.choice(charachters)

    return render(request,'generator/index.html',{'password':thepassword})
