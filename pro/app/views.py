from django.contrib import messages, auth

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Watches

# Create your views here.
def home(request):
    content=Watches.objects.all()
    d=User.objects.all()
    data={
        'result':content,
        'user1':d
        
    }
    return render(request,'index.html',data)

def details(request,id):
    product=Watches.objects.get(pk=id)
    print(product)
    data={
        'data':product
    }
    return render(request,'single.html',data)
