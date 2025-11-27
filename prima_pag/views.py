from django.shortcuts import render

# Create your views here.
# prima_pag/views.py
from django.shortcuts import render

def salut(request):
    return render(request, 'hello.html')