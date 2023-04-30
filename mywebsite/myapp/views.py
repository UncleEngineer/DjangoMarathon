from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Product, ContactUs

def Homepage(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'myapp/home.html',context)

def About(request):
    return render(request, 'myapp/about.html')

def Services(request):
    return render(request, 'myapp/services.html')

def Products(request):
    return render(request, 'myapp/products.html')

def Contact(request):

    namelist = Staff.objects.all()
    context = {'namelist':namelist}

    if request.method == 'POST':
        data = request.POST.copy()
        print('DATA:',data)
        name = data.get('name')
        title = data.get('title')
        detail = data.get('detail')
        email = data.get('email')

        newcontact = ContactUs()
        newcontact.name = name
        newcontact.title = title
        newcontact.detail = detail
        newcontact.email = email
        newcontact.save()
        context['alert'] = 'success'


    return render(request, 'myapp/contact.html',context)