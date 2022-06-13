from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('api/projects/', views.Project.as_views()),

]
