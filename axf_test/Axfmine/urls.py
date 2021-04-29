from django.conf.urls import url

from Axfmine import views

urlpatterns = [
    url(r'^mine/', views.mine, name='mine'),
]
