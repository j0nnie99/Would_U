from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Post,User,Join,Like
from .forms import PostForm
from django.core.paginator import Paginator
from community.models import Community,Scrap

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user
            post.save()
            return redirect('joinList')
    else:
        form = PostForm()
        return render(request, 'crud/new.html', {'form':form})

def main(request):
    join_list = Post.objects.all().order_by('-join_counting')[:10]
    like_list = Post.objects.all().order_by('-like_counting')[:10]
    return render(request, 'crud/main.html', {'joins': join_list, 'likes':like_list})

def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    plan_object = Post.objects.get(id=post_id)
    plan_object.view_counting = plan_object.view_counting+1
    plan_object.save()
    join = Join.objects.filter(user=request.user, post = post)
    like = Like.objects.filter(user=request.user, post = post)
    return render(request, 'crud/show.html', {'post': post, 'join':join, 'like':like})

def join(request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    joined =  Join.objects.filter(user=request.user, post=post)
    if not joined:
        Join.objects.create(user=request.user, post=post)
        post.join_counting += 1
        post.save()
    else:
        joined = Join.objects.get(user=request.user, post=post)
        post.join_counting -= 1
        post.save()
        joined.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def like(request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    liked =  Like.objects.filter(user=request.user, post=post)
    if not liked:
        Like.objects.create(user=request.user, post=post)
        post.like_counting += 1
        post.save()
    else:
        liked = Like.objects.get(user=request.user, post=post)
        post.like_counting -= 1
        post.save()
        liked.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def edit(request):
    return render(request,'crud/edit.html')

def blogupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('joinList')
    else:
        form  = PostForm(instance=post)
        return render(request, 'crud/edit.html',{'form':form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()  
    return redirect('joinList')

def search(request):
    post_object=Post.objects
    query=request.GET.get('query','') 
    if query:
        post_object=Post.objects.filter(title__icontains=query)
        body_object=Post.objects.filter(content__icontains=query)
        return render(request,'crud/searchList.html',{'result_title': post_object,'result_body':body_object,'query':query,})
    
def joinList(request):
    plans = Post.objects
    sort = request.GET.get('sort','')
    plan_list = Post.objects.all()
    if sort == 'join':
        plan_list = Post.objects.all().order_by('-join_counting', '-like_counting', 'created_at')
    elif sort == 'like':
        plan_list = Post.objects.all().order_by('-like_counting','-join_counting', 'created_at')
    elif sort == 'date':
        plan_list = Post.objects.all().order_by('-created_at')
    elif sort == 'view':
        plan_list = Post.objects.all().order_by('-view_counting', '-created_at')
    elif sort == 'writedate':
        plan_list = Post.objects.all().order_by('created_at')
    paginator = Paginator(plan_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'crud/joinList.html', {'plans':plans, 'posts':posts })   


def mypage(request) :
    username=request.user
    userpost=Post.objects.filter(username__username__endswith=request.user)
    userjoin=Join.objects.filter(user=request.user)
    userlike=Like.objects.filter(user=request.user)
    compost=Community.objects.filter(username__username__endswith=request.user)
    userscrap=Scrap.objects.filter(user=request.user)
    return render(request,'crud/mypage.html',{'username':username,'userpost':userpost,'userjoin':userjoin,'userlike':userlike,'compost':compost,'comscrap':userscrap})

def pay(request):
    plans = Post.objects.all
    charge = Post.objects.filter(charge=10000)
    title = Post.title
    return render(request, 'crud/pay.html', {'plans':plans, 'title':title, 'charge':charge})