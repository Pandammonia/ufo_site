from django.contrib import admin
from django.urls import path, include
from . import views 
from blog import urls
app_name = 'pages'
urlpatterns =  [
    path('', views.index, name='index'),
    path('are-aliens-demons-or-what/', views.are, name ='are'),
    path('userblog/', views.userposts, name="userposts"),
    path('intro/', views.intro, name='intro'),
    path('intro/cases/', views.introcases, name='introcases'),
    path('intro/theories/', views.introtheories, name='introtheories'),
    path('intro/brave_new_world/', views.braveneworld, name='brave_new_world'),
    path('sighting/', views.sighting, name='sighting'),
    path('fermi/', views.fermi, name='fermi'),
    path('theory/', views.theory, name='theory'),
    path('user_theories/', views.usertheories, name='usertheories'),
    path('user_theories/<int:th_id>/', views.theorydetail, name='thdetail'),
    path('user_blog_submit', views.userblog, name='userblog'),
    path('thanks/', views.thankyou, name='thanks'),
    path('user_sightings/', views.usersightings, name='usersightings'),
    path('user_sightings/<slug:st_id>/', views.sightdetail, name="stdetail"),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.bpostdetail, name="bpostdetail"),
    path('userblog/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.userpostdetail, name="userpostdetail"),
    path('thanks/', views.thankyou, name='thanks'),
    #blog section
]
