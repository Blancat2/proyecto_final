from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserEditForm, UserRegisterForm
from .models import Blogs


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('name_user')
            contra = form.cleaned_data.get('password')
            gmail = form.cleaned_data.get('email')

            usuario = authenticate(name_user=user, password=contra, email=gmail)

            if user is not None:
                login(request, usuario)

                

                return render(request, "AppUsers/index.html", {"mensaje":f"Bienvenido {user}"})

            else:
                return render(request, "AppUsers/index.html", {"mensaje": "Error, datos incorrectos"})

        else:
            return render(request, "AppUsers/index.html", {"mensaje":"Error, formulario erroneo"})


    form = AuthenticationForm()
    return render(request, "AppUsers/index.html", {'form':form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():

            name_user = form.cleaned_data['name_user']
            form.save()
            return render(request, "AppUsers/index.html", {"mensaje": "Usuario Creado"})
        
    else:
        form = UserRegisterForm()


    return render(request, "AppUsers/index.html", {"form":form})


def editar_perfil(request):

    user = request.user

    if request.method == 'POST':
        editarPerfiles = UserEditForm(request.POST)
        if editarPerfiles.is_valid:
            informacion = editarPerfiles.cleaned_data

            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return render(request, "AppUsers/index.html")  


    else:

        editarPerfiles = UserEditForm(initial={'email':user.email})


    return render(request, "AppUsers/editar_perfil.html", {"editarPerfiles":editarPerfiles, "user":user}) 

def __str__(self):
  return f"{self.user} - {self.imagen}"

def leer_blogs(request):

    blogs = Blogs.objects.all()
    contexto= {"blogs", blogs}

    if Blogs == None:
        return render(request, "AppUsers/blogs.html", {"mensaje": "No hay ningun blog todavia"})


    return render(request, "AppUsers/blogs.html", contexto)

def crear_blog(request):
    if request.method == 'POST':

        crearBlog = Blogs(request.POST)
        print(crearBlog)

        if crearBlog.is_valid:

            informacion = crearBlog.cleaned_data

            blog = Blogs (titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], imagen_user=informacion['imagen_user'])

            blog.save()

            return render(request, "AppUsers/blogs.html")
    
    else:
        crearBlog = Blogs()

    
    return render(request, "AppUsers/blogs.html", {"crearBlog":crearBlog})


def eliminar_blog(request, titulo):
    blog = Blogs.objects.get(title=titulo)
    blog.delete()

    blog = Blogs.objects.all()

    contexto = {"blog": blog}

    return render(request, "AppUsers/blogs.html", contexto)

def editar_blog(request, titulo):
    
    blog = Blogs.objects.get(title=titulo)

    if request.method == 'POST':

        editarBlog = Blogs(request.POST)

        print(editarBlog)

        if editarBlog.is_valid:
            informacion = editarBlog.cleaned_data

            blog.titulo = informacion['titulo']
            blog.subtitulo = informacion['subtitulo']
            blog.texto = informacion['texto']

            blog.save()

            return render(request, "AppUsers/blog.html")
        
    else:
        editarBlog = Blogs(initial={'titulo': blog.titulo, 'subtitulo': blog.subtitulo, 'texto': blog.texto})

    
    return render(request, "AppUsers/blogs.html", {"editarBlog": editarBlog, "titulo": titulo})
            
