from distutils.log import error
from pyexpat.errors import messages
import re
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm, ContactForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.conf import settings
from django.core.mail import send_mail

def mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'dnnd1264@gmail.com',
['kiberl354@gmail.com'], fail_silently=False)
            if mail:
                return redirect('success')
            else:
                messages.error(request, 'Ваше письмо не отправлено')
    else:
        form = ContactForm()
    return render(request, 'news/mail.html', {'form': form})

def success(request):
    return render(request, 'news/success.html')

def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news' : news}) 

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

class NewDeleteView(DeleteView):
    model = Artiles
    template_name = 'news/news-delete.html'
    success_url = '/news/'

def create(request):
    global error
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была не верной"

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'news/create.html', data)

def armaturi(request):
    return render(request, 'news/armaturi.html')

def balki(request):
    return render(request, 'news/balki.html')

def round(request):
    return render(request, 'news/round.html')

def listi(request):
    return render(request, 'news/listi.html')

def profanstil(request):
    return render(request, 'news/profanstil.html')

def setka(request):
    return render(request, 'news/setka.html')

def trubi(request):
    return render(request, 'news/trubi.html')

def ugolok(request):
    return render(request, 'news/ugolok.html')

def colormet(request):
    return render(request, 'news/colormet.html')

def trubaarm(request):
    return render(request, 'news/trubaarm.html')

def sandvich(request):
    return render(request, 'news/sandvich.html')

def zhinkmet(request):
    return render(request, 'news/zhinkmet.html')

def nerzstal(request):
    return render(request, 'news/nerzstal.html')