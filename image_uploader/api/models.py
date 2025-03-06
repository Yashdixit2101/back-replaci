from django.db import models

class UploadedImage(models.Model):
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url