from django.shortcuts import render

def index_view(request):
    return render (request, 'website/index.html')
def about_view(request):
    context = {'fname': 'Behzad', 'lname':'Abbasi', 'birthdate': '21 September 1985', 'age':'38',
               'website': 'www.Behzad-Abbasi.com', 'degree': 'PhD Candidate' , 'phone': '+98 914 346 5560', 
               'Email': 'behzad.Abbasy@gmail.com' , 'city':'Urmia, Iran' }
    return render (request, 'website/about.html', context)    
def contact_view(request):
    context = {'phone': '+98 914 346 5560','Email': 'behzad.Abbasy@gmail.com' , 'city':'Urmia, Iran' }
    return render (request, 'website/contact.html', context)    
def projects_view(request):
    return render (request, 'website/projects.html')
