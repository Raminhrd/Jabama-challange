from typing import Union
from django.http import HttpResponse

def usermanagement(request):
    userdetail : Union[str , int]= [
        {"username" : "srina" , "password" :'srina099489'},
    ]

    return HttpResponse(userdetail)