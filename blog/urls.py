from django.urls import path
from . import views


# a list that lists all the urls that we will make points to html pages/views
# it is contained in the urlpatterns list

urlpatterns = [
    # Index or home page
    path('', views.post_list, name='post_list'),
    # Post detail page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit')
]