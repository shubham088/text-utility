from django.urls import path, include
from . import views
urlpatterns = [
 path('', views.upload_image, name='upload_image'),
 path('image_gallary/', views.image_gallery, name='image_gallary')
]