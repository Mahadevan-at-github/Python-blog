from tkinter.font import names

from django.urls import path

from userapp.views import userlistBookView
from . import views
from userapp.views import userlistBookView
from .views import createBlog, blogDetail, blogUpdate, deleteblog, bloglist

urlpatterns = [
    path('',views.userRegistration,name='create'),
    # path('home/',views.listBookView,name='home'),
    path('detail/<int:user_id>/',views.detailsView,name='details'),
    path('update/<int:user_id>/',views.update_user,name='update'),
    path('delete/<int:user_id>/',views.deleteView,name='delete'),
    path('login/',views.loginpage,name='login'),
    path('index/',views.index,name='index'),
    path('searchUser/',views.Search_User,name='search'),
    path('user_view/',views.user_view,name='user_view'),
    path('admin_view/',views.admin_view,name='admin_view'),
    path('logout/',views.logout_view,name='logout'),
    path('booklist/',userlistBookView,name='book-list'),
    path('createblog/',createBlog,name='create_blog'),
    path('blogdetails/',blogDetail,name='blog_list'),
    path('BlogUpdate/<int:blog_id>/',blogUpdate,name='blog_update'),
    path('blogDelete/<int:blog_id>/',deleteblog,name='blog_delete'),
    path('bloglist/<int:blog_id>/',views.bloglist,name='blog_detail'),
    path('blog/',views.blog,name='blog'),
    path('blog_delete/<int:blog_id>/',views.blogdelete,name='blog_Delete'),
    path('blogcontent/<int:blog_id>/',views.blogcontent,name='blog_content'),
    path('comment/<int:blog_id>/',views.blogComment,name='Comment'),
    path('blogdisplay/',views.blogdisplay,name='blogdisplay'),
]
