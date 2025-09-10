from django.urls import path
from user.views import usermanagement

urlpatterns = [
    path('account/' , usermanagement),
]