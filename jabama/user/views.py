from typing import Union
import json
import os
from django.conf import settings
from django.http import HttpResponse , JsonResponse

def usermanagement(request):
    userdetail : Union[str , int]= [
        {"username" : "srina" , "password" :'srina099489'},
    ]

    return HttpResponse(userdetail)

def user_reservs(request):
    reservs_deatil = [
        {"name" : "Vila kordan" , "date" :'10/6/1404' , "status" : "Reserved"}
    ]

    return HttpResponse(reservs_deatil)

def payment(request):

    file_path = os.path.join(settings.BASE_DIR, 'user', 'data.json')

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return JsonResponse(data, safe=False)