
from django.urls import path
from .views import index, detail, post_list,category_list, PostDetails,PostAPIView,GenericAPIview
urlpatterns = [
    path("",index, name='home'),
    path("<slug:slug>/",detail, name='detail'),
    path("post_list",post_list),
    path("category_list",category_list),
    path("details/<int:id>/",PostDetails.as_view()),
    path('post_view',PostAPIView.as_view()),
     path('generic_view/<int:id>/',GenericAPIview.as_view()),
]
