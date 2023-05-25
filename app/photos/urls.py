from django.urls import path
from .views import GalleryView, PhotoView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', GalleryView.as_view(), name="gallery"),
    path('photo/<str:pk>', PhotoView.as_view(), name="photo"),


]
