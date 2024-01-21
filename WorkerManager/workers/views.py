from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Worker
from .serializers import WorkerSerializer


# Endpoints for all workers including create and get all
@api_view(['GET', 'POST'])
def worker_list(request):
    if request.method == 'GET':
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoints for specific workers
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def worker_detail(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
    except Worker.DoesNotExist:
        return Response({"message": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = WorkerSerializer(worker, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        worker.delete()
        return Response({"message": "Worker deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
