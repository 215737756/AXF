from django.conf.urls import url

from Axfhome import views

urlpatterns = [
    url(r'^home/', views.home,name='home'),
]