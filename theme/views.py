from django.shortcuts import render, redirect

def home_page(request):
    context = {}
    return render(request, 'base.html', context) 