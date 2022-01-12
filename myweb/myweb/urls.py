"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myweb1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authviews
from django.views.defaults import page_not_found
from myweb1.admin import admin_view
admin.site.admin_view=admin_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.loginid),
    path('first/login/', views.logind),
    path("home/",  views.home),
    path("first/signup/",views.start),
    path("signup/",views.signup),
    path("log/",views.logouts),
    path("contact/",views.contact),
    path("allblogs/",views.allblogs),
    path("home/Addpost/",views.addpost),
    path("home/<str:slug>",views.index),
    path("allblogs/<str:slug>",views.postview),
    path("postcomment",views.postcomment),
    path("deletecomment",views.deletefunction),
    path("home/profile/<str:slug>",views.profile),
    path("changepassword/",views.changepassword),
    path("resetpassword/",authviews.PasswordResetView.as_view(template_name="resetpassword.html"), name="reset_password"),
    path("resetpasswordsent/",authviews.PasswordResetDoneView.as_view(template_name="emailsent.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",authviews.PasswordResetConfirmView.as_view(template_name="resetpasswordpage.html"), name="password_reset_confirm"),
    path("passwordchanged/",authviews.PasswordResetView.as_view(template_name="passwordchanged.html"),name="password_reset_complete"),
    #changes
     path("deleteaccount/",views.deleteaccount),
     path("deletepost/",views.deletepost),
     path("signupconfirm/",views.signuopconfirm),
     path("aboutus/",views.about),
     path("json/",views.jsonreq),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
