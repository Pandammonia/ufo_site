from django import forms
from .models import Sighting, BlogPost
from django.contrib.admin import widgets  
class SightingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SightingForm, self).__init__(*args, **kwargs)
		self.fields['subj'].label = "Summary of sighting"
		self.fields['body'].label = "Details of sighting"
		self.fields['location'].label = "Location of sighting"
		self.fields['name'].label = "Your name (optional)"
	class Meta:
		model = Sighting
		fields = ['subj', 'body', 'location', 'time_of', 'name']




