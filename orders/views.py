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
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,'add_item.html')

def manager_view(request):
    items = foodItem.objects.all()
    return render(request,'manager_view.html',{'items':items})

def delete_item(request,id):
    if(request.method == 'POST'):
        item = foodItem.objects.get(id=id)
        item.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def open_edit(request,id):
    item = foodItem.objects.get(id=id)
    return render(request,'edit_item.html',{'item':item})

def edit_item(request, id):
    item = foodItem.objects.get(id=id)

    if request.method == "POST":
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.save()
        return redirect('/')

    return render(request, 'edit_item.html', {'item': item})