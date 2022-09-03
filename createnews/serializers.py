from rest_framework.serializers import ModelSerializer
from createnews.models import NewsItem


class NewsItemSerializer(ModelSerializer):
    class Meta:
        model = NewsItem
        fields = [
            'title',
            'description',
            'creation_date',
            'id',
            'image'
        ]
