from django.contrib import admin
from myweb1.models import myweb1
from myweb1.models import contactus,post,comments,userprofile,passcode
from django.http import Http404
from functools import update_wrapper
from myweb1.views import home

# Register your models here.
admin.site.register((myweb1,contactus,post,comments,userprofile,passcode))

def admin_view(view,cachable=False):
    def inner(request,*args,**kwargs):
        if not request.user.is_superuser:
            return home(request)
        return view(request,*args,**kwargs)
    return update_wrapper(inner,view)