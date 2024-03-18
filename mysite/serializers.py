from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','slug']
   

       

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['category','title','slug','category']
  

