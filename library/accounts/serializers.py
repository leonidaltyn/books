from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(write_only=True, required=True)
    last_name=serializers.CharField(write_only=True, required=True)
    email=serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self,valided_data):
        first_name=valided_data.pop(first_name)
        last_name=valided_data.pop(last_name)
        email=valided_data.pop(email)
        user=User.objects.create_user(**valided_data)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()
        return user