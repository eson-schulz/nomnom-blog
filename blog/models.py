from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()

	# Optional image to the side of the post 
	image = models.ImageField(null=True, blank=True)

class Image(models.Model):
	image = models.ImageField()