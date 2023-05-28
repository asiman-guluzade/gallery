from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
# Create your views here.

class GalleryView(APIView):
    def get(self, request, pk=None):
        category = request.GET.get('category')
        if category is None:
            photos = Image.objects.all()
        else:
            photos = Image.objects.filter(category__name=category)
        categories = Category.objects.filter() 
        data = {'categories': categories, 'photos': photos}    
        return render(request, 'photos/test.html', data)
    
class PhotoView(APIView):
    def get(self, request, pk=None):
        photo = Image.objects.get(id=pk)

        return render(request, 'photos/Photo.html', {'photo':photo})
    
class AboutView(APIView):
    def get(self, request):
        return render(request, 'photos/about.html')