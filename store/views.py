from django.http import HttpResponse
from rest_framework import routers, viewsets
from .models import *
from .prompts import *
from .service import send_to_open_ai
from .serializers import *
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def create(self, request, *args, **kwargs):
        request.data['summary'] = request.data.get("summary") if request.data.get("summary") else send_to_open_ai(
            Lib_prompt.format(request.data.get("title"), request.data.get("author")))
        obj = Books.objects.create(**request.data)
        obj.save()
        return Response({"id": obj.book_id, "title": obj.title, "author": obj.author,
            "ganer": obj.genre, "year_published": obj.year_published,
            "summary": obj.summary})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = reviews.objects.all()
    serializer_class = ReviewsSerializer

