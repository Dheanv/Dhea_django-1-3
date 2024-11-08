from django.urls import path
from educourse_app import views

urlpatterns = [
    path('', views.index, name='index'),
]