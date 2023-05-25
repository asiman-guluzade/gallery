from django.urls import path
from .views import GalleryView

urlpatterns = [
    path('', GalleryView.as_view(), name="gallery"),
    path('photo/<str:pk>', GalleryView.as_view(), name="gallery"),


]
