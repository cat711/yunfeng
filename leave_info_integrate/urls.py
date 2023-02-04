from django.urls import path
from . import views


urlpatterns = [
    # 127.0.0.1/leave

    path('admin_leave_info/', views.leave_info_integrate),
]
