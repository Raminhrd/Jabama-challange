from django.urls import path
from residences.views import all_residences , all_residences_Json

urlpatterns = [
    path('list/' , all_residences),
    path('json-list/' , all_residences_Json)
]