from django.shortcuts import render, redirect, get_object_or_404
from .forms import SightingForm
from .models import Theory, Sighting, TheoryForm, BlogPost
import praw


def index(request):

	reddit_authorized = praw.Reddit(client_id = "7Nf7jTPKSNpxjBfqMAh38g",
								client_secret="zzoJjXGRcM3JfCpL76jwuzgjaIBLMQ",
								user_agent="Luke",
								username="Pandammonia",
								password="Pandora17")
	subreddit = reddit_authorized.subreddit("UFOs")

	redposts = subreddit.hot(limit=5)
	posts_dict = {"Title":[], "Post Text":[], "ID":[], "Score":[], "Total Comments":[], "Post URL":[] }
	for post in redposts:
		posts_dict["Title"].append(post.title)
		posts_dict["Post Text"].append(post.selftext)
		posts_dict["ID"].append(post.id)
		posts_dict["Score"].append(post.score)
		posts_dict["Total Comments"].append(post.num_comments)
		posts_dict["Post URL"].append(post.url)

	posts = BlogPost.objects.all()
	context = {'posts': posts, 'posts_dict':posts_dict}
	return render(request, 'pages/index.html', context)

def bpostdetail(request, year, month, day, slug):
	post = get_object_or_404(BlogPost,
							 status='published',
							 published__year=year,
							 published__month=month,
							 published__day=day,
							 slug=slug)

	context = {'post':post}
	return render(request, 'pages/bpostdetail.html', context)
def are(request):
	return render(request, 'pages/are.html')

def intro(request):
	return render(request, 'pages/intro.html')

def introcases(request):
	return render(request, 'pages/introcases.html')

def introtheories(request):
	return render(request, 'pages/introtheories.html')

def braveneworld(request):
	return render(request, 'pages/brave_new_world.html')

def fermi(request):
	return render(request, 'pages/fermi.html')

def sighting(request):
	if request.method == 'POST':
		form = SightingForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:thanks')
	else:
		form = SightingForm()
	context = {'form':form}
	return render(request, 'pages/sighting.html', context)

def theory(request):
	if request.method == 'POST':
		form = TheoryForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:thanks')
	else:
		form = TheoryForm()
		context = {'form':form} 
	return render(request, 'pages/theory.html', context)

def usertheories(request):
	theories = Theory.objects.order_by('-added')
	context = {'theories':theories}
	return render(request, 'pages/usertheories.html', context)

def theorydetail(request, th_id):
	theory = Theory.objects.get(id=th_id)
	context = {'theory': theory}
	return render(request, 'pages/theorydetail.html', context)

def thankyou(request):
	return render(request, 'pages/thankyou.html')

def usersightings(request):
	sightings = Sighting.objects.all()
	context = {'sightings':sightings}
	return render(request, 'pages/sightings.html', context)

def sightdetail(request, st_id):
	sighting = Sighting.objects.filter(slug=st_id)
	context = {'sighting':sighting}
	return render(request, 'pages/sightingdetail.html', context)

def userblog(request):
	if request.method == 'POST':
		form = BlogForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:thanks')
	else:
		form = BlogForm()
		context = {'form':form}

	return render(request, 'pages/userblogsubmission.html', context)

def userposts(request):
	posts = UserBlogPost.objects.all()
	context = {'posts':posts}
	return render(request, 'pages/userblogs.html', context)


def userpostdetail(request, year, month, day, slug):
	post = get_object_or_404(UserBlogPost,
							 status='published',
							 published__year=year,
							 published__month=month,
							 published__day=day,
							 slug=slug)

	context = {'post': post}
	return render(request, 'pages/userpostdetail.html', context)