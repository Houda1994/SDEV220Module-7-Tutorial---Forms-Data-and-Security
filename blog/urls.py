from django.urls import path
from . import views


# a list that lists all the urls that we will make points to html pages/views
# it is contained in the urlpatterns list

urlpatterns = [
    # index or home page
    path('', views.post_list, name='post_list'),
]