from django.shortcuts import render
from .tasks import my_task
from django.http import JsonResponse

# Create your views here.
def show_page(request):
    return render(request, 'webs.html')

def taskDispatcher(request):
    task=my_task.delay(10)  # Start the task asynchronously
    return JsonResponse({'task_id': task.id},status=200)

def bubble_sort(arr):
    """
    Sorts a list of integers using the Bubble Sort algorithm.
    dfdfd
    
    Args:
    - arr (list of int): List of integers to be sorted.
    
    Returns:
    - list of int: Sorted list of integers.
    """
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr