from django.contrib.auth import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from products.models import Cart, Category, Comment, products, userDetails

class productsSeriliazer(ModelSerializer):
  class Meta:
    model=products
    fields= '__all__'


class categorySerializer(ModelSerializer):
  class Meta:
    model=Category
    fields= '__all__'



class commentSerializer(ModelSerializer):
  class Meta:
    model=Comment
    fields= '__all__'


class cartSerializer(ModelSerializer):
  class Meta:
    model=Cart
    fields= '__all__'


class userSeriliazer(ModelSerializer):
  class Meta:
    model=models.User
    fields= '__all__'


class userdetailsSerializer(ModelSerializer):
  class Meta:
    model=userDetails
    fields='__all__'