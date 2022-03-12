from audioop import reverse
import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.
def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)):
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif request.POST.get("newItem"):
            text = request.POST.get("new")
            
            if len(text) > 2:
                ls.item_set.create(text=text, complete=False)

            else:
                print("Invalid")


    return render(request, "main/list.html", {
        "ls": ls
    })


def home(request):
    return render(request, "main/home.html")


def create(request):
    form = CreateNewList()

    if request.method == "POST":
        form = CreateNewList(request.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()



    else:
        form = CreateNewList()

    return render(request, "main/create.html", {
            "form": form
        })