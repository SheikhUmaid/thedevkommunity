
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from devusers import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('devbase.urls')),

    #Auth system

    path("register/",user_view.register,name = 'register'),
    path("profile/",user_view.profile,name = 'profile'),
    path("profile/update/",user_view.profile_update,name = 'profile_update'),
    path("login/",auth_view.LoginView.as_view(template_name = "devusers/login.html"),name = 'login'),
    path("logout/",auth_view.LogoutView.as_view(template_name="devusers/logout.html"),name = "logout"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 