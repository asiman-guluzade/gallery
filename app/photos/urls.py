from django.urls import path
from .views import GalleryView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', GalleryView.as_view(), name="gallery"),
    path('photo/<str:pk>', GalleryView.as_view(), name="gallery"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
