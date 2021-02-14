from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index") ,
    path("shadman", views.shadman, name="shadman") ,
    path("<str:name>", views.greet, name="greet") 
]