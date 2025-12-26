from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages  # For flash messages
from django.conf import settings
from .models import Project
from .forms import ContactForm  # Add this import

def home(request):
    projects = Project.objects.all()[:3]
    return render(request, 'portfolio_app/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_app/about.html', {})  # Template next

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
            # For demo: Prints to console (change to real email in production)
            print(f"Contact from {name} ({email}): {message}")
            # Optional: Real email (uncomment & configure settings)
            send_mail(
                f'Portfolio Contact: {name}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['Hshinde710@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')  # Flash message
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form})