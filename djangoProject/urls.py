"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ww import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('kpi/', views.kpi),
    path('downloadKpi', views.download_kpi),
    path('getabort', views.get_abort_data),
    path('getqctlinterval', views.get_qc_tl_interval),
    path('getjobs', views.get_jobs),
    path('qcredis', views.qc_redis),
    path('artredis', views.art_redis),
    path('test', views.test),
    path('testj', views.test_js)
]
