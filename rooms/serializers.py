from rest_framework import serializers
from .models import room , bed

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = ('id','Room','notes_room')

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = bed
        fields = ('id','number_bed','Patient_name','Patient_id','Patient_gender','age','phone','second_phone','address','notes_bed','active','rooms')