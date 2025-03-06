from django.urls import path
from .views import ImageUploadView, ImageListView, ImageDeleteView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('images/', ImageListView.as_view(), name='image-list'),
    path('images/<int:image_id>/', ImageDeleteView.as_view(), name='image-delete'),
]