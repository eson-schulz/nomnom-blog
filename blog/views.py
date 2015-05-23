from django.shortcuts import render, redirect
from .models import Post
import math

def index(request, page=1):
	# Context dictionary passed to template
	context_dict = {}

	# Convert page to int
	page = int(page)

	# A list of every single blog post, sorted by creation date
	entry_list = Post.objects.order_by('-date')

	# If the page doesn't exist, redirect to the first page
	max_pages = int(math.ceil(len(entry_list) / 3.0))
	if (max_pages < page and page != 1):
		print "redirect"
		print max_pages + 1
		print page
		print max_pages + 1 < page
		return redirect('/')

	# Creates post 1, 2, and 3 if they exist
	for i in range(0, 3):
		if (len(entry_list) > ((page - 1) * 3) + i):
			context_dict['post' + str(i + 1)] = entry_list[(page - 1) * 3 + i]

	# Links next page if exists
	if page > 1 and page != 2:
		context_dict['next_url'] = "/" + str(page - 1)
	elif page > 1 and page == 2:
		context_dict['next_url'] = "/"

	# Links last page if exists
	if page < max_pages:
		context_dict['past_url'] = "/" + str(page + 1)

	return render(request, 'index.html', context_dict)

def post(request):
	context_dict = {}

	post_list = Post.objects.order_by('-date')

	context_dict['post'] = post_list[0]

	return render(request, 'blog-post.html', context_dict)