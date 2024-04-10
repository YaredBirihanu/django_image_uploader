from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('download_image/<int:image_id>/', views.download_image, name='download_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)