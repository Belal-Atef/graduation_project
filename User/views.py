from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.permissions import AllowAny,IsAuthenticated
from . models import CustomUser
from .serializers import CustomTokenObtainSerializer
from django.shortcuts import get_object_or_404
import json

# Create your views here.


'''
This function is for desplaying all clients data
by bring data from database and serializer it in 
serializer.py file and return response data
'''
@api_view(['GET'])
def display_users(request):
    data=CustomUser.objects.all()                          # Client is a model  
    serilaizer=CustomUserSerializer(data,many=True)    #ClientViewSerializer is a serializer
    return Response(serilaizer.data)




'''
This function is for Adding all client .
by write the data of the new user .
serializer data and  saving it in database
'''
@api_view(["POST"])
def add_user(request):
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)



'''
This function for get specific user 
by bring data from database and serializer it in 
serializer.py file and return response data
'''
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def display_user(request,id):
    data=get_object_or_404(CustomUser,id=id)
    serializer=CustomUserSerializer(data).data          #ClientSerializer is a serializer
    return Response(serializer)




''' 
This function for updata data of specific
by replacing old data by new data 
and saving serializer data then it 
in database
'''
@api_view(['PUT'])
def update_user(request,id):
    data=get_object_or_404(CustomUser,id=id)
    serializer=CustomUserSerializer(data,data=request.data)  #ClientSerializer is a serializer
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)
    return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)




'''
this function for deleting the user
'''
@api_view(['DELETE'])
def delete_user(request,id):
    data=get_object_or_404(CustomUser,id=id)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)





class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenObtainSerializer
    permission_classes = ([AllowAny])
    def post(self, request, *args, **kwargs):

        try: 
            user_obj = CustomUser.objects.filter(email__iexact=request.data["email"]).first()
            requestData = request.data
            serializer = self.get_serializer(data=requestData)
            if serializer.is_valid(raise_exception=True):
                data = serializer.validated_data
                user = CustomUserSerializer(user_obj)
                data['user'] = user.data
                data['status'] = status.HTTP_200_OK
                data.pop('refresh', None)
                return Response(data, status=status.HTTP_200_OK)

        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        except KeyError as e:
            return Response({'message': ["send email and password", "status= "+str (status.HTTP_400_BAD_REQUEST) ]}, status=status.HTTP_400_BAD_REQUEST)

        except CustomUser.DoesNotExist:
            return Response({'message': ["Can't find user", "status= "+str (status.HTTP_404_NOT_FOUND)],}, status=status.HTTP_404_NOT_FOUND)

