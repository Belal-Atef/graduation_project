from django.urls import path
from . import views

urlpatterns=[
    path('all',views.display_users,name='All_users'),
    path('create',views.add_user,name='Create_user'),
    path('show/<int:id>',views.display_user,name='Show_user'),
    path('update/<int:id>',views.update_user,name='Update_user'),
    path('delete/<int:id>',views.delete_user,name='Delete_user'),

    # *******************************login*****************************
    path('login/token', views.CustomTokenView.as_view(), name='token_obtain_pair'),

    
]
