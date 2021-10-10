from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User






# Create your models here.
class Contact(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    feedback=models.TextField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return ''+ self.name
    
class Blog(models.Model):
    
    head=models.CharField(max_length=500)
    body=models.TextField()
    blogger=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # bloggername=models.CharField(max_length=20)
    slug =models.SlugField(max_length=200)
    time=models.DateTimeField(default=timezone.now)
    
    

    def __str__(self):
        return self.head+ ' Written by ' +str(self.blogger)

class DiscussionQ(models.Model):
    head=models.CharField(max_length=500) 
    body=models.TextField()
    blogger=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    slugQ =models.SlugField(max_length=200)
    time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.head+ ' Written by ' +str(self.blogger)

class DiscussionA(models.Model):
    body=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(DiscussionQ,on_delete=models.CASCADE,null=False)
    time=models.DateTimeField(default=timezone.now)

# class posts(models.Model):
#     no=models.AutoField(primary_key=True),       
#     user=models.ForeignKey(User, on_delete=models.CASCADE) 
#     blog=models.ForeignKey(Blog,  on_delete=models.CASCADE)
#     time=models.DateTimeField(default=timezone.now)
