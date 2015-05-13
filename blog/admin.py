from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE

from .models import Post, Image

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=80)
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 200, 'rows': 40}))
	image = forms.ImageField()

	class Meta:
		model = Post
		fields = ('title', 'content', 'image') 

class PostAdmin(admin.ModelAdmin):
	form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(Image)