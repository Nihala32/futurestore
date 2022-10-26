from django.shortcuts import render

from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from postapi.serializers import UserSerializer,UserProfileSerializer,PostSerializer,CommentSerializer
from postapi.models import Userprofile,Posts,Comments
from rest_framework import permissions
from rest_framework.decorators import action

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = Userprofile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        serializer=UserProfileSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    # localhost:8000/api/user/profile/<pk>/add_followings
    @action(methods=["post"],detail=True)
    def add_followings(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user_to_follow=User.objects.get(id=id)
        profile=Userprofile.objects.get(user=request.user)
        profile.followings.add(user_to_follow)
        return Response({"messege":"ok"})

    @action(methods=["get"],detail=False)
    def my_followings(self,request,*args,**kwargs):
        user=request.user
        user_profile=Userprofile.objects.get(user=user)
        followings=user_profile.followings.all()
        serializer=UserSerializer(followings,many=True)
        return Response(serializer.data)





class PostsView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=["post"],detail=True)
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        user=request.user
        serializer=CommentSerializer(data=request.data,context={"post":post,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    @action(methods=["get"],detail=True)
    def get_comments(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        comments=post.comments_set.all()
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)

    # api/v1/post/<pk>/add_like
    @action(methods=["post"],detail=True)
    def add_like(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        post.liked_by.add(request.user)
        post.liked_by.all().count(request.user)
        return Response({"messege":"ok"})












