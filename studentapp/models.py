from django.db import models
from django.forms import CharField, DateInput
from studentapp.models import Students



# Create your models here.

class StudentDetails(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    joining_date=models.DateField(null=True)
    address=models.TextField()
    email=models.EmailField()
    qualification=models.CharField(blank=True,max_length=255)
    gender=models.CharField(blank=True,max_length=255)








class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'