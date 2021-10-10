from django.shortcuts import render, HttpResponse, redirect
from .models import Contact, Blog,DiscussionQ,DiscussionA
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import Update_blog


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):

    if request.method == 'POST':
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       feedback = request.POST['feedback']
       if len(phone) < 12 or phone.isdigit() == False:
          messages.warning(request,  'Enter Valid Details')
       else:
           messages.success(request,  'Successfully sent!')
           contactus = Contact(name=name, email=email,
                               phone=phone, feedback=feedback)
           contactus.save()

    return render(request, 'contact.html')


# authentication
def managesignup(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']

       if pass1 != pass2:
           messages.warning(request, 'Confirm password ,Try again')
           return redirect('index')

       useron = User.objects.create_user(username, email, pass1)
       useron.save()
       messages.success(request, 'Successfully Signed in')
       return redirect('index')

    else:
       return HttpResponse('Error ')


def managelogin(request):
    if request.method == 'POST':
       loginusername = request.POST['loginusername']
       loginpass = request.POST['loginpass']

       loginuser = authenticate(
           request, username=loginusername, password=loginpass)

       if loginuser is not None:
          login(request, loginuser)
          messages.success(request, 'Successfully Logged in')
          return redirect('index')

       else:
          messages.warning(request, 'Invalid Username or Password')
          return redirect('index')


def managelogout(request):

        logout(request)
        messages.success(request, 'Successfully Logged Out')

        return redirect('index')


def blog(request):
   allblogs = Blog.objects.all()
   params = {'allblogs': allblogs}
   return render(request, 'blog.html', params)


def blogpost(request, slug):
   post = Blog.objects.filter(slug=slug)
   allblogs = Blog.objects.all()
   context = {"post": post, 'allblogs': allblogs}

   return render(request, 'blogpost.html', context)


def postblog(request):
   if request.method == 'POST':
      head = request.POST['blogtitle']
      # bloggername=request.POST['bloggername']
      blogger = request.user
      body = request.POST['postbody']
      slug = request.POST['blogtitle']
      

      postBlog = Blog(head=head, blogger=blogger, body=body, slug=slug)
      postBlog.save()
      messages.success(request, 'Blog Posted')

   return render(request, "postBlog.html")


def yourposts(request):
   allblogs = Blog.objects.filter(blogger=request.user)
   params = {'allblogs': allblogs}
   return render(request, "yourposts.html", params)


def delete_post(request, id):
   if request.method == 'POST':
      delete = Blog.objects.get(pk=id)
      delete.delete()
      messages.success(request, 'Successfully Deleted')
   return redirect("yourposts")


def update_post(request, id):

         
   if request.method == 'POST':
      
      p=Blog.objects.get(pk=id)
      fm=Update_blog(request.POST,instance=p)
      if fm.is_valid():
         fm.save()
         messages.success(request, 'Successful')

   else:
      p=Blog.objects.get(pk=id)
      fm=Update_blog(instance=p)
   return render(request,"updatepost.html", {'Blog':p})  


def discussions(request):
   allQ = DiscussionQ.objects.all()
   params = {'allQ': allQ}
   return render(request,'discussions.html',params)

def postQ(request):
   if request.method == 'POST':
      head = request.POST['Qtopic']
      # bloggername=request.POST['bloggername']
      blogger = request.user
      body = request.POST['Qbody']
      slug = request.POST['Qtopic']
      

      postq= DiscussionQ(head=head, blogger=blogger, body=body, slugQ=slug)
      postq.save()
      messages.success(request, 'Topic Posted')

   return render(request,'discussion-postQ.html')

def Qinside(request,slugQ):
   B = DiscussionQ.objects.filter(slugQ=slugQ).first()
   A = DiscussionA.objects.filter(post=B)
   Q = DiscussionQ.objects.filter(slugQ=slugQ)
   count = DiscussionA.objects.filter(post=B).count()
   if request.method=='POST':
      body = request.POST.get('Abody')
      user=request.user
      p=request.POST.get('postSno')
      post=DiscussionQ.objects.get(id=p)
      
      Apost=DiscussionA(body=body,user=user,post=post)
      Apost.save()
      messages.success(request, 'Answer Posted')

   context = {'Q':Q,'A':A,'count':count}
   return render(request, 'discussion-inside.html', context)  

# def Ainside(request,slugQ):
#       Q = DiscussionQ.objects.filter(slugQ=slugQ)
#       context={'Q':Q}
#       return render(request, 'discussion-inside.html', context)    

# def postA(request):
#    A = DiscussionA.objects.all()
#    if request.method=='POST':
#       body = request.POST.get('Abody')
#       user=request.user
#       p=request.POST.get('postSno')
#       post=DiscussionQ.objects.get(id=p)
     
      
#       Apost=DiscussionA(body=body,uaer=user,post=post)
#       Apost.save()
#       messages.success(request, 'Answer Posted')
#    context = {'A':A}
#    return render(request,"discussion-inside.html",context)

#    # return redirect("discussion-inside/{{DiscussionQ.slugQ}}")

