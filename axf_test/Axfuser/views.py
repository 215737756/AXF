import uuid

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from Axfuser.models import AxfUser
from Axfuser.view_helper import sendEmail


def register(request):
    requests = request.method
    if requests == 'GET':
        return render(request, 'user/register/register.html')
    elif requests == 'POST':
        user = AxfUser()
        user.username = request.POST.get('name')
        user.account = request.POST.get('name')
        user.password = request.POST.get('password')
        user.email = request.POST.get('emails')
        user.icon = request.FILES.get('icon')
        token = uuid.uuid4()
        user.token = token
        user.save()
        # 发送邮件
        sendEmail(email=user.email, name=user.account, token=token)

        return HttpResponse('注册成功')


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


def matchpassword(request):
    password = request.GET.get('password')
    print(password)
    data = {
        'password': password
    }

    return JsonResponse(data=data)


def testemail(request):
    # subject, message, from_email, recipient_list
    # 主题
    subject = '激活'
    # 邮箱内容
    message = '发送激活邮件'
    # 发送人
    from_email = 'TianLiuChun@163.com'
    # 接收人
    recipient_list = ['TianLiuChun@163.com', 'YC0123AH@163.com']

    # 加载文件 loader
    index = loader.get_template('user/register/testemail.html')

    # 渲染
    context = {
        'name': '郭总'
    }
    # 点 render 渲染模板
    result = index.render(context=context)

    # html 内容
    html_message = result

    send_mail(subject=subject, message=message, from_email=from_email,
              recipient_list=recipient_list, html_message=html_message
              )

    return HttpResponse('邮件发送成功')


def activate(request):
    user = AxfUser
    token = request.GET.get('token')
    print(token)

    u = user.objects.filter(token=token).first()
    print(u.activate)
    u.activate = True
    u.save()

    return HttpResponse('成功激活')
