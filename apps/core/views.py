from django.shortcuts import render


def index(request):
    return render(request, "base.html")

def about_us(request):
    return render(request, 'core_about_us.html')

def contact(request):
    return render(request, 'core_contact.html')
