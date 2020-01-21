from django.db import models
from login_app.models import User

class MessageManager(models.Manager):
    
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['message']) < 5:
            errors['message'] = "Message should have at least 5 characters!"
        return errors

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = "messages", on_delete = models.CASCADE)
    objects = MessageManager()

class CommentManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['comment']) < 2:
            errors['comment'] = "Comment should have at least 2 characters!"
        return errors

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    message = models.ForeignKey(Message, related_name = "comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = "comments", on_delete = models.CASCADE)
    objects = CommentManager()