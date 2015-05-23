from django.db import models
import datetime

class Post(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()
	date = models.DateField(default=datetime.date.today)

	# Image ontop of the post
	image = models.ImageField(upload_to='static/uploads/')
	image2 = models.ImageField(upload_to='static/uploads/', null=True, blank=True)
	image3 = models.ImageField(upload_to='static/uploads/', null=True, blank=True)

	def __unicode__(self):
		return self.title
		
class Image(models.Model):
	image = models.ImageField()