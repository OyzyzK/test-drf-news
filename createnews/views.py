from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from createnews.models import NewsItem
from django.views import generic
from rest_framework.views import APIView

from createnews.serializers import NewsItemSerializer


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return NewsItem.objects.all()

def news_id(request, pk):
    context = dict(
        news_items=[NewsItem.objects.get(id=pk)]
    )
    return render(request, 'index.html', context)


def index(request):
    context = dict(
        news_items=NewsItem.objects.all()
    )
    return render(request, 'index.html', context)

class NewListJson(generics.ListAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

class NewIDJson(generics.RetrieveAPIView):
    serializer_class = NewsItemSerializer

    def get_queryset(self):
        return NewsItem.objects.filter(id=self.kwargs['pk'])


