from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.jobs, name='jobs'),
    path('postjobs', views.postjobs, name='postjobs'),
    path('details', views.details, name='details')
]



