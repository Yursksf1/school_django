from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student

# Create your views here.


def subject(request):
    subjects = Subject.objects.all()
    response = ''
    for subject in subjets:
        print(subject.name)
        response = response + ' ' + subject.name

    return HttpResponse(response)


def students(request):
    response = get_students()
    return JsonResponse(response)


def index(request):
    students = get_students()
    context = {
        'message': 'hola mundo',
        'students': students

    }

    return render(request, 'home.html', context)


def get_students():
    students = Student.objects.all()
    response = []
    for student in students:
        # print(student.first_name, student.last_name)
        student_response = {
            'full name': '{} {}'.format(student.first_name, student.last_name),
        }
        enrollments = student.enrollment_set.all()
        student_enrollment = []

        for enrollment in enrollments:

            average_enrollment = 0
            notes = enrollment.note_set.all()
            if notes:
                for note in notes:
                    average_enrollment = average_enrollment + note.value

                average_enrollment = average_enrollment / len(notes)
                student_enrollment.append(
                    {
                        'name': enrollment.subject.name,
                        'average': average_enrollment
                    }
                )

        student_response['enrollments'] = student_enrollment
        response.append(student_response)

    response = {'students': response}
    return response