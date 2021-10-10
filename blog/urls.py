from django.urls import path,include
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('postblog', views.postblog, name='postblog'),
    path('blog', views.blog, name='blog'),
    path('Signup', views.managesignup, name='managesignup'),
    path('login', views.managelogin, name='managelogin'),
    path('logout', views.managelogout, name='managelogout'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('yourposts', views.yourposts, name='yourposts'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('update/<int:id>', views.update_post, name='update_post') ,
    path('discussion', views.discussions, name='discussion') ,
    path('discussion/postQ', views.postQ, name='postQ'),
    path('discussion-inside/<str:slugQ>', views.Qinside, name='Qinside'),  
    # path('discussion/postA', views.postA, name='postA') , 
    # path('Post_answers/<int:id>', views.postA, name='Post_answers') ,
     
   
       

]
