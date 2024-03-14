from .serializers import *
from rest_framework.response import Response


def save_message_data(request):
    serializer = UserMsgSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'msg': 'Message Data Saved Successfully.'}, status=200)
    else:
        err = {i: str(serializer.errors[i][0]) for i in serializer.errors}
        return Response({'status': 400, 'errors': err}, status=400)