from django.db import models
from datetime import datetime

class ShowManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        current_date = datetime.now()
        filter_show = Show.objects.filter(title = post_data['title'])
        show_date = datetime.strptime(post_data['release_date'], "%Y-%m-%d")
        if len(post_data['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(filter_show) != 0:
            errors["filter_show"] = "Title already exists in the database"
        if len(post_data['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(post_data['description']) < 10 and len(post_data['description']) != 0:
            errors["description"] = "Description should be at least 10 characters"
        if show_date > current_date:
            errors["release_date"] = "Release date should be in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    network = models.CharField(max_length = 20)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()