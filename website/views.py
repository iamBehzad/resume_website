from django.shortcuts import render

def index_view(request):
    return render (request, 'website/index.html')
def about_view(request):
    return render (request, 'website/about.html')
def contact_view(request):
    return render (request, 'website/contact.html')
def portfolio_view(request):
    return render (request, 'website/portfolio.html')
def resume_view(request):
    return render (request, 'website/resume.html')