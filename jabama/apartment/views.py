from django.http import HttpResponse ,  JsonResponse

def apartment_list(request):
    apatments = [
        {"name": "Apartment Tehran", "price": 3500, "address": "Zaferanie"},
        {"name": "Apartment Karaj", "price": 4000, "address": "Azimiye"},
        {"name": "Apartment Tehran", "price": 3000, "address": "Azadi"},
    ]
    result = '<br>'.join(f'name : {a['name']} | Price : {a['price']} | address : {a['address']}' for a in apatments)

    return HttpResponse(result)

def apartment_list_json(request):
    apartments_json = [
        {"name": "Apartment Tehran", "price": 3500, "address": "Zaferanie"},
        {"name": "Apartment Karaj", "price": 4000, "address": "Azimiye"},
        {"name": "Apartment Tehran", "price": 3000, "address": "Azadi"},
    ]

    return JsonResponse(apartments_json , safe=False)