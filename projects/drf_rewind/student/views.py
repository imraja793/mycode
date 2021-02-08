from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import View

from student.models import Student


class CheckData(View):

    def get(self, request):
        a = Student.objects2.filter(is_student=False)
        print(a)
        return HttpResponse(a)

