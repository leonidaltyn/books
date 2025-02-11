from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from accounts.serializers import UserSerializer
from django.shortcuts import redirect
class UserRegistrationAPIView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('user_login')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserLoginAPIView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('book_list')
        return Response({'error':'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return redirect('user_login')
    def get(self,request):
        logout(request)
        return redirect('user_login')