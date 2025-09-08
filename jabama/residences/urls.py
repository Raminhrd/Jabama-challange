from django.urls import path
from residences.views import all_residences

urlpatterns = [
    path('list/' , all_residences)
]