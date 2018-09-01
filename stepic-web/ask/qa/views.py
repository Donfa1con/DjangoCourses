from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question
from .forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login


def new(request):
    return render(request, 'qa/new.html', {})


def base(request):
    return render(request, 'qa/base.html', {})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return redirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def popular(request):
    try:
        page = int(request.GET.get("page", 1))
    except TypeError:
        page = 1
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {'questions': page.object_list,
                                               'page': page,
                                               'paginator': paginator, })


def index(request):
    try:
        page = int(request.GET.get("page", 1))
    except TypeError:
        page = 1
    questions = Question.objects.new()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'qa/index.html', {'questions': page.object_list,
                                             'page': page,
                                             'paginator': paginator, })


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
            return redirect(question.get_url())
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'qa/question_detail.html', {'question': question,
                                                       'form': form})
