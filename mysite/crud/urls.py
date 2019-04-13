from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('dzialy/', views.dzialy, name = 'dzialy'),
  path('dzialy/<int:dzial_id>/', views.dzial_details, name = 'dzial_details'),
  path('dzialy/<int:dzial_id>/delete', views.dzial_delete, name = 'dzial_delete'),
]