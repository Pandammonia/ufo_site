from django.db import models
from django.conf import settings
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

VISIBILITY = [
			('Visible', 'Visible'),
			('Hidden', 'Hidden'),
]

class Sighting(models.Model):
	subj = models.CharField(max_length=100)
	body = models.TextField()
	location = models.CharField(max_length=100)
	added = models.DateTimeField(auto_now_add=True)
	time_of = models.CharField(max_length=100)
	name = models.CharField(max_length=80, null=True, blank=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.subj
 	

class SightForm(ModelForm):
	class Meta:
		model = Sighting
		fields = ['subj', 'body', 'location', 'time_of']

class Theory(models.Model):

	VISBILITY = (
		('visible', 'Visible'),
		('hidden', 'hidden'),)

	theory_area = (
		('1', 'UFO/UAPs nature'),
		('2', 'Origins of UFO/Aliens'),
		('3', 'Where they come from'),
		('4', 'Their intentions'),
		('5', 'Other'),)


	Title = models.CharField(max_length=100)
	Subject = models.CharField(max_length=10,
							   choices=theory_area)
	Details = models.TextField()
	Name = models.CharField(max_length=100, blank=True, null=True)
	added = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20,
							  choices=VISIBILITY,
							  default='Visible')
	email = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.Title

class TheoryForm(ModelForm):
	class Meta:
		model = Theory
		fields = ['Title', 'Subject', 'Details', 'Name', 'email',]
		labels = {"Title": "Title",
				  "Name": "Name (optional)",
				  "email": "Email (optional)",}

class BlogPost(models.Model):

	STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),)

	title = models.CharField(max_length=100, unique=True)
	body = models.TextField()
	username = models.CharField(max_length=100, blank=True, null=True , default="Anonymous")
	added = models.DateTimeField(auto_now_add=True)
	email = models.CharField(max_length=100, blank=True)
	slug = models.SlugField()
	published = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def get_absolute_url(self):
		return reverse('pages:bpostdetail', args=[self.published.year,
												  self.published.month,
												  self.published.day,
												  self.slug])



