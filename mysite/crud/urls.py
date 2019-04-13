from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
  path('', views.index, name = 'index'),
  path('dzialy/', views.dzialy, name = 'dzialy'),
  path('dzialy/<int:dzial_id>/', views.dzial_details, name = 'dzial_details'),
  path('dzialy/<int:dzial_id>/delete', views.dzial_delete, name = 'dzial_delete'),
  path('dzialy/add', views.dzial_add, name = 'dzial_add'),
  path('dzialy/add/new', views.dzial_add_new, name = 'dzial_add_new'),
  path('dzialy/<int:dzial_id>/edit', views.dzial_edit, name = 'dzial_edit'),
  path('dzialy/dzial_edit/<int:dzial_id>', views.dzial_to_edit, name = 'dzial_to_edit')
]