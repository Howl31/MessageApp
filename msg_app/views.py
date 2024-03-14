from django.shortcuts import render
from rest_framework.views import APIView
from .helpers import *


# Create your views here.

# Data Format

# {
#     "user": 2,
#     "msg": "Hi, Welcome to daily reminder",
#     "scheduled_date": "2024-03-14",
#     "scheduled_time": "12,37"
# }


class StoreMessages(APIView):
    def post(self, request):
        response = save_message_data(request)
        return response