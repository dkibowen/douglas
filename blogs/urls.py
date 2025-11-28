from django.urls import path 
from . import views

urlpatterns = [
    path('<int:pk>',views.posts_by_category,name='posts_by_category'),
]