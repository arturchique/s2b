from django.shortcuts import render
from django.views.decorators.http import require_GET
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.contrib.auth import get_user_model


class AdminView(APIView):
    def get(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        if worker.position == "w":
            animals = Animal.objects.filter(shelter=shelter)
            serializer = AnimalSerializer(animals, many=True)
            return Response({"data": serializer.data})
        elif worker.position == "a":
            return Response({"data": "Это админ приюта"})
        return Response({"data": "ok"})