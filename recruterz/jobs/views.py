from django.shortcuts import render
from django.http import HttpResponse
from .models import job

# Create your views here.


def jobs(request):
    jobs_content = job.objects.all()
    return render(request, "jobs.html",{'jobs_content': jobs_content})

def details(request):
    return render(request, "details.html")

def postjobs(request):
    # if request.method == "POST":
    #     return render(request, "post_jobs.html")

    return render(request, "post_job.html")
