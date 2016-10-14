from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Doufu

# Create your views here.

def index(request):
    lastest_doufu_list = Doufu.objects.all()[:]
    template = loader.get_template('doufu/index.html')
    context = {
        'lastest_doufu_list': lastest_doufu_list,
    }
    return HttpResponse(template.render(context, request))