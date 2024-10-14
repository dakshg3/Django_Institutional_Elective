from django.shortcuts import render

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
# from social_core.actions import do_complete
# from social_django.utils import psa
# from social_django.views import NAMESPACE, _do_login
from django.contrib.auth import REDIRECT_FIELD_NAME
from electives.models import timer
from datetime import datetime, timezone


from django.contrib.auth import logout
def social_user(backend, uid, user=None, *args, **kwargs):
    '''OVERRIDED: It will logout the current user
    instead of raise an exception '''

    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}
            
def login_views(request):
    print("login_views")
    print(request)
    logout(request)
    hrs = timer.objects.values('hrs','mins')
    x=int(datetime.now().strftime('%H'))+5
    y=int(datetime.now().strftime('%M'))+30
    if(y>60):
        y=y%60
        x=x+1
    if(x>24):
        x=x%24
    x="{:02d}".format(x)
    y="{:02d}".format(y)
    context = {
		'hrs': hrs[0]['hrs'],
		'mins': hrs[0]['mins'],
		'curr':x,
		'currmins':y
		}
    return render(request, 'registration/login.html',context)
    

def logout1_views(request):
    return render(request, 'logout1.html')

def home_views(request):
    print("home_views")
    print(request)
    return render(request, 'home.html')


def home(request):
    print("home")
    print(request)
    return render(request, 'home.html')
