from django.urls import path
from apartment.views import apartment_list , apartment_list_json

urlpatterns = [
    path('list/' , apartment_list),
    path('json-list/' , apartment_list_json)
]