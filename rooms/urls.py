from django.urls import path ,include
from .views import RoomView,BedView
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('room',RoomView)
# router.register('bed',BedView)

urlpatterns = [
path('allroom',views.display_rooms,name='All_rooms'),
path('allbeds',views.display_beds,name='All_beds'),
path('createroom',views.add_room,name='Create_room'),
path('createbed',views.add_bed,name='Create_bed'),
path('showroom/<int:id>',views.display_one_room,name='Show_room'),
path('showbed/<int:id>',views.display_one_bed,name='Show_bed'),
path('updateroom/<int:id>',views.update_room,name='Update_room'),
path('updatebed/<int:id>',views.update_bed,name='Update_bed'),
path('deleteroom/<int:id>',views.delete_room,name='Delete_room'),
path('deletebed/<int:id>',views.delete_bed,name='Delete_bed'),
]