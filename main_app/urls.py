from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('dogs/',views.index,name='index'),
    path('dogs/<int:dog_id>/',views.detail,name='detail'),
    path('dogs/create',views.DogCreate.as_view(),name='dogs_create'),
    path('dogs/<int:pk>/update/',views.DogUpdate.as_view(),name='dogs_update'),
    path('dogs/<int:pk>/delete/',views.DogDelete.as_view(),name='dogs_delete'),
    path('dogs/<int:dog_id>/add_price',views.add_price,name='add_price'),
    path('sports/',views.SportList.as_view(),name='sports_index'),
    path('sports/<int:pk>/',views.SportDetail.as_view(),name='sports_detail'),
    path('sports/create/', views.SportCreate.as_view(), name='sports_create'),
    path('sports/<int:pk>/update/', views.SportUpdate.as_view(), name='sports_update'),
    path('sports/<int:pk>/delete/', views.SportDelete.as_view(), name='sports_delete'),
    path('dogs/<int:dog_id>/assoc_sport/<int:sport_id>/', views.assoc_sport, name='assoc_sport'),
]