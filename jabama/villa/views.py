from django.http import HttpResponse , JsonResponse
import jdatetime


def villa_list(request):
    villas = [
        {"name": "Villa kordan", "price": 4000, "address": "kordan"},
        {"name": "Villa Sorkhab", "price": 10000, "address": "Sorkhab"},
        {"name": "Villa Sohelie", "price": 9000, "address": "Sohelie"},
    ]
    today = jdatetime.date.today()
    weekday = today.weekday()
    monthday = (today.month, today.day)

    official_holidays = [(1, 3), (1, 5), (1, 19), (6, 19)]

    result_time = []
    for v in villas:
        price = v["price"]

        if monthday in official_holidays:
            price = int(price * 1.2)

        elif weekday in [5, 6]:
            price = int(price * 0.8)

        result_time.append(
            f"name: {v['name']} | price: {price} | address: {v['address']}"
        )

    return HttpResponse("<br>".join(result_time))
        
def villa_list_json(request):
    villas_json = [
        {"name": "Villa kordan", "price": 4000, "address": "kordan"},
        {"name": "Villa Sorkhab", "price": 10000, "address": "Sorkhab"},
        {"name": "Villa Sohelie", "price": 9000, "address": "Sohelie"},
    ]
     
    return JsonResponse(villas_json ,  safe=False)