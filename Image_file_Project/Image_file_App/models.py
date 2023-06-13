from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    extraction_data = models.TextField(blank=True)
    scheduled_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)