from django.shortcuts import render
from django.http.response import Http404
from .models import *


def index(request):
    context = {}
    if "id" in request.GET:
        try:
            context["this_student"] = Student.objects.get(id=request.GET["id"])
        except Student.DoesNotExist:
            return Http404

    context["students"] = Student.objects.all()

    return render(request, "index.html", context)
