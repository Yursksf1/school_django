from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


    def __str__(self):
        return '{} - {} - {}'.format(self.student, self.teacher, self.subject)

class Note(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.enrollment, self.value)









# class Estudiante(Person):
#     promedio = models.DecimalField(max_digits=5, decimal_places=2)
    
# class Profesor(Person):
#     pass

# class Materias(models.Model):
#     name = models.CharField(max_length=30)