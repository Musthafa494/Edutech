from django.shortcuts import render,get_object_or_404
from courses.models import Course,Module


def course(request):
    categories=Course.objects.all()
    return render(request,'courses.html',{'categories':categories})
def category_courses(request,category_id):
    category=get_object_or_404(Course,pk=category_id)
    courses=Module.objects.filter(category=category)
    return render(request,'category.html',{'category':category, 'courses':courses})

def details(request,course_id):
    p=Module.objects.get(id=course_id)
    return render(request,'coursedetails.html',{'p':p})

def about(request):
      return render(request,'about.html')