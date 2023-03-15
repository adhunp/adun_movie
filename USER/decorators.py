from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def auth_user(func):
    def wrapper(request,*args,**kwargs):
        if not (request.session.get('u_id')):
            return redirect('USER:ulogin')
        else:
            return func(request,*args,**kwargs)
    return wrapper