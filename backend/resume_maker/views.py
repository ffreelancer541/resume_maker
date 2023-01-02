from django.shortcuts import render , HttpResponse
from .models import *
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from .renderers import User_renderer
from .serializers import *
from rest_framework.response import Response
from .tokens import get_tokens_for_user
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.generics import UpdateAPIView , ListAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ResgisterView(APIView):
    renderer_classes=[User_renderer]
    def post(self , request , format=None):
        serializer=RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token=get_tokens_for_user(user)
        return Response({"token":token , 'user_id':user.id ,"membership":'basic' , 'data':serializer.data} , status=status.HTTP_201_CREATED)

# class OtpView(APIView):
#     renderer_classes=[User_renderer]
#     def post(self , request, foramt=None ):
#         email=request.data['email']
#         otp=random.randint(1000 , 9999)
#         subject='Novaresume support'
#         message=f'We are excited to have you on board. Copy the following opt to continue {otp}'
#         to=email
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=backend.settings.EMAIL_HOST_USER,
#             recipient_list=[to , ],
#             fail_silently=True
#         )
#         return Response( {'otp':otp})



class LoginView(APIView):
    renderer_classes=[User_renderer]
    def post(self , request , format=None):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=request.data.get('email')
        password=request.data.get('password')
        
        user=authenticate(email=email , password=password)
        # serializer2=UserSerializer(data={'first_name':user.first_name , 'last_name':user.last_name ,'email':user.email, 'phone':user.phone })
        # serializer2.is_valid(raise_exception=True)
        # print(serializer2.data)

        group=Group.objects.get(name='Premium')

        if user is not None:
            token=get_tokens_for_user(user)
            if user.groups.filter(name=group).first():
                membership='Premium'
            else :
                membership='Basic'
            data={
                'first_name':user.first_name , 'last_name':user.last_name ,'email':user.email, 'phone':user.phone
            }
            return Response({"token":token  , "user_id":user.id , "membership":membership ,'data':data   } , status=status.HTTP_200_OK  )
        else:
            return Response(serializer.errors , status=status.HTTP_401_UNAUTHORIZED)

class UpdateUser(UpdateAPIView):
    renderer_classes=[User_renderer]
    queryset=User.objects.all()
    serializer_class=UpdateUserSerializer
    permission_classes=[IsAuthenticated]

class ResumePOST(APIView):
    def post(self , request , format=None):
        serializer=ResumePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ResumeTemplateView(ListAPIView):
    renderer_classes=[User_renderer]
    queryset=ResumeTemplates.objects.all()
    serializer_class=ResumeTemplateSerializer
