from django.urls import path
from user.views import usermanagement , user_reservs , payment

urlpatterns = [
    path('account/' , usermanagement),
    path('reserve-detail/' , user_reservs),
    path('payment/' , payment)
]