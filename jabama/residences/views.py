import jdatetime
from django.http import HttpResponse, JsonResponse

def all_residences(request):
    residences_list = [
        {"name": "Villa kordan", "price": 4000, "address": "kordan"},
        {"name": "Villa Sorkhab", "price": 10000, "address": "Sorkhab"},
        {"name": "Villa Sohelie", "price": 9000, "address": "Sohelie"},
        {"name": "Apartment Tehran", "price": 3500, "address": "Zaferanie"},
        {"name": "Apartment Karaj", "price": 4000, "address": "Azimiye"},
        {"name": "Apartment Tehran", "price": 3000, "address": "Azadi"},
    ]

    today = jdatetime.date.today()
    weekday = today.weekday()
    monthday = (today.month, today.day)

    official_holidays = [(1, 3), (1, 5), (1, 19), (6, 19)]

    result_time = []
    for res in residences_list:
        price = res["price"]

        if monthday in official_holidays:
            price = int(price * 1.2)

        elif weekday in [5, 6]:
            price = int(price * 0.8)

        result_time.append(
            f"name: {res['name']} | price: {price} | address: {res['address']}"
        )

    return HttpResponse("<br>".join(result_time))


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