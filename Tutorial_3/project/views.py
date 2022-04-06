from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


# Create your views here.

def index(request):
    projects = Project.objects.all()

    return render(request, "project/index.html", {
        "projects": projects
    })


def project(request, pk):

    projectObject = None
    for i in projectsList:
        if i["id"] == str(pk):
            projectObject = i

    return render(request, "project/project.html", {
        "project": projectObject,
        "error": "This is something wrong!"
    })


def query(request):
    projectObj = Project.objects.all()

    tags = projectObj.tags.all()

    return render(request, "project/query.html", {
        "tag": tags
    })


def createProject(request):
    form = ProjectForm()

    if request.method == "POST":

        # Recreate an instance of that form and pass the data from the front end.
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")
        

    return render(request, "project/project-form.html", {
        "form": form
    })




def updateProject(request, pk):

    project1 = Project.objects.get(id=pk)
    form = ProjectForm(instance=project1)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project1)

        if form.is_valid():
            form.save()

            return redirect("index")



    return render(request, "project/project-form.html", {
        "form": form
    })




def deleteProject(request, pk):
    project2 = Project.objects.get(id=pk)

    if request.method == "POST":
        project2.delete()

        return redirect("index")


 
    return render(request, "project/delete.html", {
        "object": project2
    })