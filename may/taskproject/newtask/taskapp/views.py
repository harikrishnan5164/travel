from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#def home(request):
    #return HttpResponse("hey its home")
#def demo(request):
 #   return render(request,"add.html")
#def addition(request):
    #x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #res=x+y
   # su=x-y
   ## mu=x*y
   # di=x/y
    #return render(request,"result.html",{'result':res,'res1':su,'res2':mu,'res3':di})
from . models import Place
from . models import People


def demo(request):
    obj=Place.objects.all()
    per=People.objects.all()
    return render(request,"index.html",{'result':obj,'output':per})