from django.shortcuts import render,redirect
from myweb1.models import contactus,post,comments,userprofile,passcode
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.timezone import now
from django.http import JsonResponse
import smtplib
from email.message import EmailMessage
from random import randint
# Create your views here.
def start(request):
    if request.user.is_anonymous:
         return render(request,'signup.html')
    return redirect("/home")
def loginid(request):
    if request.user.is_anonymous:
        return render(request,'login.html')
    return redirect("/home")
def home(request):
    #if request.user.is_anonymous:
       # return redirect('/first')
    postcontent=post.objects.all()[:3]
    context ={"posts":postcontent}
    return render(request, "home.html",context)
def allblogs(request):
    postcontent=post.objects.all()
    context ={"posts":postcontent}
    return  render(request, "allblogs.html",context)
def postview(request,slug):
    postshow=post.objects.filter(postslug=slug).first()
    comment=comments.objects.filter(post=postshow)
    if (postshow==None):
        return redirect("/allblogs")
    context={"postshow":postshow,"comments":comment}
    return  render(request, "postview.html",context)
def index(request,slug):
    if request.user.is_anonymous:
        return redirect('/first')
    postcontent=post.objects.all()[:3]
    context ={"posts":postcontent}
    return render(request, "home.html",context)

def signup(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        emailid=request.POST.get('email')
        username=request.POST.get('username')
        check=User.objects.all().filter(username=username).first()
        emailcheck=User.objects.all().filter(email=emailid).first()
        if check!=None:
            messages.error(request ,"Username is  already taken")
            return redirect("/first/signup")
        elif emailcheck!=None:
            messages.error(request ,"this email "+emailid+" already used")
            return redirect("/first/signup")
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if (password==cpassword):
            passcodes=randint(100000,999999) 
            pin=passcode(email=emailid,pin=passcodes)
            pin.save()
            msg=EmailMessage()
            msg['subject']="confirm email"
            msg['From']=""#your email
            msg['TO']=emailid
            msg.set_content("your Confirm code is \n"+str(passcodes))
            email =smtplib.SMTP_SSL("smtp.gmail.com",465)
            email.login("","")#your email ,pass
            email.send_message(msg)
            email.quit()
            context={"firstname":firstname,"lastname":lastname,"emailid":emailid,"username":username,"password":password,"cpassword":cpassword}
            return render(request, "signupconfirm.html",context)
        else :
            messages.error(request ,"password or username is invalid")
    return redirect("/first/signup")

def signuopconfirm(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        emailid=request.POST.get('email')
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        passcodes=request.POST['passcode']
        pin=passcode.objects.all().filter(pin=int(passcodes)).first()
        if pin is not None :
            pin.delete()
            newuser =User.objects.create_user(username,emailid,password)
            newuser.first_name=firstname
            newuser.last_name=lastname
            newuser.save()
            user=authenticate(username=username,password=password)
            login(request,user)
            profile=userprofile(firstname=firstname,lastname=lastname,email=emailid,username=username,user=request.user,slug=username)
            profile.save()
            msg=EmailMessage()
            msg['subject']="account created"
            msg['From']=""#your email
            msg['TO']=request.user.email
            msg.set_content("""hello user\n We hereby provide you a platform to read and write . Here you can give a life to your story, articles, poems. Whatever you think you can write to enlighten others . You can read articles on topics of your choice . If you are a beginer in writing then Soch is the ideal platform for you . We have started this intiative to support such beginers . As we are new in this field ,We promise you that we would upgrade our tools according to writer in no time.
            Thank you for connecting with Soch !!
            Have a nice Day .
            Enjoy Writing""")
            msg.add_alternative("""<!DOCTYPE html>
            <html lang="en">
            <head>
            <title>
            ACCOUNT CREATED
            </title>
            </head>
            <body bgcolor="black" text="white">
            <h1 align="center"><font face="Cooper" color="blue">Hello user</font></h1>
            <p>Welcome to soch !! We hereby provide you a platform to read and write . Here you can give a life to your story, articles, poems. Whatever you think you can write to enlighten others . You can read articles on topics of your choice . If you are a beginer in writing then Soch is the ideal platform for you . We have started this intiative to support such beginers . As we are new in this field ,We promise you that we would upgrade our tools according to writer in no time.
            Thank you for connecting with Soch !!
            </p><p>Have a nice Day .</p>
            <p>Enjoy Writing . </p>
            </body>
            </html>
            """,subtype="html")
            email =smtplib.SMTP_SSL("smtp.gmail.com",465)
            email.login("","")#your email,pass
            email.send_message(msg)
            email.quit()
            logout(request)
            messages.success(request ,"Your account is created Successfully!!")
            return redirect("/first/")
        else:
            messages.error(request ,"passcode didnot match")
            context={"firstname":firstname,"lastname":lastname,"emailid":emailid,"username":username,"password":password,"cpassword":cpassword}
            return render(request,"signupconfirm.html",context)
    return render(request,"signupconfirm.html")




def logind(request):
    if request.method=='POST':
        email=request.POST.get('username')
        passwd=request.POST.get('name')
    user=authenticate(username=email,password=passwd)
    if user is not None:
        login(request,user)
        return redirect('/home')
    messages.error(request ,"Username or Password is Incorrect")
    return redirect('/first')



def logouts(request):
    logout(request)
    return redirect("/first")

def contact(request):
    if request.method=='POST':
        email=request.POST['email']
        querry=request.POST['querry']
        contact_us=contactus(email=email,contact=querry)
        contact_us.save()
        msg=EmailMessage()
        msg['subject']="Thank You for contacting us"
        msg['From']=""#your email
        msg['TO']=email
        msg.set_content("We will Reach you in 7-10 working days!! ")
        msg.add_alternative("""<!DOCTYPE html>
        <html lang="en">
        <head>
        <title>
        contact
        </title>
        </head>
        <body bgcolor="black" text="white">
        <p>We will  reach you in 7-10 working days!! </p>
        </body>
        </html>
        """,subtype="html")
        email =smtplib.SMTP_SSL("smtp.gmail.com",465)
        email.login("","")#your email ,pass
        email.send_message(msg)
        email.quit()
        messages.success(request ,"Your Response is recorded")
    return render(request, "contact.html")

def postcomment(request):
    if (request.method=="POST"):
        comment=request.POST.get("comment")
        user=request.user
        postslno=request.POST.get("postslno")
        postid=post.objects.get(slno=postslno)

    usercomment=comments(comment=comment,user=user,post=postid)
    usercomment.save()
    messages.success(request ,"Your comment is posted Successfully!!")
    return redirect("/allblogs/"+postid.postslug)

def deletefunction(request):
    if request.method=="POST":
        delete=request.POST["delete"]
        postslno=request.POST.get("postslno")
        postid=post.objects.get(slno=postslno)
        comment=comments.objects.get(idno=delete)
        comment.delete()
    return redirect("/allblogs/"+postid.postslug)

def profile(request,slug):

    if request.method=="POST":
        profiles=userprofile.objects.filter(slug=slug).first()
        if profiles.about!="":
            image=request.FILES['image']
            profiles.image=image
        else:
            image=request.FILES['image']
            about=request.POST["About"]
            profiles.about=about
            profiles.image=image
        profiles.save()
    profiles=userprofile.objects.filter(slug=slug).first()
    userpost=post.objects.all().filter(author=slug)
    if profiles==None:
        return redirect("/home")
    context={"profile":profiles ,"posts":userpost}
    return render(request ,"profile.html" ,context)


def createslug():
    j=randint(1000000,9999999)
    j="p"+str(j)
    posts=post.objects.all().filter(postslug=j).first()
    if posts is not None:
        createslug()
    return j

def addpost(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        user=request.user
        author=request.user.username
        slug=createslug()
        timestamp=now()
        Addpost=post(title=title,content=content,postslug=slug,user=user,author=author,timestamp=timestamp)
        Addpost.save()
        messages.success(request ,"Your post is added see you profile")
        return redirect("/allblogs/")
    return render(request,"addpost.html")

def changepassword(request):
    if request.method=="POST":
        currentpassword=request.POST["currentpassword"]
        newpassword=request.POST["newpassword"]
        confirmpassword=request.POST["confirmpassword"]
        user=authenticate(username=request.user.username,password=currentpassword)
        if user is not None :
            if newpassword==confirmpassword:
                user=User.objects.get(username=request.user.username)
                user.set_password(newpassword)
                username=user.username
                user.save()
                messages.success(request ,"password changed")
                user=authenticate(username=username,password=newpassword)
                login(request,user)
                return redirect ("/home")
            else:
                messages.error(request ,"password didnot match")
                return redirect("/changepassword")
        else:
            messages.error(request ,"current password is incorrect")
            return redirect("/changepassword")

    return render(request,"changepassword.html")

def deleteaccount(request):
    if request.user.is_anonymous:
         return redirect("/home/")
    if request.method=="POST":
        password=request.POST['password']
        user=authenticate(username=request.user.username,password=password)
        if user is not None:
            user=User.objects.get(username=request.user.username)
            user.delete()
            messages.success(request ,"Account Deleted")
            return redirect("/home/")
        else:
            messages.error(request ,"Incorrect Password")
    return render(request,"deleteaccount.html")

def deletepost(request):
    if request.method=="POST":
        slno=request.POST['slno']
        posts=post.objects.get(slno=slno)
        posts.delete()
        messages.success(request ,"Post Deleted")
        return redirect("/home/")
    else:
        return redirect("/home/")

def about(request):
    return render(request,"aboutus.html")

def jsonreq(request):
    posts=post.objects.all()
    collection={p.content : p.timestamp for p in posts}
    return JsonResponse(collection)
