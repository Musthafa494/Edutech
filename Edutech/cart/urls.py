from django.urls import path
from cart import views
app_name='cart'


urlpatterns = [
    path('cartproducts/<int:p>',views.cartproducts,name='cartproducts'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('deleteitem/<int:p>',views.deleteitem,name='deleteitem'),
    path('cartremove/<int:p>',views.cartremove,name='cartremove'),
    path('order/',views.order,name='order'),
    path('orderview/',views.orderview,name='orderview'),
    path('content', views.content, name='content'),

]