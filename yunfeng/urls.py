
from django.contrib import admin

import info_integrate.views
import login.views
import register.views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.views.user_login),
    path('register/', register.views.register),
    path('first/', include('firstapp.urls')),
    path('leave/', include('leave.urls')),
    path('adjust/', include('adjust.urls')),
    path('rank/', include('ranking.urls')),
    path('integrate/', info_integrate.views.info_integrate),
    path('admin_login/',include('admin_login.urls')),
]
