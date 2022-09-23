from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('pages:index')
	else:
		form = CustomUserCreationForm()
	context = {'form':form}
	return render (request, 'registration/register.html', context)


# Create your views here.
