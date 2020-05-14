from django.shortcuts import render
from django_cowsay.models import CowSayText
from django_cowsay.forms import CowSayForm
from django_cowsay.terminal_talker import terminal_talker

def index(request):
    new_form = CowSayForm()
    if request.method == 'POST':
        form = CowSayForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            cow_spoke = terminal_talker(text)
            CowSayText.objects.create(text=text)
            return render(request, 'index.html', {'cow_spoke': cow_spoke, 'form': new_form})
    return render(request, 'index.html', {'form': new_form})


def history(request):
    all_spoken = CowSayText.objects.all().order_by('-pk')
    ten_recent = all_spoken[:10]
    most_recent = []
    for speak in ten_recent:
        most_recent.append(terminal_talker(speak.text))
    return render(request, 'history.html', {'most_recent': most_recent})