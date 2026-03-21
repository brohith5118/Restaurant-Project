from django.shortcuts import render,redirect
from .models import foodItem

# Create your views here.

def home(request):
    items = foodItem.objects.all()
    return render(request,'home.html',{'items':items})

def add_item(request):
    if(request.method == 'POST'):
        price = request.POST.get('price')
        name = request.POST.get('name')
        type = request.POST.get('type')
        description = request.POST.get('description')

        foodItem.objects.create(name=name,price=price,type=type,description=description)
        return redirect('/')
    return render(request,'add_item.html')

def manager_view(request):
    items = foodItem.objects.all()
    return render(request,'manager_view.html',{'items':items})

def delete_item(request,id):
    if(request.method == 'POST'):
        item = foodItem.objects.get(id=id)
        item.delete()
    return redirect('/')