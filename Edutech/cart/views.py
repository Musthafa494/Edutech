from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart,Order,Account
from courses.models import Module
from django.contrib.auth import authenticate,login,logout
def cart_view(request):
    total=0
    try:
        user=request.user
        carts=Cart.objects.filter(user=user)
        for i in carts:
            total+=i.quantity*i.products.price
    except Cart.DoesNotExist:
        pass
    return render(request,'mycourses.html',{'cart':carts,'total':total})


@login_required
def cartproducts(request,p):
    products=Module.objects.get(id=p)
    user=request.user
    try:


         carts=Cart.objects.get(products=products,user=user)
         if carts.quantity < carts.products.stock:
             carts.quantity+=1
         carts.save()

    except Cart.DoesNotExist:
        carts = Cart.objects.create(products=products, user=user, quantity=1)
        carts.save()


    return redirect('cart:cart_view')
@login_required
def deleteitem(request,p):
    user=request.user
    products=Module.objects.get(id=p)
    try:
        cart=Cart.objects.get(user=user,products=products)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def cartremove(request,p):
    user=request.user
    products=Module.objects.get(id=p)
    try:
        cart=Cart.objects.get(user=user,products=products)
        if cart.quantity >1:
            cart.quantity -=1
            cart.save()

        else:
            cart.delete()

    except:
        pass
    return redirect('cart:cart_view')

@login_required
def order(request):
    total=0
    items=0
    msg=0

    if (request.method=='POST'):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.products.price
            items+=i.quantity


        ac=Account.objects.get(acctnumber=n)
        if float( ac.amount) >= total:
                ac.amount=ac.amount-total
                ac.save()
                for i in cart:
                    o=Order.objects.create(user=user,products=i.products,email=a,phone=p,order_status="paid",noofitems=i.quantity)
                    o.save
                cart.delete()
                msg="successfully Registerd for the course  "
                return render(request, 'orderdetails.html',{'msg':msg,'total':total,'items':items})
        else:
                msg="insufficient Amount.you can't place order"
                return render(request,'orderdetails.html',{'msg':msg})

    return render(request,'adress.html')
@login_required
def orderview(request):

    ord=Order.objects.filter(user=request.user,order_status="paid")

    return render(request,"orderview.html",{'o':ord} )
def content(request):
    pdf=Module.objects.values_list('file',flat=True)
    return render(request, 'content.html',{'pdf':pdf})