from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1/leave
    path('exit/', views.user_exit),
    path('create/', views.create_leave),
    path('createu/', views.create_user),
    path('show/', views.leave_show),
]