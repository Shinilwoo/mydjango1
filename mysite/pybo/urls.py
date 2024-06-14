from django.contrib import admin
from django.urls import path,include
from pybo import views

app_name='pybo'
urlpatterns = [
    path('', views.home, name='home'), # http://localhost:8000 + http://localhost:8000/pybo
    path('greet/', views.greet),
    path('<int:question_id>/',views.detail,name='detail'),\
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
    path('question/create/',views.question_create, name='question_create'),
]
