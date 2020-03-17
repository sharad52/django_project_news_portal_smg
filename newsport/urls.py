from django.urls import path
from .views import index


#giving app name
app_name = 'newsport'

urlpatterns = [
    path('',index,name='index'),
]