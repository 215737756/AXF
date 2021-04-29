from django.conf.urls import url

from Axfcart import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
]
