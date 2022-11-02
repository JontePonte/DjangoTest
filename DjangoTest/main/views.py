
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList



def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if not ls in response.user.todolist.all():
        return render(response, "main/view.html", {})

    if response.method == "POST":
        # Save checkbox status
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        # Save new items
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)

    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"] # Unencrypts data
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        
        return HttpResponseRedirect(f"/{t.id}")

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})


def view(response):
    return render(response, "main/view.html", {})

