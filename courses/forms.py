from django import forms
from django.contrib.auth.models import User
from .models import Class,Subjects,Lesson



class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        help_texts = {
           'title': 'For example. Class 11 or Informatics Class',
            'desc':'Put a short description of the class',
            'image':'You can place a class photo or it can be left blank'
        }
        labels ={
            'desc':'Describe'
        }

class SubjectsForm(forms.ModelForm):
    class Meta:
        model =Subjects
        fields = ['creator','slug', 'title', 'classie', 'desc', 'image_subjects']
        help_texts = {
            'title': 'For example. Mathematics, Geography, etc.',
            'desc':'Put a brief description of the subject',
            'classie':'Select the class for which you will create the subject',
            'image_subjects':'You can place a photo of the subject or it can be left blank'
        }
        labels = {
            'title':'Title',
            'classie':'Class',
            'desc':'Describe'
        }
        widgets = {'creator': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'subjects', 'video_id', 'position']
        help_texts = {
            'title':'Set the lesson title',
            'subjects':'Choose the subject for which this lesson belongs',
            'video_id':'Set up a video ID from Youtube that you will upload (<a href="/media/youtube_help.png"> where I can find ID </a>)',
            'position':'Set the position number or the learning queue'
        }
        widgets = {
            'slug': forms.HiddenInput()
        }