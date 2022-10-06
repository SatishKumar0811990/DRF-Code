from django.shortcuts import render

from gs1.api.models import Student
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Model Object - Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')
