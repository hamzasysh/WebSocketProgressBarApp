from django.shortcuts import render
from .tasks import my_task
from django.http import JsonResponse

# Create your views here.
def show_page(request):
    return render(request, 'webs.html')

def taskDispatcher(request):
    task=my_task.delay(10)  # Start the task asynchronously
    return JsonResponse({'task_id': task.id},status=200)