from django.shortcuts import render, redirect, RequestContext, render_to_response
from .models import Post
import math

def blog(request, template='blog.html', short_template='blog_short.html', page=1):
	# Context dictionary passed to template
	context_dict = {}

	# Add the short template location
	context_dict['short_template'] = short_template

	# A list of every published post, sorted by creation date
	entry_list = Post.objects.order_by('-date').exclude(published=False)

	# The first post
	context_dict['latest_post'] = entry_list[0]

	# Creates a list of the rest of the posts
	context_dict['more_posts'] = entry_list[1:]

	# Used for endless post loading
	if request.is_ajax():
		template = short_template

	# Render the request
	return render_to_response(template, context_dict, context_instance=RequestContext(request))

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

# Simple about page
def about(request):
	return render(request, 'general/about.html')

# Simple index page
def index(request):
	return render(request, 'general/index.html')

# Simple contact page
def contact(request):
	return render(request, 'general/contact.html')