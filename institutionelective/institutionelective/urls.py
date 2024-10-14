"""institutionelective URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
#from pages.views import index_view, form_view
from .views import home, login_views, home_views, logout1_views
from templates import registration
from django.contrib.auth import views
from electives.views import options_view, insertdata_view, export_xls, finalform_view, adminlogin_view, adexport_view, uploaddata, changetime
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', login_views),
    path('adminlogin/', adminlogin_view),
    path('adexport/', adexport_view),
    path('insertdata/', insertdata_view),
    url(r'^auth/', include('social.apps.django_app.urls', namespace='social')), 
    url(r'^home/', options_view, name='home'),
    path('log/', logout1_views),
    path('admin/', admin.site.urls),
    url(r'^upload/',uploaddata),
    url(r'^changetime/',changetime),
    url(r'^export/', export_xls, name='export_users_xls'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


