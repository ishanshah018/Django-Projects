from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('welcome/',views.welcome,name='welcome'),
    path('search/',views.search,name='search'),
    path('inform/<int:id>/',views.stu_information,name='inform'),
]
