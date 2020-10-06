from django.urls import path
from . import views

urlpatterns = [

    path('', views.show_blog, name='showblog'),
    path('<int:post_id>/', views.specific_post, name='specific_post'),

]