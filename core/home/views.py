from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializers = StudentSerializer(student_objs, many=True)
    return Response({'status': 200, 'payload': serializers.data})

@api_view(['POST'])
def post_student(request):
    serializers = StudentSerializer(data=request.data)
    if not serializers.is_valid():
        return Response({'status': 403, 'message': 'Something went wrong', 'errors': serializers.errors})
    
    serializers.save()
    return Response({'status': 200, 'payload': serializers.data, 'message': 'Student created successfully'})

@api_view(['PUT','PATCH'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializers = StudentSerializer(student_obj, data=request.data, partial=True)
        if not serializers.is_valid():
            return Response({'status': 403, 'message': 'Something went wrong', 'errors': serializers.errors})
        
        serializers.save()
        return Response({'status': 200, 'payload': serializers.data, 'message': 'Student updated successfully'})
    except Student.DoesNotExist:
        return Response({'status': 403, 'message': 'Invalid ID'})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message': 'Deleted Successfully'})
    except Student.DoesNotExist:
        return Response({'status': 403, 'message': 'Invalid ID'})
