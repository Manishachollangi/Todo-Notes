from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('list_api/', views.list_api),
    path('<int:pk>/', views.detail),
    path('add/', views.add),
    path('add_api/', views.add_api),
    path('<int:pk>/edit_api/', views.edit_api),
    path('<int:todo_id>/delete/', views.delete),
]