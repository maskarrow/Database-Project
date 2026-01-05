from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, ProdusAlimentar, Producator, ClientProdus, ProdusProducator
from .forms import (
    ClientForm, ProdusForm, ProducatorForm,
    ClientProdusForm, ProdusProducatorForm
)
from .permissions import admin_required


@login_required
def home(request):
    return render(request, "home.html")



@login_required
def clienti_list(request):
    items = Client.objects.all().order_by("nume", "prenume")
    return render(request, "clienti/list.html", {"items": items})


@login_required
def clienti_create(request):
    form = ClientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("clienti_list")
    return render(request, "generic_form.html", {"title": "Adaugă client", "form": form})


@login_required
def clienti_update(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("clienti_list")
    return render(request, "generic_form.html", {"title": "Editează client", "form": form})


@admin_required
def clienti_delete(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("clienti_list")
    return render(request, "confirm_delete.html", {"object": obj, "back_url": "clienti_list"})



@login_required
def produse_list(request):
    items = ProdusAlimentar.objects.all().order_by("denumire")
    return render(request, "produse/list.html", {"items": items})


@login_required
def produse_create(request):
    form = ProdusForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produse_list")
    return render(request, "generic_form.html", {"title": "Adaugă produs", "form": form})


@login_required
def produse_update(request, pk):
    obj = get_object_or_404(ProdusAlimentar, pk=pk)
    form = ProdusForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produse_list")
    return render(request, "generic_form.html", {"title": "Editează produs", "form": form})


@admin_required
def produse_delete(request, pk):
    obj = get_object_or_404(ProdusAlimentar, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("produse_list")
    return render(request, "confirm_delete.html", {"object": obj, "back_url": "produse_list"})



@login_required
def producatori_list(request):
    items = Producator.objects.all().order_by("denumire")
    return render(request, "producator/list.html", {"items": items})


@login_required
def producatori_create(request):
    form = ProducatorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("producatori_list")
    return render(request, "generic_form.html", {"title": "Adaugă producător", "form": form})


@login_required
def producatori_update(request, pk):
    obj = get_object_or_404(Producator, pk=pk)
    form = ProducatorForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("producatori_list")
    return render(request, "generic_form.html", {"title": "Editează producător", "form": form})


@admin_required
def producatori_delete(request, pk):
    obj = get_object_or_404(Producator, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("producatori_list")
    return render(request, "confirm_delete.html", {"object": obj, "back_url": "producatori_list"})



@login_required
def client_produs_list(request):
    items = ClientProdus.objects.select_related("client", "produs").all()
    return render(request, "relatii/client_produs_list.html", {"items": items})


@login_required
def client_produs_create(request):
    form = ClientProdusForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("client_produs_list")
    return render(request, "generic_form.html", {"title": "Adaugă relație Client-Produs", "form": form})


@login_required
def client_produs_update(request, pk):
    obj = get_object_or_404(ClientProdus, pk=pk)
    form = ClientProdusForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("client_produs_list")
    return render(request, "generic_form.html", {"title": "Editează relație Client-Produs", "form": form})


@admin_required
def client_produs_delete(request, pk):
    obj = get_object_or_404(ClientProdus, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("client_produs_list")
    return render(request, "confirm_delete.html", {"object": obj, "back_url": "client_produs_list"})



@login_required
def produs_producator_list(request):
    items = ProdusProducator.objects.select_related("produs", "producator").all()
    return render(request, "relatii/produs_producator_list.html", {"items": items})


@login_required
def produs_producator_create(request):
    form = ProdusProducatorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produs_producator_list")
    return render(request, "generic_form.html", {"title": "Adaugă relație Produs-Producător", "form": form})


@login_required
def produs_producator_update(request, pk):
    obj = get_object_or_404(ProdusProducator, pk=pk)
    form = ProdusProducatorForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produs_producator_list")
    return render(request, "generic_form.html", {"title": "Editează relație Produs-Producător", "form": form})


@admin_required
def produs_producator_delete(request, pk):
    obj = get_object_or_404(ProdusProducator, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("produs_producator_list")
    return render(request, "confirm_delete.html", {"object": obj, "back_url": "produs_producator_list"})
