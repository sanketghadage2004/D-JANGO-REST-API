from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from API.models import Blog
from .serializers import BlogSerializer
# Create your views here.

class BlogAPI(APIView):
    
    serializer_class = BlogSerializer

    def get(self, request):
        # responseList = [
        #     'GET',
        #     'this os a GET HTTP request',
        # ]

        blogs = Blog.objects.values().all()
        # blogs = model_to_dict(blogs)
        return Response({'data':blogs})


    def post(self, request):
        # print(request.POST)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():

            
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            status = serializer.validated_data.get('status')

            Blog.objects.create(
                title = title,
                description = description,
                status = status

            )
            responseList = [
                'success !'
            ]
            return Response({'data':responseList})
        else:
            responseList = [
                'failed !'
            ]
            return Response(serializer.errors)

    def put(swlf, request):
        responseList = [
            'PUT',
            'this is a PUT HTTP request',

        ]
        return Response({'data':responseList})
    
    
    def patch(swlf, request):
        responseList = [
            'PATCH',
            'this is a PATCH HTTP request',

        ]
        return Response({'data':responseList})
    
    
    def delete(swlf, request):
        responseList = [
            'DELETE',
            'this is a DELETE HTTP request',

        ]
        return Response({'data':responseList})
