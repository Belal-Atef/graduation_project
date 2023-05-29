from rest_framework import serializers
from . models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
   
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user
   
    class Meta:
        model=CustomUser
        fields= ('id', 'username', 'password', 'email', 'phone_number', 'age', 'job', 'gender', 'speciality', 'department', 'address', 'created_at', 'updated_at' )

    


    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)

    #     return user




class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = (user.email)
        token['is_staff'] = user.is_staff
        token['user'] = user.is_active

        return token