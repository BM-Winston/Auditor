from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  Auditor
from .serializer import AuditorSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import RegisterForm, AuditorForm
import email
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User, Auditor,Profile


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()   

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})


def login(request):
    if request.method == 'POST':
       
        return redirect('auditor')

   
    return render(request,'registration/login.html')


@login_required(login_url='/accounts/login/') 
def add_post(request):
    if request.method == 'POST':
        form = AuditorForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
       
        return redirect('auditor')
    else:
        form=AuditorForm()

        return render(request,'add_post.html',{'form':form} )


class AuditorView(APIView):
     #base class for our API view function.
    def get(self, request, format=None):

        #define a get method 
        all_auditor = Auditor.objects.all()

        #serialize the Django model objects 
        serializers = AuditorSerializer(all_auditor, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        
        serializers = AuditorSerializer(data=request.data)

        # serialize the data in the request
        if serializers.is_valid():

            
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,) 