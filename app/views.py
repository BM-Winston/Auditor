from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  Auditor
from .serializer import AuditorSerializer

# Create your views here.
def home(request):
    return render(request, 'home.html')

class AuditorView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_auditor = Auditor.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = AuditorSerializer(all_auditor, many=True)
        return Response(serializers.data)

def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = AuditorSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,) 