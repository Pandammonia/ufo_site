from django.db import models
from django.conf import settings
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


class UserBlogPost(models.Model):

	STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),)

	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	email = models.CharField(max_length=100, blank=True, null=True)
	published = models.DateTimeField(default=timezone.now)
	added = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique_for_date='published')
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(UserBlogPost, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:userpostdetail', args=[self.published.year,
												  self.published.month,
												  self.published.day,
												  self.slug])

class UserBlogPostForm(ModelForm):
	class Meta:
		model = UserBlogPost
		fields = ['title', 'body', 'email']
		labels = {"title": "Title",
				  "body": "Your post:",
				  "email": "Email (optional)",}
