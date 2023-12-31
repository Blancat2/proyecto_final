"""
URL configuration for proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppUsers.views import login_request, register, editar_perfil, leer_blogs, editar_blog, eliminar_blog, crear_blog
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_request, name='Login'),
    path('register/', register, name = 'Register'),
    path('logout/', LogoutView.as_view(template_name='AppUsers/logout.html'), name = 'Logout'),
    path('editar_perfil/', editar_perfil, name='Editar_Perfil'),
    path('blogs/', leer_blogs, name= "Leer_blogs"),
    path('blogs/', crear_blog, name= "Crear_blogs"),
    path('blogs/', editar_blog, name= "Editar_blogs"),
    path('blogs/', eliminar_blog, name= "Eliminar_blogs"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)