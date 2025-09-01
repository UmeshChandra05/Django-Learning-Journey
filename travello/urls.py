from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('destination/<str:name>/', views.destination_detail, name = 'destination_detail')
]
