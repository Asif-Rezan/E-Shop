from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from products.api.serializers import cartSerializer, categorySerializer, commentSerializer, productsSeriliazer, userSeriliazer, userdetailsSerializer


from products.models import Cart, Category, Comment, UserForm, confirmedOrder, products, userDetails

from rest_framework.response import Response





from django.contrib.auth.decorators import login_required

from django.db.models import Q

# Create your views here.



@api_view(['GET'])
def Home(request):
  
  q=request.query_params.get('q') if request.GET.get('q')!=None else ''


  productItem=products.objects.filter(
    Q(productName__icontains=q) |
    Q(category__name__icontains=q)
  )

  if q:
    category_title=q
  else:
    category_title="All"

  
  categories=Category.objects.all()

  # paginator = Paginator(productItem, 2)
  # page_number = request.GET.get('page')
  # page_obj = paginator.get_page(page_number)


  serializer=productsSeriliazer(productItem, many=True)
  serializer2=categorySerializer(categories, many=True)



  #context={'products':productItem, 'categories':categories, 'category_title':category_title}
  return Response({
        'productItem': serializer.data,
        'category': serializer2.data,
        'category_title':category_title,
    })





@login_required(login_url='login')
@api_view(['GET','POST'])
def productDetails(request,pk):
  product=products.objects.get(id=pk)

  product_serializer=productsSeriliazer(product,many=False)



  product_comment=product.comment_set.all()


 
  comment_serializer=commentSerializer(product_comment, many=True)


  if request.method=="POST":
      comment=Comment.objects.create(
      user=request.user,
      product=product,
      body=request.POST.get('body')
    )


  context={'product':product_serializer.data,'product_comment':comment_serializer.data}

  return Response(context)







@api_view(['GET','POST'])
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect('home')
    # else:
    #     form = UserForm()


    return Response("Registration successfull")




@api_view(['GET','POST'])
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


 
  return Response("Login successfull")







@login_required(login_url='login')
@api_view(['GET','POST'])
def DeleteComment(request, pk):
  comment=Comment.objects.get(id=pk)
  comment.delete()
  return Response("Delete successfull")





@login_required(login_url='login')
@api_view(['GET'])
def userLogout(request):
  logout(request)
  return redirect('home')




@login_required(login_url='login')
@api_view(['GET'])
def paymentPage(request):

  productId=request.GET.get('id')
  product=products.objects.get(id=productId)
  product_seriliazer=productsSeriliazer()
  context={'product':product_seriliazer.data}

  return Response(context)


@login_required(login_url='login')
@api_view(['GET'])
def addToCart(request):
  
  productId=request.GET.get('product-id')
  product=products.objects.get(id=productId)

  cart=Cart.objects.create(
    
    user=request.user,
    products=product
  )

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





@login_required(login_url='login')
@api_view(['GET'])
def showCart(request,pk):

  user=User.objects.get(id=pk)
  #product=products.objects.get(id=1)
  cartItem=Cart.objects.all()

  cart_serializer=cartSerializer(cartItem,many=True)  


  context={'cartItem':cart_serializer.data}
  return Response(context)









  
@login_required(login_url='login')
@api_view(['GET'])
def removeCart(request):
  id=request.GET.get('id')
  cart=Cart.objects.get(id=id)
  cart.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
@api_view(['GET','POST'])
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
@api_view(['GET','POST'])
def profilePage(request):
  id=request.user.id
  user=User.objects.get(id=id)
  user_serializer=userSeriliazer(user,many=False)



  try:
    details=userDetails.objects.get(user=request.user)
    

  except userDetails.DoesNotExist:
    details=None
  

  details_serializer=userdetailsSerializer(details,many=False)

  context={'user':user_serializer.data, 'details':details_serializer.data}



  return Response(context)











@api_view(['GET','POST','PUT'])
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


      
  return Response('updated')




