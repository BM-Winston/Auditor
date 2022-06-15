from django.conf import settings
from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('api/auditor/', views.AuditorView.as_view()),
    path('home/',views.home,name = 'home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('add_post/', views.add_post, name='add_post'),
    path('profile/', views.profile, name='profile'),
    path('api_key/', views.api_key, name='api_key'),
    path('api/profile/', views.ProfileView.as_view()),
    path('add_project/', views.add_project, name='add_project'),
    path('projects/', views.projects, name='projects'),

    


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
