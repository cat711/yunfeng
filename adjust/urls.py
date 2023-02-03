from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1/adjust
    path('create/', views.create_adjust),
    path('query/', views.adjust_query),
    path('show/', views.adjust_show),
]