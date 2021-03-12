from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from account.models import Articles
from api.serializers import ArticlesSerializer


class ArticlesViewSet(viewsets.ViewSet):
    def list(self, request):
        item = Articles.objects.all().order_by('-published_date', '-published_time')
        serializer = ArticlesSerializer(item, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            item = Articles.objects.get(id=id)
            serializer = ArticlesSerializer(item)
            return Response(serializer.data)
