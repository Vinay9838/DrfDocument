from datetime import date
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Employee


class UserRegistrationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegistrationSerializers, self).create(validated_data)


class EmployeeUpdateSerializer(serializers.Serializer):

    gender = serializers.ChoiceField(choices=['M','F','O'])
    blood_group = serializers.CharField(max_length=5, required=True)
    date_of_birth = serializers.DateField(required=True)
    country = serializers.CharField(required=False)
    photo = serializers.FileField(required=True)

    def validate_date_of_birth(self, value):
        if value and value > date.today() + relativedelta(years=-18):
            raise serializers.ValidationError('Invalid DOB')
        return value





