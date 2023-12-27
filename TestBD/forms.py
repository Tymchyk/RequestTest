from django.forms import ModelForm, TextInput,Textarea,NumberInput
from .models import Students
class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields=['student_name','student_surname','student_age']
        widgets = {
            'student_name': TextInput(attrs={"class": "form-control name", "placeholder":"Write student name"}),
            'student_surname': TextInput(attrs={"class": "form-control surname","placeholder":"Write student surname"}),
            'student_age':NumberInput(attrs={"class":"form-control age","placeholder":"Write student age"}),
        }