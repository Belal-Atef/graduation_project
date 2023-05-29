from django.db import models

# Create your models here.

# Beds = models.ForeignKey(bed, on_delete = models.CASCADE)
class room(models.Model):
    Room = models.CharField(max_length = 6, unique=True)
    notes_room = models.TextField(max_length = 3000, null= True ,blank= True)

    def __str__(self):
        return self.Room


class bed(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    number_bed = models.CharField(max_length = 4)
    Patient_name = models.CharField(max_length = 50, null = True ,blank= True)
    Patient_id = models.CharField(max_length = 14, null = True ,blank= True)
    Patient_gender = models.CharField(max_length = 10, choices= GENDER_CHOICES ,blank= True)
    age = models.IntegerField(blank= True, null = True)
    phone = models.CharField(max_length = 11, null = True ,blank= True)
    second_phone = models.CharField(max_length = 11, null = True ,blank= True)
    address = models.TextField(max_length = 100 ,blank= True )
    notes_bed = models.TextField(max_length = 3000, null= True ,blank= True)
    active = models.BooleanField(default = True)
    rooms = models.ForeignKey(room,on_delete = models.CASCADE)

    def __str__(self):
        return self.number_bed


