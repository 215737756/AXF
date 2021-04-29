
from django.core.mail import send_mail
from django.template import loader

from axf_test.settings import EMAIL_HOST_USER


def sendEmail(email, name, token):
    subject = '激活'
    message = ''
    from_email = EMAIL_HOST_USER
    recipient_list = [email]  # 'YC0123AH@163.com'
    index = loader.get_template('user/register/testemail.html')

    context = {
        'name': name,
        'url': 'http://192.168.28.61:8000/axfuser/activate/?token='+str(token)
    }
    result = index.render(context=context)
    html_message = result
    send_mail(subject=subject, message=message, from_email=from_email,
              recipient_list=recipient_list, html_message=html_message
              )
