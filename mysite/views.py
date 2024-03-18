from django.shortcuts import render
from .models import Category, Post
from django.http import HttpResponse, JsonResponse
from .serializers import PostSerializer,CategorySerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, 'mysite/index.html', context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post":post
    }
    return render(request, 'mysite/detail.html', context)

@csrf_exempt
def post_list(request):
    
    if request.method =='GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='POST':
        data = JsonResponse().parse(request)
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        


@csrf_exempt
def category_list(request):
    
    if request.method =='GET':
       
       cats =Category.objects.all()
       serializer = CategorySerializer(cats, many=True)
       return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='POST':
        data = JsonResponse().parse(request)
        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)