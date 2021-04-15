from django.contrib import admin
from .models import Student, Teacher, Subject, Enrollment, Note

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):  
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin): 
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin): 
    pass