from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import BookingForm, ContactForm
from django.contrib import messages

 
def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def booking(request):
    if request.method=="POST":
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html',dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)
    


def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form}) 