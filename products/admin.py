from django.contrib import admin
from django.db.models.base import Model

from products.models import Cart, Category, UserForm, confirmedOrder, products, userDetails

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display=('productName', 'category')
  list_per_page=(20)


class confirmOrderAdmin(admin.ModelAdmin):
 
  list_per_page=(10)
  list_display=('productName','Price','user','Address','Phone')

  def Price(self,obj):
      return obj.productName.productPrice
  
  def Address(self,obj):
    return obj.address

  def Phone(self,obj):
    return obj.phone
      

  
    
    
  
 
  

  





admin.site.register(products,ProductAdmin)
admin.site.register(Category)
admin.site.register(confirmedOrder,confirmOrderAdmin)
