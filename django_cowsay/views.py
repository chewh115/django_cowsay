from django.shortcuts import render
from django_cowsay.models import CowSayText
from django_cowsay.forms import CowSayForm

def index(request):
    cowsays = []
    if request.method == 'POST':
        form = CowSayForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
    return render(request, 'index.html')