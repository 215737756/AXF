

from django.shortcuts import render


# Create your views here.
from Axfhome.models import Wheel, AxfTopMenu, AxfMustBuy, AxfMainShow


def home(request):
    wheel_img = Wheel.objects.all()
    loop_top_menu = AxfTopMenu.objects.all()
    mustbuy_list = AxfMustBuy.objects.all()
    mainshows = AxfMainShow.objects.all()
    return render(request, 'axf/main/home/home.html', context=locals())
