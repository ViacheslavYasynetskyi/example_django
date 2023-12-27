from django.shortcuts import render

from my_app.models import Example


def index(request):
    list_examples = Example.objects.all()
    context = {
        "examples": list_examples
    }

    return render(request, "index.html", context=context)
