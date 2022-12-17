from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.

def demo(request):
    obj=Place.objects.all()
    ob=Team.objects.all()
    return render(request,"indexx.html",{'result':obj, 'res':ob})
