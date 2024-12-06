from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploaded_notes, name='uploaded_notes'),
]