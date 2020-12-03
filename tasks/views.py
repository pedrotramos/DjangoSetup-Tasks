from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from rest_framework import serializers as rf_serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from tasks.models import Task


class TaskSerializer(rf_serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "pub_date", "description")


@api_view(["GET"])
def get_tasks(request):
    all_tasks = Task.objects.all()
    json = serializers.serialize("json", all_tasks)
    return HttpResponse(json, content_type="application/json")


@api_view(["GET"])
def get_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        return JsonResponse(model_to_dict(task), safe=False)
    except Task.DoesNotExist:
        raise Http404("Task not found! Double check the ID.")


def add_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(["PUT"])
def alter_task(request, task_id):
    try:
        taskToAlter = Task.objects.get(pk=task_id)
    except:
        raise Http404("Task does not exist")

    data = JSONParser().parse(request)
    if "title" in data:
        taskToAlter.title = data["title"]
    if "date" in data:
        taskToAlter.pub_date = data["pub_date"]
    if "description" in data:
        taskToAlter.description = data["description"]

    taskToAlter.save()

    return JsonResponse(model_to_dict(taskToAlter), status=201, safe=False)


@api_view(["DELETE"])
def remove_task(request, task_id):
    try:
        taskToRemove = Task.objects.get(pk=task_id)
        taskToRemove.delete()
    except Task.DoesNotExist:
        raise Http404("Task does not exist! Double check the ID.")
    return HttpResponse("Task successfully deleted!")


@api_view(["GET", "POST"])
def list_post(request):
    if request.method == "GET":
        get_tasks(request)
    else:
        add_task(request)


@api_view(["GET", "PUT", "DELETE"])
def get_put_del(request, task_id):
    if request.method == "GET":
        get_task(request, task_id)
    elif request.method == PUT:
        alter_task(request, task_id)
    else:
        remove_task(request, task_id)