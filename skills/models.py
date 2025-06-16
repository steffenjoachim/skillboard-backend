from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  

    def __str__(self):
        return self.title

