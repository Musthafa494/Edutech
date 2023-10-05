from django.urls import path
from courses import views

app_name="courses"

urlpatterns=[

    path('categories', views.course, name="course"),
    path('category/<int:category_id>/',views.category_courses,name='category_courses'),
    # path('Modules/<slug:cslug>/', views.Modules, name="Modules"),
    path('detail/<int:course_id>/', views.details, name="details"),
    path('abouts', views.about,name="about"),

]