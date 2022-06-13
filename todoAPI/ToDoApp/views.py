from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


from ToDoApp.models import Tasks
from ToDoApp.serializers import TaskSerializer

# Create your views here.

@csrf_exempt
def taskAPI(request, id=0): 
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)

        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Successfully added task!", safe=False)
        return JsonResponse("Failed to add task.", safe=False)

    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task=Tasks.objects.get(TaskID=task_data['TaskID'])
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Successfully updated task!", safe=False)
        return JsonResponse("Failed to update task.", safe=False)

    elif request.method=='DELETE':
        print(id)
        task=Tasks.objects.get(TaskID=id)
        task.delete()
        return JsonResponse("Delete Successfully!",safe=False)
    