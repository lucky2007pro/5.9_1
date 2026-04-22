from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class UserView(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello, World!'}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)

    def put(self, request, format=None):
        return Response({'message': 'User updated successfully!'}, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, request, pk, format=None):
        return Response({'message': f'User {pk} retrieved successfully!'}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        return Response({'message': f'User {pk} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)