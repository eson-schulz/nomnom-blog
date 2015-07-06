from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Image, Author
from django.forms.extras.widgets import SelectDateWidget
import datetime

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=80)
	author = forms.ModelChoiceField(queryset=Author.objects.all())
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 170, 'rows': 40}))
	date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today)
	image = forms.ImageField()
	image2 = forms.ImageField(required=False)
	image3 = forms.ImageField(required=False)

	class Meta:
		model = Post
		fields = ('title', 'author', 'content', 'image', 'image2', 'image3', 'published', 'slug', 'date') 

class PostAdmin(admin.ModelAdmin):
	# How the posts are displayed in a list
	list_display = ('title', 'author', 'date', 'published')
	# Automatically generate slug based on title
	prepopulated_fields = {'slug':('title',)}
	# Organize posts by date
	ordering = ['-date']

	fieldsets = [
		(None, {'fields': ['published', 'title', 'author', 'content', 'image', 'image2', 'image3']}),
		('Advanced Information', {'fields': ['date', 'slug'], 'classes':['collapse']}),
	] 
	form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Image)