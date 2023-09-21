"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from erp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/add',views.EmployeeCreateView.as_view(),name="emp_add"),
    path('',views.IndexView.as_view(),name="home"),
    path('employee/all',views.EmployeeListView.as_view(),name="emp_list"),
    path('employee/<int:pk>',views.EmployeeDetailView.as_view(),name="emp_detail"),
    path('employee/remove/<int:pk>',views.EmployeeDeleteView.as_view(),name="emp_delete"),
    path('employee/edit/<int:pk>',views.EmployeeEditView.as_view(),name="emp_edit"),
    path('register',views.RegistrationView.as_view(),name="register"),
    path('singin',views.SignInView.as_view(),name="singin"),
    path('singout',views.SignOutView.as_view(),name="singout"),
    path('emp/home',views.EmpHome.as_view(),name="emp_home"),
    path('course/add',views.CourseCreateView.as_view(),name="course_add"),
    path('course/all',views.CourseListView.as_view(),name="course_list"),
    path('course/<int:pk>',views.CourseDetailView.as_view(),name="course_detail"),
    path('course/<int:pk>/remove>',views.course_delete_view,name="course_delete"),
    path('course/<int:pk>/change',views.CourseEditView.as_view(),name="course_edit"),
    path('course/home',views.CourseHome.as_view(),name="course_home"),
    path('batches/add',views.BatchCreateView.as_view(),name="batch_add"),
    path('batches/<int:pk>/change',views.BatchEditView.as_view(),name="batch_edit"),
    path('students/add',views.StudentCreateView.as_view(),name="student_add"),
    path('students/all',views.StudentListView.as_view(),name="student_list"),
    path('students/<int:pk>',views.StudentDetailView.as_view(),name="student_detail"),
    path('students/edit/<int:pk>',views.StudentEditView.as_view(),name="student_edit"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
