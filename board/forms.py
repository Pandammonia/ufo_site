from django import forms
from .models import Post, Reply

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'author', 'email']
		labels = ['Post Title', 'Message', 'Name', 'Email']

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ['title', 'body', 'author']
		labels = []
