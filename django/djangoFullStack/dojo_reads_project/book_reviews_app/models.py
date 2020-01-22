from django.db import models
from login_app.models import User

class AuthorManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['new_author']) <= 0:
            errors['new_author'] = "Author's name should be at least 1 character"
        if len(post_data['new_author']) > 100:
            errors['new_author'] = "Author's name cannot be longer that 100 characters"
        author = Author.objects.filter(name = post_data['new_author'])
        if len(author) != 0:
            errors['author_exist'] = "This author already exists"
        return errors

class BookManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) <= 0:
            errors['title'] = "Title should have at least 1 character"
        if len(post_data['title']) > 100:
            errors['title'] = "Title cannot be longer that 100 characters"
        return errors

class ReviewManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['review']) < 15:
            errors['review'] = "Review should be at least 15 characters long"
        if post_data['rating'] != '':
            if int(post_data['rating']) < 1 or int(post_data['rating']) > 5:
                errors['rating'] = "Rating should be between 1 and 5"
        else:
            errors['rating'] = "Rating is required; it should be between 1 and 5"
        return errors

class Author(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, related_name = "books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name = "reviews", on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name = "reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()