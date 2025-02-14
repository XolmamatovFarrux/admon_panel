from django.urls import path

from rootapp import views

urlpatterns = [
    path('index/',views.kurs,name='kurs' ),
    path('student/',views.students,name='student'),

]