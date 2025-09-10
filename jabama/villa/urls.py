from django.urls import path
from villa.views import villa_list , villa_list_json

urlpatterns = [
    path('list/' , villa_list),
    path('json-list/' , villa_list_json)
]