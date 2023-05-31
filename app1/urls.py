from app1.views import * 

from django.urls import path,include
app_name='sample1'

urlpatterns=[

    path('Hardik/',Hardik,name='Hardik'),
    path('Virat/',Virat,name='Virat'),

]
