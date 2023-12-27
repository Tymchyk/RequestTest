from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Students
from .serializers import StudentsSerializer
from django.views.generic.edit import CreateView
from .forms import StudentsForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class IndexView(CreateView):
    template_name = 'index.html'
    form_class = StudentsForm
    model = Students

@method_decorator(csrf_exempt, name='dispatch')
class IndexResponses(View):
    def get(self, request, *args, **kwargs):
        students = Students.objects.all()
        students_serialize = StudentsSerializer(students, many= True)
        return JsonResponse(students_serialize.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        student = Students(student_name = data["student_name"], 
                           student_surname = data["student_surname"], 
                           student_age = data["student_age"])
        student.save()
        return JsonResponse({"success": "ok"})
    
@method_decorator(csrf_exempt, name='dispatch')
class IndexDeleteResponse(View):
    def delete(self, request,id):
        Students.objects.get(id = id).delete()
        return JsonResponse({"success": "ok"})

    