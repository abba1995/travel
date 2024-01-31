from django.http import request
from django.shortcuts import render

from . models import Place,Meet


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Meet.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj2})
# def about(request):
#     return render(request,"elements.html")

