from django.http import HttpResponse
from rest_framework import routers, viewsets
from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = reviews.objects.all()
    serializer_class = ReviewsSerializer



API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3.1-8B"
headers = {"Authorization": "Bearer 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"}



def query(request, payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
output = query({
    "inputs": "Can you please let us know more details about your ",
})