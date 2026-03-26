from django.shortcuts import render,redirect
from .models import foodItem,Category,Order,OrderItem
from django.db.models import Case, When, Value, IntegerField
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    categories = Category.objects.all().order_by('order')
    return render(request,'home.html',{'categories':categories})

def add_item(request):
    categories = Category.objects.all()

    if(request.method == 'POST'):
        price = request.POST.get('price')
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = Category.objects.get(id=category_id)

        foodItem.objects.create(
            name=name,
            price=price,
            category=category,
            description=description,
            image=image
        )
        
        return redirect('manager_view')
    return render(request,'add_item.html',{'categories':categories})


def manager_view(request):
    items = foodItem.objects.select_related('category').all()
    return render(request,'manager_view.html',{'items':items})

def delete_item(request,id):
    if(request.method == 'POST'):
        item = get_object_or_404(foodItem, id=id)
        item.delete()
    return redirect('manager_view')

def open_edit(request,id):
    item = foodItem.objects.get(id=id)
    categories = Category.objects.all()
    return render(request,'edit_item.html',{'item':item,'categories':categories})

def edit_item(request, id):
    item = foodItem.objects.get(id=id)

    if request.method == "POST":
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        category_id = request.POST.get('category')
        item.category = Category.objects.get(id = category_id)
        item.description = request.POST.get('description')
        if request.FILES.get('image'):
            item.image = request.FILES.get('image')
        item.save()
        return redirect('manager_view')

    categories = Category.objects.all()
    return render(request, 'edit_item.html', {
        'item': item,
        'categories': categories
    })

def view_item(request,id):
    item = foodItem.objects.select_related('category').get(id=id)
    return render(request,'item.html',{'item':item})

def add_to_cart(request,id):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity',1))

        order_id = request.session.get('order_id')

        if order_id:
            order = Order.objects.get(id=order_id, is_completed=False)
        else:
            order = Order.objects.create()
            request.session['order_id'] = order.id

        item = foodItem.objects.get(id=id)

        order_item, created = OrderItem.objects.get_or_create(
            order = order,
            food_item = item,
            defaults={'quantity':quantity}
        )

        if not created:
            order_item.quantity += quantity
            order_item.save()
    return redirect('view_item',id=id)