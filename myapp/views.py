
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img': img, 'form': form})
  

def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    return JsonResponse({'message': 'Image deleted successfully'})

def download_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    response = HttpResponse(image.photo, content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{image.photo.name}"'
    return response
  