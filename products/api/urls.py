from . import views
from django.urls import path


urlpatterns = [
    path('',views.Home, name='home-api'),
    path('delete/<str:pk>/',views.DeleteComment,name='delete-api'),
    path('details/<str:pk>/',views.productDetails, name="product-details-api"),
    path('registration/',views.register,name="register-api"),
    path('login/',views.loginUser,name='login-api'),
    path('logout/',views.userLogout,name='logout-api'),
    path('payment',views.paymentPage,name='payment-page-api-api'),
    path('add-to-cart/',views.addToCart,name='cart-api'),
    path('cart/<str:pk>/',views.showCart,name='show-cart-api'),
     path('remove/',views.removeCart,name='remove-cart-api'),
    path('order-confirmed/',views.orderConfirmed,name='confirm-order-api'),
    path('profile/',views.profilePage,name='profile-api'),
    path('update/',views.updateProfile,name='update-profile-api')
]

