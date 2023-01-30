from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1/first/test
    path('test', views.test_land),
]
