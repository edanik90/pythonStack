from django.db import models

class Wizard(models.Model):
    name = models.CharField(max_length = 45)
    house = models.CharField(max_length = 45)
    pet = models.CharField(max_length = 45)
    year = models.IntegerField()

    # def __repr__(self):
    #     return f"id={self.id}|| Wizard: {self.name}, House: {self.house}, Pet: {self.pet}, Year: {self.year}"