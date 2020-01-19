from django.db import models

class CourseManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 5:
            errors['name'] = "Course name should have at least 5 characters!"
        if len(post_data['description']) < 15:
            errors['description'] = "Description should be at least 15 characters long"
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.OneToOneField(Description, related_name = "course_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()