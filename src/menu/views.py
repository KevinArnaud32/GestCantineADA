from django.shortcuts import render, redirect
from .models import Menu
from .form import MenuForm

# Create your views here.
def list(request):

    menus = Menu.objects.all()
    menus_count = Menu.objects.count()
    

    context = {
        'menus': menus,
        'menus_count': menus_count
    }

    return render(request, 'menu/list.html', context)


def add(request):

    if request.method == "POST":
        form_menu = MenuForm(request.POST)
        if form_menu.is_valid():
            print(form_menu.cleaned_data)
            form_menu.save()
            return redirect('menu:list')
    
    
    form_menu = MenuForm()

    context = {
        'title': 'Ajouter un menu',
        'form_menu': form_menu
    }


    return render(request, 'menu/form.html', context)


def update(request, id):

    menu = Menu.objects.get(id = id)

    context = {
        'title': 'Modification menu'
    }

    if request.method == "POST":
        form_menu = MenuForm(request.POST, instance = menu)
        if form_menu.is_valid():
            print(form_menu.cleaned_data)
            form_menu.save()
            return redirect('menu:list')
        
    form_menu = MenuForm(instance = menu)

    context['form_menu'] = form_menu

    return render(request, 'menu/form.html', context)


def delete(request, id):

    menu = Menu.objects.get(id = id)
    menu.delete()
    
    return redirect('menu:list')
