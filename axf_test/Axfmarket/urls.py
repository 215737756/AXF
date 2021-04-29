from django.conf.urls import url

from Axfmarket import views

urlpatterns = [
    url(r'^market/', views.market, name='market'),
]
