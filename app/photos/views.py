from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class GalleryView(APIView):
    def get(self, request):
        return render(request, 'photos/index.html')