from rest_framework import routers, serializers, viewsets
from .models import *


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['book_id', 'title', 'author',
        'genre', 'year_published', 'summary']


class ReviewsSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)

    class Meta:
        model = reviews
        fields = ['review_id', 'book_id', 'user_id',
        'review_text', 'rating']