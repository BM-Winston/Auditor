from django.conf import settings
from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('api/auditor/', views.AuditorView.as_view()),
    path('',views.home,name = 'home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('add_post/', views.add_post, name='add_post'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
