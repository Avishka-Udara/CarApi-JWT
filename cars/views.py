from django.http import JsonResponse
from .models import Car
from .serializers import CarSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated




@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def car_list(request):
    
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

@api_view(['GET','PUT','DELETE'])
def car_detail(request, pk):
    
    try:
        cars = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return JsonResponse({'message': 'The car does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CarSerializer(cars)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CarSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)