from django.contrib import admin
from courses.models import Class,Lesson,Subjects
# Register your models here.

admin.site.register(Class)
admin.site.register(Subjects)
admin.site.register(Lesson)

