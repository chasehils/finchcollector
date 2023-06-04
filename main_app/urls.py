from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/add_photo', views.add_photo, name='add_photo'),
    path('finches/<int:finch_id>/assoc_birdhouse/<int:birdhouse_id>', views.assoc_birdhouse, name='assoc_birdhouse'),
    path('finches/<int:finch_id>/unassoc_birdhouse/<int:birdhouse_id>/', views.unassoc_birdhouse, name='unassoc_birdhouse'),
    path('birdhouses/', views.BirdhouseList.as_view(), name='birdhouses_index'),
    path('birdhouses/<int:pk>/',views.BirdhouseDetail.as_view(), name='birdhouses_detail'),
    path('birdhouses/create/',views.BirdhouseCreate.as_view(), name='birdhouses_create'),
    path('birdhouses/<int:pk>/update/',views.BirdhouseUpdate.as_view(), name='birdhouses_update'),
    path('birdhouses/<int:pk>/delete/',views.BirdhouseDelete.as_view(), name='birdhouses_delete'),
   
]