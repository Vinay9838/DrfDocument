from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import status, parsers
from drf_spectacular.utils import extend_schema,OpenApiResponse
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import UserRegistrationSerializers, EmployeeUpdateSerializer
from .models import Employee


# Create your views here.

class UserRegistrationView(APIView):
    parser_classes = [parsers.FormParser]
    
    @extend_schema(
        summary='User Registration',
        description="This is POST method api, in which user data will be created and using the same user instance one Employee instance will be created",
        request= UserRegistrationSerializers,
        responses={
            200: OpenApiResponse(description='Json Response'),
            400: OpenApiResponse(description='Validation error')
        }
    )
    def post(self,request): 
       user_serializers = UserRegistrationSerializers(data=request.data)
       if not user_serializers.is_valid():
           return Response({"errors":user_serializers.errors}, status.HTTP_400_BAD_REQUEST)
       user = user_serializers.save()
       token, created = Token.objects.get_or_create(user=user) 
       employee = Employee.objects.create(user=user)
       return Response({"message":"User registration completed", "token":token.key},status.HTTP_200_OK)
    

class EmployeeUpdateView(APIView):
    parser_classes = [parsers.MultiPartParser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary='Emplyee detail update',
        description='Update the employee details using basic authentication i.e. username and the password used during user registration',
        request= EmployeeUpdateSerializer,
        responses={
            200: OpenApiResponse(description='Json Response'),
            400: OpenApiResponse(description='Validation error')
        }
    )
    def post(self,request): 
       employee_serializers = EmployeeUpdateSerializer(data=request.data)
       if not employee_serializers.is_valid():
           return Response({"errors":employee_serializers.errors}, status.HTTP_400_BAD_REQUEST)
       
       gender = employee_serializers.validated_data['gender']
       blood_group = employee_serializers.validated_data['blood_group']
       date_of_birth = employee_serializers.validated_data['date_of_birth']
       country = employee_serializers.validated_data['country']
       photo = employee_serializers.validated_data['photo']
       user = request.user

       try:
           employee = Employee.objects.get(user=user)
           employee.gender = gender
           employee.blood_group = blood_group
           employee.date_of_birth = date_of_birth
           employee.country = country
           employee.photo = photo
           employee.save()
       except Employee.DoesNotExist:
           return Response({"error":"Employee detail not found!"}, status.HTTP_404_NOT_FOUND) 
      
       return Response({"message":"Data updated successfully"},status.HTTP_200_OK)
    