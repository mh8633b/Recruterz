from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def jobs(request):
    return render(request, "jobs.html")


def details(request):
    return render(request, "details.html")
