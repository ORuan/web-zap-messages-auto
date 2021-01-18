from django.shortcuts import render
from accounts.forms import UserForm
from seln.utils import AutomationWhatsApp


def register_users(request):
    send = AutomationWhatsApp('teste-teste', '5577998714634')
    send.send()
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('painel')
        else:
            form_data = UserForm(request.POST)
            return render(request, 'forms/form.html', {'form':form_data})
        return render(request, 'forms/form.html', {'form':form_data})
    else:
        form_data = UserForm()
        context = {
            "form":form_data,
            "title":"Cadastro"
        }
        return render(request, 'forms/form.html', context)

def edit_users(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form_data = UserForm(request.POST or None, instance=user)
        if form_data.is_valid():
            form_data.save()
            return redirect('usuarios:editar')
        else:
            form_data = UserForm(request.POST or None, instance=user)
            context = {
                "form":form_data,
                "title":"Edição"
            }
            return render(request, 'forms/form.html', context)
        context = {
            "form":form_data,
            "title":"Edição"
        }
        return render(request, 'forms/form.html', context)
    else:
        form_data = UserForm(request.POST or None, instance=user)
        context = {
            "form":form_data,
            "title":"Edição"
        }
        return render(request, 'forms/form.html', context)


def view_your_user(request):
    if request.method == "GET":
        user = User.objects.get(id=request.user.id)
        context = {
            "user": user
        }
        return render(request, 'display/profile.html', context)