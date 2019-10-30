from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    date_pub = models.DateField()
    heading = models.CharField(max_length=20)
    content = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)