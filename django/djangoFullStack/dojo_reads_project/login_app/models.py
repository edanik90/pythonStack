from django.db import models
import re

class UserManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters long"
        if len(post_data['alias']) < 2:
            errors['alias'] = "Alias should be at least 2 characters long"
        given_alias = User.objects.filter(alias = post_data['alias'])
        if len(given_alias) > 0:
            errors['invalid_alias'] = "This alias already in use"
        try: 
            User.objects.get(email = post_data['email'])
            errors['emails'] = "This email address is already taken"
        except:
            pass
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['invalid_email'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters long!"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords don't match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 384)
    password = models.CharField(max_length = 60)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)