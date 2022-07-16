from xml.parsers.expat import model
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import BooleanField

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank= True,unique=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_date = models.DateTimeField(default= timezone.now)
    active = models.BooleanField(default=True)