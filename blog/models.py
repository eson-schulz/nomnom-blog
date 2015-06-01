from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Post(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()
	date = models.DateField(default=datetime.date.today)

	# Author of post
	author = models.ForeignKey('Author')

	# Image ontop of the post
	image = models.ImageField(upload_to='static/uploads/post/')
	image2 = models.ImageField(upload_to='static/uploads/post/', null=True, blank=True)
	image3 = models.ImageField(upload_to='static/uploads/post/', null=True, blank=True)

	# Slug to nicely format url
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=80)
	biography = models.TextField()

	picture = models.ImageField(upload_to='static/uploads/author/')

	def __unicode__(self):
		return self.name

class Image(models.Model):
	title = models.CharField(max_length=80)
	image = models.ImageField(upload_to='static/uploads/image/')

	def __unicode__(self):
		return self.title