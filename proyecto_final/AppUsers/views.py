from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from forms import UserEditForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('name_user')
            contra = form.cleaned_data.get('password')

            usuario = authenticate(name_user=user, password=contra)

            if user is not None:
                login(request, usuario)

                #poner Inicio

                return render(request, "", {"mensaje":f"Bienvenido {user}"})

            else:
                return render(request, "", {"mensaje": "Error, datos incorrectos"})

        else:
            return render(request, "", {"mensaje":"Error, formulario erroneo"})


    form = AuthenticationForm()
    return render(request, "", {'form':form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            name_user = form.cleaned_data['name_user']
            form.save()
            return render(request, "", {"mensaje": "Usuario Creado"})
        
    else:
        form = UserCreationForm()


    return render(request, "", {"form":form})


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

