from django.contrib import admin
from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index'),
	path('submit_article/', views.submitarticle, name='submitarticle'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.userpostdetail, name="userpostdetail"),
	


	]