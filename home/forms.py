from django import forms

from .models import Booking, ContactMessage


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields = '__all__'

        widgets= {
            'booking_date': DateInput()
        }

        labels={

             'p_name' : "Patient Name" ,
             'p_phone' : "Patient Phone" ,
             'p_email' : "Patient Mail ID" ,
             'doc_name' : "Doctor Name" ,
             'booking_date' : "Booking Date" ,
             
             }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }