from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.


class Category(models.Model):
  name=CharField(max_length=100)


  def __str__(self) -> str:
      return self.name



class products(models.Model):
  productName=models.CharField(max_length=500)
  productDescription=models.TextField()
  productPrice=models.FloatField() 
  category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
  productImage=models.ImageField(upload_to='',null=True)
  

  def __str__(self) -> str:
      return self.productName








class UserForm(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'firstName form-control bg-white border-left-0 border-md','placeholder':'Enter first name'}),label='')
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'lastName form-control bg-white border-left-0 border-md', 'placeholder':'Enter last name '}),label='')
  username=forms.CharField(widget=forms.TextInput(attrs={'class': 'username form-control bg-white border-left-0 border-md', 'placeholder':'Enter username'}),label='')
  email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'email form-control bg-white border-left-0 border-md','placeholder':'Enter email'}),label='')
  password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'pwd2 form-control bg-white border-left-0 border-md',
        'placeholder':'Password'
        }
    ),label='')
  password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'pwd1 form-control bg-white border-left-0 border-md',
        'placeholder':'Confirm Password '
        }
    ),label='')
 
  class Meta:
        model = User
        
        fields = ('first_name','last_name', 'username', 'email','password1' ,'password2' )


class userDetails(models.Model):
  user=models.OneToOneField(User, on_delete=CASCADE,primary_key=True)
  phn=models.CharField(max_length=50,null=True)
  address1=models.CharField(max_length=200, null=True)
  address2=models.CharField(max_length=200,null=True)
  postcode=models.CharField(max_length=50, null=True)
  state=models.CharField(max_length=100, null=True)
  area=models.CharField(max_length=100,null=True)
  country=models.CharField(max_length=100,null=True)
  region=models.CharField(max_length=50, null=True)
 


  





class Cart(models.Model):
  products=models.ForeignKey(products, related_name='products', on_delete=models.CASCADE,null=True,blank=True)
  user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE,null=True,blank=True)



  def __str__(self) -> str:
      return self.user






  
  

  





class Comment(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(products,on_delete=models.CASCADE)
  body=models.TextField()
  updated=models.DateTimeField(auto_now=True)
  created=models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering=['-updated','-created']



class confirmedOrder(models.Model):
  productName=models.ForeignKey(products,on_delete=models.CASCADE, null=True)
  user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  address=models.CharField(max_length=500, null=True)
  phone=models.CharField(max_length=50,null=True)


