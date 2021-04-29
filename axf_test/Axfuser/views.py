from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from Axfuser.models import AxfUser


def register(request):
    return render(request, 'user/register/register.html')


def login(request):
    return render(request, 'user/login/login.html')


def checkName(request):
    data = {
        'status': 200,
        'message': 'success'
    }

    name = request.GET.get('name')

    user = AxfUser.objects.filter(account=name)
    if user.exists():
        data['status'] = 201
        data['message'] = '用户名已存在'
        return JsonResponse(data=data)

    else:
        return JsonResponse(data=data)
