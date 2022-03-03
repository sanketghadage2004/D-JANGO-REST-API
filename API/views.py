from functools import partial
import imp
from logging import exception
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from django.forms.models import model_to_dict
from API.models import Blog
from .serializers import BlogSerializer
from rest_framework import status
"""Api Views"""
from rest_framework.views import APIView
"""view set"""
from rest_framework.viewsets import ViewSet
# Create your views here.

"""API by using the PAIVIEW"""

class BlogAPI(APIView):
    serializer_class = BlogSerializer

    def get(self, request, blog_id=None):
        # responseList = [
        #     'GET',
        #     'this os a GET HTTP request',
        # ]
        if blog_id:
            try:
                blog = Blog.objects.values().get(id = blog_id)
                return Response(blog)
            except Blog.DoesNotExist:
                return Response({'message': 'data not found'},status=status.HTTP_404_NOT_FOUND)

            except Exception as e:
                return Response({'message': 'data not found'},status=status.HTTP_400_BAD_REQUEST)

        else:
            blogs = Blog.objects.values().all()
            return Response(blogs)

            # blogs = model_to_dict(blogs)

    def post(self, request, blog_id=None):
        # print(request.POST)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():

            
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            blogstatus = serializer.validated_data.get('status')

            Blog.objects.create(
                title = title,
                description = description,
                status = blogstatus

            )
            responseList = [
                'success !'
            ]
            return Response({'data':responseList})
        else:
            responseList = [
                'failed !'
            ]
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, blog_id = None):
        if blog_id:
            try:
                blog = Blog.objects.get(id = blog_id)
            except Blog.DoesNotExist:
                return Response({'message':'Data id not found'}, status = status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(blog, data = request.data)
            if serializer.is_valid():
                title = serializer.validated_data.get('title')
                description = serializer.validated_data.get('description')
                blogstatus = serializer.validated_data.get('status')
                blog.title = title
                blog.description = description
                blog.status = blogstatus
                blog.save()
                return Response({'message':'success'})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message','Blog id not found'}, status = status.HTTP_400_BAD_REQUEST)

       
    
    def patch(self, request, blog_id):
        if blog_id:
            try:
                blog = Blog.objects.get(id = blog_id)
            except Blog.DoesNotExist:
                return Response({'message':'Data id not found'}, status = status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(blog, data = request.data, partial = True)
            if serializer.is_valid():
                title = serializer.validated_data.get('title')
                description = serializer.validated_data.get('description')
                blogstatus = serializer.validated_data.get('status')
                if title:
                    blog.title = title
                if description:
                    blog.description = description
                if blogstatus is not None:
                    blog.status = blogstatus
                blog.save()
                return Response({'message':'success'})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message','Blog id not found'}, status = status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request,blog_id):
        if blog_id:
            try:
                Blog.objects.get(id  = blog_id).delete()
                return Response({"messgae":"success"})
            except Blog.DoesNotExist:
                return Response({"messgae":"data not found"}, status  = status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message':"blog_id is required"}, status = status.HTTP_400_BAD_REQUEST)



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserAuthApi(ObtainAuthToken):
    pass
    # renderer_classes = api_settings.DEFAULT_RENDER_CLASSES