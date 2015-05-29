from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Image
from django.forms.extras.widgets import SelectDateWidget
import datetime

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=80)
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 170, 'rows': 40}))
	date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today)
	image = forms.ImageField()
	image2 = forms.ImageField(required=False)
	image3 = forms.ImageField(required=False)

	class Meta:
		model = Post
		fields = ('title', 'content', 'image', 'image2', 'image3', 'slug', 'date') 

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	fieldsets = [
		(None, {'fields': ['title', 'content', 'image', 'image2', 'image3']}),
		('Advanced Information', {'fields': ['date', 'slug'], 'classes':['collapse']}),
	]
	form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
