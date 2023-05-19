"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.conf.urls.i18n import urlpatterns as i18n_urls
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('language/', views.language_view, name='language'),
    path('logout/',views.logout,name='logout'),
    path('admin/', admin.site.urls),
    path('qr-code/', views.qr_code_view, name='qr_code'),
    path('services/', views.services, name='services'),
    path('service1/', views.service1, name='service1'),
    path('success/',views.success ,name='success'),
    path('service2/', views.service2, name='service2'),
    path('service3/', views.service3, name='service3'),
    path('service4/', views.service4, name='service4'),
    path('language_selection/', views.language_selection, name='language_selection'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

