from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()[:3]
    return render(request, 'portfolio_app/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_app/about.html', {})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Contact from {name} ({email}): {message}")

            send_mail(
                f'Portfolio Contact: {name}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['Hshinde710@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form})