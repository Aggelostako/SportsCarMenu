from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
def home(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request,'useraccount/home.html', context)

def item(request):
    return HttpResponse("<h1>What a fantastic car</h1>")

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item':item,}
    return render(request,'useraccount/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'useraccount/item-form.html',{'form':form})

def update_item(request,id):
    item = Item.objects.get(pk=id) 
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() :
        form.save()
        return redirect('home')
    return render(request,'useraccount/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request,'useraccount/item-delete.html',{'item':item})
    a



# Create your views here.
