from . import views
from django.urls import path


urlpatterns = [
    
    path('',views.Home,name="home"),
    path('delete/<str:pk>/',views.DeleteComment,name='delete'),
    path('registration/',views.register,name="register"),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('details/<str:pk>/',views.productDetails, name="product-details"),
    path('payment',views.paymentPage,name='payment-page'),
    path('add-to-cart/',views.addToCart,name='cart'),
    path('cart/<str:pk>/',views.showCart,name='show-cart'),
    path('remove/',views.removeCart,name='remove-cart'),
    path('order-confirmed/',views.orderConfirmed,name='confirm-order'),
    path('profile/',views.profilePage,name='profile'),
    path('update/',views.updateProfile,name='update-profile')
   
]
