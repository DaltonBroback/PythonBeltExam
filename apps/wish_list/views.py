from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Item
from ..loginregistration.models import User


def index(request):
    context = {
	   "All_Items": Item.objects.all(),
	   "All_Users": User.objects.all(),
	   "This_Items_Me": Item.objects.filter(user__email=request.session['email'], added_by=request.session['username']),
	   "This_Items_Them": Item.objects.filter(user__email=request.session['email']).exclude(added_by=request.session['username']),
       "Other_Items": Item.objects.exclude(user__email=request.session['email']),
    }
    return render(request, 'wish_list/index.html', context)

def logout(request):
    return redirect('users:my_index')

def add(request):
    # Item.objects.all().delete()
    return render(request, 'wish_list/create.html')
def items(request, id):
    request.session['id'] = id
    context = {
        "This_Item": Item.objects.get(id = id),
        "These_Users": User.objects.filter(items__id = id)
    }
    return render(request, 'wish_list/items.html', context)

def create(request):
    user_email = request.session['email']
    this_user = User.objects.get(email = user_email)
    item_name = request.GET['item']
    errors = 0
    try:
        item = Item.objects.get(name = item_name)
        this_user.items.add(item)
        this_user.save()
        print "double item"
        # Item.objects.get(name = item_name).add(user = this_user)
        messages.add_message(request, messages.INFO, "Item already listed")
        return redirect('wish:my_add')
    except:
        if len(item_name) < 3:
            errors += 1
            messages.add_message(request, messages.INFO, "item name must be longer than 3 characters!")
            return redirect('wish:my_add')
        if errors == 0:
            item = Item.objects.create(name = item_name, added_by =request.session['username'])
            item.save
            this_user.items.add(item)
            this_user.save()
        return redirect('wish:my_index')
    return redirect('wish:my_index')

def take(request):
    this_user = User.objects.get(email = request.session['email'])
    this_item = Item.objects.get(id = request.GET['id'])
    this_user.items.add(this_item)
    this_item.save()
    this_user.save()
    return redirect('wish:my_index')

def remove(request):
    this_user = User.objects.get(email = request.session['email'])
    this_item = Item.objects.get(id = request.GET['id'])
    this_user.items.remove(this_item)
    this_item.save()
    this_user.save()
    return redirect('wish:my_index')

def delete(request):
    this_item = Item.objects.get(id = request.GET['id'])
    this_item.delete()
    return redirect('wish:my_index')




# Create your views here.
