from django.shortcuts import render
from django.http import HttpResponse
from .models import Animals


def detail(request, question_id):
    animal = Animals.objects.get(name="cat")
    return HttpResponse("You're looking at question %s." % animal.pk)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
