from django.shortcuts import render

from mysite import log_conf


def index(request):
    log_conf.log()
    return render(request, "hello.html", {})