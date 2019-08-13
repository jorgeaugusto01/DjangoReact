from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo                     
from .serializers import TodoSerializer  


#@api_view(['GET', 'POST'])
@csrf_exempt
def todo_list(request):
    """
    Retorna as todo's list
    """
    if request.method == 'GET':
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def todo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class TodoView(viewsets.ModelViewSet):       
#     serializer_class = TodoSerializer        
#     queryset = Todo.objects.all()            


