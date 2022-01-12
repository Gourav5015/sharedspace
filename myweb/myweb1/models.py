from django.db import models
from django.utils.timezone import now
import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class myweb1(models.Model):
    login=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class contactus(models.Model):
    idno=models.BigAutoField(primary_key=True)
    email=models.CharField(max_length=50)
    contact=models.TextField()
    def __str__(self):
        return self.email

class post(models.Model):
    slno=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=RichTextField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    author=models.CharField(max_length=50)
    postslug=models.CharField(max_length=200)
    timestamp=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title+ " by "+self.author
    

class comments(models.Model):
    idno=models.BigAutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment

class userprofile(models.Model):
    idno=models.BigAutoField(primary_key=True)
    about=models.TextField(null=True ,default=None ,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    slug=models.CharField(max_length=100)
    image=models.ImageField(upload_to="myweb1/media",default="/myweb1/media/download.jpg",blank=True)
    #changes
    verification=models.BooleanField(blank=True,null=True,default=0)
    def __str__(self):
        return self.username

class passcode(models.Model):
    idno=models.BigAutoField(primary_key=True)
    email=models.CharField(max_length=70)
    pin=models.IntegerField()
    def __str__(self):
        return str(self.pin)

