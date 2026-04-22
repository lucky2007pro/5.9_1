from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Commend
from .serializers import CommendSerializer

class CommendListCreateView(APIView):
    # GET: Barcha commend'larni ro'yxatini olish
    def get(self, request, format=None):
        commends = Commend.objects.all()
        serializer = CommendSerializer(commends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Yangi commend yaratish
    def post(self, request, format=None):
        serializer = CommendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommendDetailView(APIView):
    # Obyektni bazadan olish yoki 404 qaytarish uchun yordamchi funksiya
    def get_object(self, pk):
        return get_object_or_404(Commend, pk=pk)

    # GET: Bitta commend'ni olish
    def get(self, request, pk, format=None):
        commend = self.get_object(pk)
        serializer = CommendSerializer(commend)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: Bitta commend'ni to'liq yangilash
    def put(self, request, pk, format=None):
        commend = self.get_object(pk)
        serializer = CommendSerializer(commend, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH: Bitta commend'ni qisman yangilash
    def patch(self, request, pk, format=None):
        commend = self.get_object(pk)
        serializer = CommendSerializer(commend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Bitta commend'ni o'chirish
    def delete(self, request, pk, format=None):
        commend = self.get_object(pk)
        commend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
