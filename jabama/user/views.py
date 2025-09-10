from typing import Union
import json
import os
from django.conf import settings
from django.http import HttpResponse , JsonResponse


def usermanagement(request):
    userdetail = [
        {"username": "srina", "password": "srina099489", "telephone": "09338486745"},
    ]

    result = "<br>".join([f"username: {u['username']} | password: {u['password']} | telephone: {u["telephone"]}" for u in userdetail])

    return HttpResponse(result)

def usermanagement_json(request):
    userdetail_json = [
        {"username": "srina", "password": "srina099489", "telephone": "09338486745"},
    ]

    return JsonResponse(userdetail_json , safe=False)


def user_reservs(request):
    reservs_deatil = [
        {"name" : "Vila kordan" , "date" :'10/6/1404' , "status" : "Reserved"}
    ]
    result = "<br>".join([f"name: {r['name']} | date: {r['date']} | status: {r["status"]}" for r in reservs_deatil])
    return HttpResponse(result)

def user_reservs_json(request):
    reservs_deatil_json = [
        {"name" : "Vila kordan" , "date" :'10/6/1404' , "status" : "Reserved"}
    ]

    return JsonResponse(reservs_deatil_json , safe=False)

def payment(request):

    file_path = os.path.join(settings.BASE_DIR, 'user', 'data.json')

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return JsonResponse(data, safe=False)