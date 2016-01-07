from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django import forms;


class StudentName(models.Model):
    Student_Name = models.CharField(max_length=30)
    Level = models.CharField(max_length=30)
    Course = models.CharField(max_length=80)
    def __str__(self):
        return self.Student_Name
   
class Comment(models.Model):
    Student_Name = models.ForeignKey(StudentName)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.Student_Name
    def __str__(self):
        return self.comment



######Model form section#######
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentName;
        fields = ['Student_Name','Level','Course'];

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment;
        fields = ['Student_Name','comment'];    
    





