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

def all_residences_Json(request):
    json_residences_list = {
         '1' : 'name : Villa kordan  price : 4000  addres : kordan' , 
         '2' : 'name : Villa Sorkhab  price : 10000  addres : Sorkhab' , 
         '3' : 'name : Villa Sohelie  price : 9000  addres : Sohelie' , 
         '4' : 'name : Apartment Tehran  price : 3500 addres: Zaferanie',
         '5' : 'name : Apartment Karaj  price : 4000 addres: Azimiye',
         '6' : 'name : Apartment Tehran  price : 3000 addres: Azadi',
    }
    return JsonResponse(json_residences_list)