from django.shortcuts import render, redirect, get_object_or_404
from . import views
from .models import UserBlogPost, UserBlogPostForm
from django.contrib.auth.decorators import login_required

def index(request):
	posts = UserBlogPost.objects.all()
	context = {'posts':posts}
	return render(request, 'blog/index.html', context)

@login_required
def submitarticle(request):
	if request.method == 'POST':
		form = UserBlogPostForm(data=request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.author = request.user
			new_form.save()
			return redirect ('pages:thanks')
	else:
		form = UserBlogPostForm()
		context = {'form':form}
	return render(request, 'blog/submitarticle.html', context)

def userpostdetail(request, year, month, day, slug):
	post = get_object_or_404(UserBlogPost,
							 status='published',
							 published__year=year,
							 published__month=month,
							 published__day=day,
							 slug=slug)

	context = {'post': post}
	return render(request, 'blog/userpostdetail.html', context)


