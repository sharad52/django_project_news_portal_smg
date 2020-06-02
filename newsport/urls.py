from django.urls import path
from .views import IndexView,detail,factorial


#giving app name
app_name = 'newsport'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('details/<int:news_id>/',detail,name="detail"),
    path('news/submit/',factorial,name="submit")
]