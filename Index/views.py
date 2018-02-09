# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render 
from .models import Posts ,Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

# Create your views here.
def index(request):
    now = timezone.now()
    post = Posts.objects.order_by('posts_date')
    print post
    page = request.GET.get('page',1)
    paginator = Paginator(post, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'index/index.html',{'posts' : posts})

def post_detail(request,post_id):
    post_details = Posts.objects.filter(pk=post_id)
    images  = Image.objects.filter(gallery=post_id)
    context =  {
        'post_details' : post_details,
        'images'  : images

    }

    return render(request,'index/detail.html',context)