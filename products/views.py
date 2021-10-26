from django import forms
from django.http import request
from django.shortcuts import redirect, render
from .models import Cart, Category, Comment, UserForm, products
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *




from django.contrib.auth.decorators import login_required

from django.db.models import Q

# Create your views here.




def Home(request):
  q=request.GET.get('q') if request.GET.get('q')!=None else ''


  productItem=products.objects.filter(
    Q(productName__icontains=q) |
    Q(category__name__icontains=q)
  )

  if q:
    category_title=q
  else:
    category_title="All"

  
  categories=Category.objects.all()

  paginator = Paginator(productItem, 2)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  context={'products':productItem, 'categories':categories, 'category_title':category_title,'page_obj': page_obj}
  return render(request,'products/home.html',context)
 



@login_required(login_url='login')
def productDetails(request,pk):
  product=products.objects.get(id=pk)
  


  product_comment=product.comment_set.all()
 
  

  if request.method=="POST":
      comment=Comment.objects.create(
      user=request.user,
      product=product,
      body=request.POST.get('body')
    )

 

  


  context={'product':product,'product_comment':product_comment}
  return render(request,'products/product_details.html',context)





def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'registration.html', {'form': form})


def loginUser(request):
  if request.user.is_authenticated:
    return redirect('home')

    
  if request.method=='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')

    try:
      user=UserForm.objects.get(username=username)
    except:
       messages.error(request, 'Username or password does not exist')

    user= authenticate(request,username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect ('home')

    # else:
    #   messages.error(request, 'Username or password does not exist')

    


  context={}
  return render(request,'login.html',context)


@login_required(login_url='login')
def DeleteComment(request, pk):
  comment=Comment.objects.get(id=pk)
  comment.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





@login_required(login_url='login')
def userLogout(request):
  logout(request)
  return redirect('home')




@login_required(login_url='login')
def paymentPage(request):

  productId=request.GET.get('id')
  product=products.objects.get(id=productId)
  context={'product':product}

  return render(request,'products/payment_page.html',context)


@login_required(login_url='login')
def addToCart(request):
  
  productId=request.GET.get('product-id')
  product=products.objects.get(id=productId)


 
  

  # cart=Cart(products=Id, user=request.user)
  # cart.save(force_insert=True)

  cart=Cart.objects.create(
    
    user=request.user,
    products=product
  )

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='login')
def showCart(request,pk):

  user=User.objects.get(id=pk)
  #product=products.objects.get(id=1)
  cartItem=Cart.objects.all()
  


  context={'cartItem':cartItem}
  return render(request, 'products/cart.html', context)




@login_required(login_url='login')
def removeCart(request):
  id=request.GET.get('id')
  cart=Cart.objects.get(id=id)
  cart.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def orderConfirmed(request):
  id=request.GET.get('id')
  product=products.objects.get(id=id)


  try:
    details=userDetails.objects.get(user=request.user)
    address=details.address1 + " " + details.address2
    phone=details.phn
  except userDetails.DoesNotExist:
    details=None
    address=None
    phone=None
    messages.error(request, 'Complete your profile to order')
    return redirect('profile')

  
  if address==" ":
    messages.error(request, 'Complete your profile to order')
    return redirect('profile')


   



  order=confirmedOrder.objects.create(
    productName=product,
    user=request.user,
    address=address,
    phone=phone
  )
  return redirect('home')


@login_required(login_url='login')
def profilePage(request):
  id=request.user.id
  user=User.objects.get(id=id)

  try:
    details=userDetails.objects.get(user=request.user)
  except userDetails.DoesNotExist:
    details=None
  

  context={'user':user, 'details':details}
  return render(request, 'products/profile.html',context)


def updateProfile(request):

  if request.method=='POST':
    phn=request.POST.get('phn')
    address1=request.POST.get('address1')
    address2=request.POST.get('address2')
    postcode=request.POST.get('postcode')
    state=request.POST.get('state')
    area=request.POST.get('area')
    country=request.POST.get('country')
    region=request.POST.get('region')


    try:
      details=userDetails.objects.get(user=request.user)
      userDetails.objects.filter(user=request.user).update(
      user=request.user,
      phn=phn,
      address1=address1,
      address2=address2,
      postcode=postcode,
      state=state,
      area=area,
      country=country,
      region=region
    )
    except userDetails.DoesNotExist:
      details=None
      userdtls=userDetails(
      user=request.user,
      phn=phn,
      address1=address1,
      address2=address2,
      postcode=postcode,
      state=state,
      area=area,
      country=country,
      region=region
       )
      userdtls.save()

   
    
    
   
    

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





