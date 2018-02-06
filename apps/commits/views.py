from functools import wraps

from random import randint

from django.db.models import Count, F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.commits.models import Commit
from commitdb import settings


def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        password = request.COOKIES.get(settings.PAGE_ACCESS_COOKIE)
        password_correct = password == settings.PAGE_ACCESS_PASSWORD
        if not password_correct:
            return HttpResponseRedirect(settings.LOGIN_URL)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        response = HttpResponseRedirect('/')
        response.set_cookie(
            settings.PAGE_ACCESS_COOKIE, request.POST['password']
        )
        return response
    return render(request, 'login.html')


@login_required
def index(request: HttpRequest) -> HttpResponse:
    count = Commit.objects.aggregate(count=Count('git_hash'))['count']
    random_index = randint(0, count - 1)
    random_commit = Commit.objects.all()[random_index]
    return render(
        request,
        'index.html',
        {
            'commit': random_commit
        },
    )


@login_required
def browse(request: HttpRequest, git_hash: str) -> HttpResponse:
    commit = get_object_or_404(
        Commit,
        git_hash=git_hash
    )
    return render(
        request,
        'index.html',
        {
            'commit': commit,
            'browse': True,
        },
    )


@login_required
def vote_funny(request: HttpRequest, git_hash: str) -> HttpResponse:
    print('Voted FUNNY', git_hash)
    make_vote(git_hash, 'score_funny')
    return HttpResponseRedirect('/')


@login_required
def vote_not_funny(request: HttpRequest, git_hash: str) -> HttpResponse:
    make_vote(git_hash, 'score_not_funny')
    return HttpResponseRedirect('/')


def calculate_total_score(git_hash: str):
    Commit.objects.filter(git_hash=git_hash).update(
        score=F('score_funny') - F('score_not_funny')
    )


def make_vote(git_hash: str, score: str):
    Commit.objects.filter(git_hash=git_hash).update(**{score: F(score) + 1})
    calculate_total_score(git_hash)
