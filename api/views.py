from .models import Todo
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class TodoView(APIView):
    def get(self, request:Request)->Response:
        pass