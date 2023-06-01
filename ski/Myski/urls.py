from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('ajout', views.ajout),
    path('traitement', views.traitement)
    path('/affiche/<int:id>/',views.read),
path('/update/<int:id>/',views.update),
]