from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm
from .models import User, Community, Scrap
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.
def com_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.username = request.user  #로그인 안 한 유저에 대한 에러페이지 만들기
            community.save()
            return redirect('comList')
    else:
        form = PostForm()
        return render(request,'com_new.html',{'form':form})


def comList(request):
    plans = Community.objects
    sort = request.GET.get('sort','')
    plan_list = Community.objects.all()
    if sort == 'scrap':
        plan_list = Community.objects.all().order_by('-scrap_counting', '-pub_date')
    elif sort == 'view':
        plan_list = Community.objects.all().order_by('-view_count', '-pub_date')
    elif sort == 'date':
        plan_list = Community.objects.all().order_by('-pub_date')
    elif sort == 'writedate':
        plan_list = Community.objects.all().order_by('pub_date')
    paginator = Paginator(plan_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'com_list.html', {'plans':plans, 'posts':posts })    
   
##

####
def community(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    scrap = Scrap.objects.filter(user=request.user, post = post)
    plan_object = Community.objects.get(id=post_id)
    plan_object.view_count = plan_object.view_count+1
    plan_object.save()

    return render(request, 'com_detail.html', {'post': post, 'scrap':scrap})



def scraplist(request):
    scraps = Scrap.objects.filter(user=request.user)
    user = request.user
    paginator = Paginator(scraps,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'scraplist.html', {'scraps':scraps, 'posts':posts, 'user':user})

def scrap(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    scrapped = Scrap.objects.filter(user=request.user, post=post)
    if not scrapped:
        Scrap.objects.create(user=request.user, post=post)
        post.scrap_counting += 1
        post.save()
    else:
        scrapped = Scrap.objects.get(user=request.user, post=post)
        post.scrap_counting -= 1
        post.save()
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def com_update(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('community', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'detail.html',{'form':form})

def com_delete(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    post.delete()
    return redirect('comList')


