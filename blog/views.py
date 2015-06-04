from django.shortcuts import render, redirect
from .models import Post
import math

def blog(request, page=1):
	# Context dictionary passed to template
	context_dict = {}

	# A list of every single blog post, sorted by creation date
	entry_list = Post.objects.order_by('-date')

	# The first post
	context_dict['latest_post'] = entry_list[0]

	# Creates a list of the rest of the posts
	context_dict['more_posts'] = entry_list[1:]

	return render(request, 'index.html', context_dict)

def post(request, post_slug):
	context_dict = {}

	# Try to render post with specific slug
	try:
		# Get the post with the specific slug
		post = Post.objects.get(slug=post_slug)
		context_dict['post'] = post
	except Post.DoesNotExist:
		# TODO - Render an error page: can't find page
		pass

	return render(request, 'blog-post.html', context_dict)

def about(request):
	return render(request, 'general/about.html')