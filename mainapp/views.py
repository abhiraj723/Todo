from django.shortcuts import render, redirect
from mainapp.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    # create data
    if request.method == 'POST':
        item = request.POST.get('item')
        Lists.objects.create(item=item)
        messages.success(request, "Item added SuccessFully")
        return redirect('index')
    return render(request, 'index.html')

def about(request):
    #show data
    it = Lists.objects.all()
    context = {
        "lst":it,
    }
    return render(request, 'about.html',context)

#Delete item
def delItem(request, id):
    i = Lists.objects.get(sno=id)
    i.delete()
    messages.success(request, "Item Deleted Successfully")
    return redirect('about')

#update Item
def updateItem(request, id):
    ite = Lists.objects.get(sno=id)
    data = {
        "ls" : ite,
    }
    if request.method =='POST':
        item = request.POST.get('item')
        ite.item = item
        ite.save()
        messages.success(request, "Updated Successfully")
        return redirect('about')

    return render(request, 'update.html', data)
    