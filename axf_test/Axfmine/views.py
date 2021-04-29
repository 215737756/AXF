import json
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def mine(request):
    return render(request, 'axf/main/mine/mine.html')
    # a = {'name': 'zs', 'age': 15, }
    # result = json.dumps(a)
    # return HttpResponse(result)
