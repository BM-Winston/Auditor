from django.shortcuts import render,redirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import AuditorSerializer, ProfileSerializer


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import RegisterForm, AuditorForm
import email
from django.contrib import messages
from .models import Auditor,Profile



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



# @login_required(login_url='/accounts/login/') 
# def add_post(request):
#     if request.method == 'POST':
#         form = AuditorForm(request.POST, request.FILES)
#         if form.is_valid():
#             post=form.save(commit=False)
#             post.save()
       
#         return redirect('auditor')
#     else:
#         form=AuditorForm()

#         return render(request,'add_post.html',{'form':form} )

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('login')



@login_required(login_url='/accounts/login/')
def add_project(request):
    if request.method=='POST':
        form = AuditorForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('projects')
    else:
        form = AuditorForm()
    return render(request,'add_project.html',{'form':form})


@login_required(login_url='/accounts/login/')
def projects(request):

    auditor = Auditor.objects.all()
    return render(request,'projects.html',{'auditor':auditor})

@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'flask' in request.GET and request.GET['flask']:
        searchTerm = request.GET.get('flask')
        auditorResults = Auditor.search_auditor(searchTerm)     
        return render(request,'search.html',{'results':auditorResults})

    else:
        message = 'You have not searched for any term'
        return render(request,'search.html',{'message':message})


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


class ProfileView(APIView):
     #base class for our API view function.
    def get(self, request, format=None):

        #define a get method 
        all_auditor = Profile.objects.all()

        #serialize the Django model objects 
        serializers = ProfileSerializer(all_auditor, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        
        serializers = ProfileSerializer(data=request.data)

        # serialize the data in the request
        if serializers.is_valid():

            
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,) 