from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    body = models.TextField()
    post_date = models.DateField()

    def __str__(self):
        return self.title