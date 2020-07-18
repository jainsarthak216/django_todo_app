from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('update_task/<str:pk>', views.updateTask, name = "update"),
    path('delete_task/<str:pk>', views.delTask, name = "delete"),
    ]