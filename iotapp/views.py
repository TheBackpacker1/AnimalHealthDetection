from django.shortcuts import render,HttpResponse
from .models import cheepNecklace
# Create your views here.

def home(request):
    context = {'allcheep':cheepNecklace.objects.all()}
    return render(request,"website/home.html",context=context)