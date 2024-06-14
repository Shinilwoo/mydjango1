from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import QuestionForm
from .models import Question
from django.utils import timezone

def home(request):
    # question_list=Question.objects.all()
    # order_by('속성명'), order_by('-속성명')
    page=request.GET.get('page','1')
    question_list=Question.objects.order_by('-create_date')
    paginator=Paginator(question_list,10)
    page_obj=paginator.get_page(page)
    # context={'question_list':question_list}
    context={'question_list':page_obj}
    # return HttpResponse("안녕하세요. pybo에 오신걸 환영합니다")
    # return render(request,'pybo/index.html')
    return render(request,'pybo/question_list.html',context)

def detail(request,question_id):
    # question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'pybo/question_detail.html',context)

def answer_create(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:detail',question_id=question.id)

def question_create(request):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)# 임시저장
            question.create_date=timezone.now()
            question.save()#db에 저장
            return redirect('pybo:home')
    else: # 'GET'
        form=QuestionForm()
        context={'form':form}
        return render(request,'pybo/question_form.html',context)

    # return render(request,'pybo/question_form.html',
    #               {'form':form})

def greet(request):
    return HttpResponse("반갑습니다")