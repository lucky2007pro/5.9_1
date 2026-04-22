from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CommendSerializer
from .models import Commend
# Create your views here.

class CommendView(APIView):
    def get(self, request, format=None):
        commends = Commend.objects.all()
        serializer = CommendSerializer(commends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommendCreateView(APIView):
    def post(self, request, format=None):
        serializer = CommendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        commend = Commend.objects.get(pk=pk)
        serializer = CommendSerializer(commend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        commend = Commend.objects.get(pk=pk)
        commend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        commend = Commend.objects.get(pk=pk)
        serializer = CommendSerializer(commend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)