from django.shortcuts import render
from .models import foodItem

# Create your views here.

def home(request):
    items = foodItem.objects.all()
    return render(request,'home.html',{'items':items})