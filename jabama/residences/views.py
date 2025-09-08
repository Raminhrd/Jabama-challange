from django.shortcuts import render
from django.http.response import HttpResponse , JsonResponse

def all_residences(request):
    residences_list = [
        'name : Villa kordan  price : 4000  addres : kordan' , 
        'name : Villa Sorkhab  price : 10000  addres : Sorkhab' , 
        'name : Villa Sohelie  price : 9000  addres : Sohelie' , 
        'name : Apartment Tehran  price : 3500 addres: Zaferanie',
        'name : Apartment Karaj  price : 4000 addres: Azimiye',
        'name : Apartment Tehran  price : 3000 addres: Azadi',

    ]
    result = '<br>'.join(residences_list)
    return HttpResponse(result)