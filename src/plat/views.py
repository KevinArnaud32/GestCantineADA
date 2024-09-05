from django.shortcuts import render, redirect
from .models import Plat
from .form import PlatForm

# Create your views here.
def list(request):

    plats = Plat.objects.all()
    plats_count = Plat.objects.count()

    context = {
        'plats': plats,
        'plat_count': plats_count
    }

    return render(request, 'plat/list.html', context)


def add(request):

    if request.method == "POST":
        form_plat = PlatForm(request.POST)
        if form_plat.is_valid():
            print(form_plat.cleaned_data)
            form_plat.save()
            return redirect('plat:list')
    
    
    form_plat = PlatForm()

    context = {
        'title': 'Ajouter un plat',
        'form_plat': form_plat
    }


    return render(request, 'plat/form.html', context)


def update(request, id):

    plat = Plat.objects.get(id = id)

    context = {
        'title': 'Modification plat'
    }

    if request.method == "POST":
        form_plat = PlatForm(request.POST, instance = plat)
        if form_plat.is_valid():
            print(form_plat.cleaned_data)
            form_plat.save()
            return redirect('plat:list')
        
    form_plat = PlatForm(instance = plat)

    context['form_plat'] = form_plat

    return render(request, 'plat/form.html', context)


def delete(request, id):

    plat = Plat.objects.get(id = id)
    plat.delete()
    
    return redirect('plat:list')