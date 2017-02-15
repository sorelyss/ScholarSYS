from django.forms import ModelForm
from django import forms
from apps.Students.models import Student




class StudentRegisterForm(ModelForm):
    name = forms.CharField(required=True)
    # pariente = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender= forms.CharField(required=True)


    class Meta:
        model = Student
        fields = ("name","age","gender","pariente")
        labels = {"name":"Name","age":"Age","gender":"Gender","pariente":"Relation"}

        

    def save(self, commit=True):
        student = super(StudentRegisterForm, self).save(commit=False)
        if commit:
            student.save()
        return student