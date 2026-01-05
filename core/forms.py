from django import forms
from .models import Client, ProdusAlimentar, Producator, ClientProdus, ProdusProducator


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["nume", "prenume", "adresa"]


class ProdusForm(forms.ModelForm):
    class Meta:
        model = ProdusAlimentar
        fields = ["denumire", "data_producere", "data_expirare"]
        widgets = {
            "data_producere": forms.DateInput(attrs={"type": "date"}),
            "data_expirare": forms.DateInput(attrs={"type": "date"}),
        }


class ProducatorForm(forms.ModelForm):
    class Meta:
        model = Producator
        fields = ["denumire", "tara_origine", "adresa"]


class ClientProdusForm(forms.ModelForm):
    class Meta:
        model = ClientProdus
        fields = ["client", "produs"]


class ProdusProducatorForm(forms.ModelForm):
    class Meta:
        model = ProdusProducator
        fields = ["produs", "producator"]
