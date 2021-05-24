from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import job
# from jobs.models import job
# Create your views here.


def jobs(request):
    jobs_content = job.objects.all()
    return render(request, "jobs.html", {'jobs_content': jobs_content})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def details(request):
    return render(request, "details.html")


def postjobs(request):
    if(request.method == "POST"):
        # print("fom btn clicked")
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        location = request.POST.get('location', '')
        experince = request.POST.get('experince', '')
        qualification = request.POST.get('qualification', '')
        # experince = request.POST.get('experince','')
        job_post = job(title=title, description=description, location=location,
                       experince=experince, qualification=qualification)
        job_post.save()
        return redirect("/")

    # if request.method == "POST":
    #     return render(request, "post_jobs.html")

    return render(request, "post_job.html")
