from django.db import models

# Create your models here.


class Task(models.Model):
    titles = models.CharField(max_length=200)
    descriptions = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
