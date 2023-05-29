from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import room , bed
from .serializers import RoomSerializer ,BedSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class RoomView(viewsets.ModelViewSet):
     queryset = room.objects.all()
     serializer_class = RoomSerializer

class BedView(viewsets.ModelViewSet):
     queryset = bed.objects.all()
     serializer_class = BedSerializer
     



'''
This function is for desplaying all clients data
by bring data from database and serializer it in 
serializer.py file and return response data
'''
@api_view(['GET'])
def display_rooms(request):
    data=room.objects.all()                          # Client is a model  
    serilaizer=RoomSerializer(data,many=True)    #ClientViewSerializer is a serializer
    return Response(serilaizer.data)


@api_view(['GET'])
def display_beds(request):
    data=bed.objects.all()                          # Client is a model  
    serilaizer=BedSerializer(data,many=True)    #ClientViewSerializer is a serializer
    return Response(serilaizer.data)


'''
This function is for Adding all client .
by write the data of the new user .
serializer data and  saving it in database
'''
@api_view(["POST"])
def add_room(request):
        serializer=RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def add_bed(request):
        serializer=BedSerializer(data=request.data)
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
def display_one_room(request,id):
    data=get_object_or_404(room,id=id)
    serializer=RoomSerializer(data).data          #ClientSerializer is a serializer
    return Response(serializer)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def display_one_bed(request,id):
    data=get_object_or_404(bed,id=id)
    serializer=BedSerializer(data).data          #ClientSerializer is a serializer
    return Response(serializer)



''' 
This function for updata data of specific
by replacing old data by new data 
and saving serializer data then it 
in database
'''
@api_view(['PUT'])
def update_room(request,id):
    data=get_object_or_404(room,id=id)
    serializer=RoomSerializer(data,data=request.data)  #ClientSerializer is a serializer
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)
    return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_bed(request,id):
    data=get_object_or_404(bed,id=id)
    serializer=BedSerializer(data,data=request.data)  #ClientSerializer is a serializer
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)
    return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)



'''
this function for deleting the user
'''
@api_view(['DELETE'])
def delete_room(request,id):
    data=get_object_or_404(room,id=id)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def delete_bed(request,id):
    data=get_object_or_404(bed,id=id)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

