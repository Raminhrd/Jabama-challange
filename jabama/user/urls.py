from django.urls import path
from user.views import usermanagement , usermanagement_json , user_reservs, user_reservs_json , payment

urlpatterns = [
    path('account/' , usermanagement),
    path('account-json/' , usermanagement_json),
    path('reserve-detail/' , user_reservs),
    path('reserve-json/' , user_reservs_json),
    path('payment/' , payment)
]