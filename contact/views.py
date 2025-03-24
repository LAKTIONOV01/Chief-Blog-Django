from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .models import ContactModel
from .forms import ContactForm


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})



class CreateContact(CreateView):
    model = ContactModel
    form_class = ContactForm
    success_url = reverse_lazy('contact:about')


class AboutView(View):
    def get(self, request):
        return render(request, 'contact/about.html')
