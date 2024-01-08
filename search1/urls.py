from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('image/', views.image, name="image"),
    path('advance/', views.advance, name="advance"),
]
