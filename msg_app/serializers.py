from .models import *
from .serializers import *
from rest_framework import serializers


class UserMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'

