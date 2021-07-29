from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Todo
import json




def list(request):
    return render(request,'todo/list.html')

def list_api(request):
    title = request.GET.get('title')
    pk = request.GET.get('id')
    if title:
        todo_list = json.loads(serializers.serialize('json', Todo.objects.filter(title__istartswith = title)))
    elif pk:
        todo_list = json.loads(serializers.serialize('json', Todo.objects.filter(pk = pk)))
    else:
         todo_list = json.loads(serializers.serialize('json', Todo.objects.all()))
    todo_list = [{**l['fields'], 'pk': l['pk']} for l in todo_list]
    return JsonResponse(todo_list, safe=False)

def detail(request, pk):
    return render(request,'todo/detail.html')

def add(request):
    return render(request,'todo/add.html')

@csrf_exempt
def add_api(request):
    data = json.loads(request.body)
    todo_obj = Todo(title = data['title'], description = data['description'])
    todo_obj.save()
    return JsonResponse(model_to_dict(todo_obj), safe=False)

@csrf_exempt
def edit_api(request, pk):
    data = json.loads(request.body)
    todo_obj = Todo.objects.get(pk = pk)
    todo_obj.title = data['title']
    todo_obj.description = data['description']
    todo_obj.save()
    return JsonResponse(model_to_dict(todo_obj), safe=False)

@csrf_exempt
def done_api(request, pk):
    todo_obj = Todo.objects.get(pk = pk)
    todo_obj.is_done = not todo_obj.is_done
    todo_obj.save()
    return JsonResponse(model_to_dict(todo_obj), safe=False)

@csrf_exempt
def delete(request, todo_id):
    return HttpResponse("You're voting on todo %s." % todo_id)
