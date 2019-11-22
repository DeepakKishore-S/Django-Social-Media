from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required # login required security purpose for normal viewe
from django.shortcuts import get_object_or_404 # object error
from .models import *
from django.contrib.auth.models import User # importing inbuilt User model
from .models import Profile as prof
from django.db.models import Q # for query to search the data
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm, CommentForm # importing form from form.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView # importing class based view
from django.contrib import messages
# used during change password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # for security purpose for class based views


#home
def index(request):

    return render(request, 'app/Home.html')


#sign up
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created Sucessfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
        add_form = ProfileUpdateForm()
    context = {
        'form': form,
    }
    return render(request,'app/register.html',context)

#my posts
@login_required
def mypost(request):
    logged_in_user_posts = Post.objects.filter(author=request.user)
    return render(request, 'app/myposts.html', {'posts': logged_in_user_posts})

#posts
@login_required
def posts(request):

    context = {
        'posts': Post.objects.all()
    }

    return  render(request,'app/Posts.html',context)

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'app/Posts.html'
    context_object_name = 'posts'
    ordering =  ['-last_modified']

#another user post
class UserListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'app/UserPost.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-last_modified')


#post details
@login_required
def postdetails(request, pk):
    posts = Post.objects.get(pk=pk)
    Comments = Comment.objects.filter(post=posts)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {
        'posts': posts,
        'form': form,
        'Comments':Comments

    }
    return  render(request,'app/detail.html',context)

# like the post
class PostLikeRedirect( LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        like_re_d = get_object_or_404(Post, *args, **kwargs)
        print(like_re_d)
        url = like_re_d.get_absolute_url()
        user = self.request.user
        auth = user.is_authenticated
        if auth == True:
            if user in like_re_d.like.all():
                like_re_d.like.remove(user)
            else:
                like_re_d.like.add(user)
        return url

# to add favourite
class PostFavouriteRedirect( LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        fav_re_d = get_object_or_404(Post, *args, **kwargs)
        url = fav_re_d.get_absolute_url()
        user = self.request.user
        auth = user.is_authenticated
        if auth == True:
            if user in fav_re_d.favourite.all():
                fav_re_d.favourite.remove(user)
            else:
                fav_re_d.favourite.add(user)

        return url

#Follow
class UserFollowRedirect( LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        follow_re_d = get_object_or_404(prof, *args, **kwargs)
        print(follow_re_d)
        url = follow_re_d.get_absolute_url()
        user = self.request.user
        fuser = prof.objects.get(user=user)
        auth = user.is_authenticated
        print(auth)
        print(follow_re_d.user.Follower)
        if auth == True:
            if user in follow_re_d.Follower.all():
                # print(user)
                follow_re_d.Follower.remove(user)
                # print(follow_re_d.user)
                fuser.Following.remove(follow_re_d.user)
                print('remove')
            else:
                print('add')
                follow_re_d.Follower.add(user)
                fuser.Following.add(follow_re_d.user)


        return url



#Delete post
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/Posts/'
    template_name = 'app/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'app/post_form.html'
    fields = ['title', 'subject',  'content', 'pic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'app/updatepost.html'
    fields = ['title', 'subject', 'content', 'pic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return  render(request,'app/profile.html',context)

#user profile view
@login_required
def Profiledetail(request):

    return render(request,'app/prof.html')


# another user profile view

@login_required
def userpage(request, id, *args, **kwargs):
    luser = request.user
    print(luser)
    profil = prof.objects.get(pk=id)
    user = User.objects.get(pk=profil.user_id)
    print(user)
    context = {'profile': profil,
               'user' : user,
                'luser': luser
               }

    return render(request, 'app/visitprof.html', context)



#password change view

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change_password.html', {
        'form': form
    })

# user search

def search(request):
    template = 'app/search.html'
    query = request.GET.get('q')
    search_user = User.objects.filter(Q(username__icontains=query))
    return render(request,template,{'users':search_user})

def search_posts(request):
    template = 'app/search_posts.html'
    querys = request.GET.get('q')
    search_post = Post.objects.filter(Q(title__icontains=querys)|Q(subject__icontains=querys))
    return render(request,template,{'posts':search_post})



def followings(request,pk):
     user = prof.objects.get(id=pk)
     followings=user.Following.all()
     print(followings)
     return render(request,'app/following.html',{'followings':followings})


def followers(request, pk):
    user = prof.objects.get(id=pk)
    followers = user.Follower.all()
    print(followings)
    return render(request, 'app/followers.html', {'followers': followers})

def followerspost(request, id):
    fposts = []
    obj = User.objects.get(id=id)
    name = obj.username
    print(name)
    user = prof.objects.get(user__username = name)
    print(user)
    print(user.user)
    followings = user.Following.all()
    for user in followings:
         posts = Post.objects.filter(author=user)
         for post in posts:
             fposts.append(post)
    print(fposts)


    return render(request,'app/followers_posts.html',{'posts':fposts })

def favourites(request,pk):
    user = request.user
    print(user)
    favourite = user.post_favourites.all()
    print(favourite)
    context = {
        'fav' : favourite
    }
    return render(request,'app/favourite.html',context)