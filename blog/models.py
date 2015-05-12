from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
	title = models.CharField(max_length=80)
	content = HTMLField()

	# Optional image to the side of the post 
	image = models.ImageField(null=True, blank=True)

class Image(models.Model):
	image = models.ImageField()