from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=80)
	body = models.TextField()
	author = models.CharField(max_length = 80)
	email = models.EmailField()
	added = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={'slug':self.slug})

class Reply(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.CharField(max_length=80)
	added = models.DateTimeField(auto_now_add=True)