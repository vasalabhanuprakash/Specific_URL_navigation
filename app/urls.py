from app.views import * 
from django.urls import path

app_name='sample'

urlpatterns=[

    path('Dhoni/',Dhoni,name='Dhoni'),
    
]
