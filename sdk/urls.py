
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (PostListView, PostCreateView, PostUpdateView,
                    PostDeleteView,UserListView, PostLikeRedirect,
                    UserFollowRedirect, PostFavouriteRedirect)
from django.conf.urls import url
from . import views
from . import views as user_view # for creating userpage
from django.contrib.auth import views as auth_views # for login and logout for security

urlpatterns = [

    #Home
    url(r'^$', views.index, name='Home'),

    #signup and sign_in
    url(r'^signup$', user_view.register, name='sign_up'),
    url(r'^login$', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    url(r'^logout$', auth_views.LogoutView.as_view(template_name='app/Home.html'), name='logout'),

    #posts
    path('Posts/', PostListView.as_view(), name='posts'),
    url(r'^myposts$',views.mypost, name='my_post'),
    path('user/<str:username>/', UserListView.as_view(), name='userpost'),
    path('Posts/<int:pk>/', views.postdetails, name='detail'),
    path('<int:id>/Followers_Posts', views.followerspost, name='Followers_Posts'),
    path('Posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('Posts/<int:pk>/like', PostLikeRedirect.as_view(), name='post-like'),
    path('Posts/<int:pk>/favourite', PostFavouriteRedirect.as_view(), name='post-add-favourite'),
    path('<int:pk>/favourites', views.favourites, name='favourite'),
    path('Posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('Posts/create/', PostCreateView.as_view(), name='newpost'),

    #profile
    url(r'^profile$', user_view.Profiledetail, name='profile'),
    url(r'^edit_profile$', user_view.Profile, name='update_profile'),
    path('profile/<int:pk>/follwings', views.followings, name='followings'),
    path('profile/<int:pk>/follwers', views.followers, name='followers'),
    url(r'^profiles/(?P<id>[0-9]+)/$', views.userpage, name='userpage'),
    path('profiles/<int:pk>/follow', UserFollowRedirect.as_view(), name='user-follow'),


    #search
    url(r'^search_posts$', views.search_posts, name='search_posts'),
    url(r'^search$', views.search, name='search'),





    #change password
    url(r'^password/$', views.change_password, name='change_password'),

    #forgot password
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view
    (template_name='registration/password_reset_form.html'),
        name='password_reset'),

    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view
    (template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view
        (template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view
    (template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),


]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
