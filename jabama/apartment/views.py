from django.http import HttpResponse ,  JsonResponse
import jdatetime

def apartment_list(request):
    apatments = [
        {"name": "Apartment Tehran", "price": 3500, "address": "Zaferanie"},
        {"name": "Apartment Karaj", "price": 4000, "address": "Azimiye"},
        {"name": "Apartment Tehran", "price": 3000, "address": "Azadi"},
    ]

    today = jdatetime.date.today()
    weekday = today.weekday()
    monthday = (today.month, today.day)

    official_holidays = [(1, 3), (1, 5), (1, 19), (6, 19)]

    result_time = []
    for a in apatments:
        price = a["price"]

        if monthday in official_holidays:
            price = int(price * 1.2)

        elif weekday in [5, 6]:
            price = int(price * 0.8)

        result_time.append(
            f"name: {a['name']} | price: {price} | address: {a['address']}"
        )

    return HttpResponse("<br>".join(result_time))

def apartment_list_json(request):
    apartments_json = [
        {"name": "Apartment Tehran", "price": 3500, "address": "Zaferanie"},
        {"name": "Apartment Karaj", "price": 4000, "address": "Azimiye"},
        {"name": "Apartment Tehran", "price": 3000, "address": "Azadi"},
    ]

    return JsonResponse(apartments_json , safe=False)