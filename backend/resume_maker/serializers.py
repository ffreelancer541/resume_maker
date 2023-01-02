from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email' , 'first_name','last_name' ,'phone' ,  'tc' , 'password' ]
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        return  User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=255)
    class Meta:
        model=User
        fields=['email' , 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name' , 'last_name' , 'email' , 'phone' ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
class ResumePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields='__all__'

class ResumeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResumeTemplates
        fields='__all__'

