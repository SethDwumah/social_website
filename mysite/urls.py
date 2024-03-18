
from django.urls import path
from .views import index, detail, post_list,category_list
urlpatterns = [
    path("",index, name='home'),
    path("<slug:slug>/",detail, name='detail'),
    path("post_list",post_list),
    path("category_list",category_list),
]
