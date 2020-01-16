from django.db import models

class Show(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    network = models.CharField(max_length = 20)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)