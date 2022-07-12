from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('dogs/',views.index,name='index'),
    path('dogs/<int:dog_id>/',views.detail,name='detail')
]