from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요. mybo에 오신걸 환영합니다")
