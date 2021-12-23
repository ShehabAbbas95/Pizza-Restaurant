from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from . models import *
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = {
        "user" : request.user,
        "dinner": item.objects.filter(type='Dinner'),
        "regular":item.objects.filter(type='Regular').all(),
        "sicilian":item.objects.filter(type='Sicilian').all(),
        "p_s":pasta_salads.objects.all(),
        "subs":item.objects.filter(type='Subs'),
        "top":toppings.objects.all(),

    }
    return render(request, "orders/index.html",context)
def log_in(request):
    username = request.POST["username"]
    password = request.POST["pass"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})
def log_out(request):
    logout(request)
    return render(request, "orders/login.html", {"message":"Logged Out."})

def addtocart(request, id=None):

    if request.method== "POST":

        plate = (request.POST.get('plate'))
        if not plate:
            messages.error(request, 'Select Your Plate :D')
            return HttpResponseRedirect(reverse(addtocart))
        if plate == "Regular":
            type = request.POST.get("typer")
            if not type:
                messages.error(request, 'Select Your Regular-Pizza Filling :D')
                return HttpResponseRedirect(reverse(addtocart))
        elif plate == "Sicilian":
            type = request.POST.get('types')
            if not type:
                messages.error(request, 'Select Your Sicilian-Pizza Filling :D')
                return HttpResponseRedirect(reverse(addtocart))
        else:
            type = request.POST.get('dinner')

        size = request.POST.get("size")
        if not size:
            messages.error(request, 'Missing Order Size:D')
            return HttpResponseRedirect(reverse(addtocart))
        topping = request.POST.get('topping')
        topping2 = request.POST.get('2topping')
        if not topping2 and (type== '2 toppings' or type== '3 toppings'):
            messages.error(request, 'Select Your 2nd Topping:D')
            return HttpResponseRedirect(reverse(addtocart))
        topping3= request.POST.get('3topping')
        if not topping3 and type == '3 toppings':
            messages.error(request, 'Select Your 3rd Topping:D')
            return HttpResponseRedirect(reverse(addtocart))
        item_number = request.POST.get("item_number")
        sub = request.POST.get('subs')
        subs_number = request.POST.get('subs_number')
        p_s = request.POST.get('p_s')
        item_price = item.objects.filter(name=type,type=plate).all()
        p_s_price = pasta_salads.objects.filter(n=p_s)
        p_s_number = request.POST.get("p_s_number")
        if not p_s_price:
            p_s_price =  pasta_salads.objects.filter(n="Pasta & Salads")
        subs_price = item.objects.filter(name=sub,type="Subs").all()
        if not subs_price:
            subs_price = item.objects.filter(name="Subs",type="Subs").all()
        if size == 'small':
            price = (item_price[0].small * int(item_number)) + (p_s_price[0].price * int(p_s_number)) + (subs_price[0].small * int(subs_number))

        else:
            price = (item_price[0].large * int(item_number)) + (p_s_price[0].price * int(p_s_number)) + (subs_price[0].large * int(subs_number))


        context = {
        "size": size,
        "name": plate,
        "topping" : topping,
        "2topping": topping2,
        "3topping": topping3,
        "sub": sub,
        "type": type,
        "price": price,

        }
        user = request.user.get_username()
        if not id:
            cart = carts(name=plate, size = size, type=type,topping = topping,second_topping=topping2,
            third_topping=topping3, subs = sub, pasta_salads= p_s ,item_number=item_number,
            subs_number=subs_number, p_s_number=p_s_number, price = price , user = user)
            cart.save()
            return redirect("/cart")
        carts.objects.filter(id=id).update(name=plate, size = size, type=type,topping = topping,second_topping=topping2,
        third_topping=topping3, subs = sub, pasta_salads= p_s, item_number=item_number,
        subs_number=subs_number, p_s_number=p_s_number, price= price )
        return redirect("/cart")

    else:
        context = {
            "plate": plates.objects.all(),
            "subs":item.objects.filter(type='Subs'),
            "topping":toppings.objects.all(),
            "typer" : item.objects.filter(type='Regular'),
            "types" : item.objects.filter(type='Sicilian'),
            "dinner" : item.objects.filter(type='Dinner'),
            "p_s" : pasta_salads.objects.all(),
            "id":id
        }
        return render(request, "orders/addtocart.html",context)
def cart(request, user=None):
    if request.method == "POST":
        cart = carts.objects.all()
        user = request.user.get_username()
        for i in range(len(cart)):
            f = cart[i]
            order = orders(name=f.name, size = f.size, type=f.type,topping = f.topping,second_topping=f.second_topping,
            third_topping=f.third_topping, subs = f.subs, pasta_salads= f.pasta_salads, user = user)
            order.save()
        carts.objects.all().delete()
        return HttpResponseRedirect(reverse(index))

    else:
        cost = 0
        user = request.user.get_username()
        cart = carts.objects.all()
        cost = carts.objects.filter(user = user).aggregate(Sum('price'))
        if not cart:
            messages.error(request, "Cart Empty")
            return HttpResponseRedirect(reverse(index))

        return render(request, "orders/cart.html", {"cart":cart,"cost":cost})
def remove(request,id=None):
    if not id:
        carts.objects.all().delete()
    carts.objects.filter(id=id).delete()
    return redirect("/cart")

def edit(request,id=None):
    return HttpResponseRedirect(reverse(addtocart))
