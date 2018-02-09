# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

 
 
def error_404(request):
        data = {}
        return render(request,'handle/error_404.html', data)
 
def error_500(request):
        data = {}
        return render(request,'handle/error_500.html', data)