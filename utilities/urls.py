from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.text_utilities, name='text_utilities'),
    path('remove_punc', views.remove_punctuations, name="remove_punctuations"),
]
