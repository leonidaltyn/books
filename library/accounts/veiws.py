from rest_framework.veiws import APIVeiw
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from accounts.serializers import UserSerializer
class UserRegistrationAPIView(APIView):
    def post(self,reqest):
        serializer=UserSerializer(data=reqest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)