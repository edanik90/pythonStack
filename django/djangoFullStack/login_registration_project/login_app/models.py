from django.db import models
import re
from datetime import datetime, timedelta

class UserManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        current_date = datetime.now()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters long"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters long"
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
        try:
            birthday = datetime.strptime(post_data['birthday'], "%Y-%m-%d")
            if birthday > current_date:
                errors['birthday'] = "Birthday should be in the past"
            if birthday > current_date - timedelta(days=365*13):
                errors['birthday'] = "You have to be at least 13 years old to register!"
        except:
            errors['birthday'] = "You must provide a valid date"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 384)
    password = models.CharField(max_length = 60)
    birthday = models.DateField()
    objects = UserManager()