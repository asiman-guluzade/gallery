from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class GalleryView(APIView):
    def get(self, request, pk=None):
        return render(request, 'photos/test.html')
    
class PhotoView(APIView):
    def get(self, request, pk=None):
        return render(request, 'photos/Photo.html')