from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from products.models import Product
import uuid

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class ProductCreateView(CreateView):
    model = Product
    success_url = '/'
    fields = ['name', 'year', 'end_date']
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.serial = uuid.uuid4()
        instance.account = self.request.user.account
        return super().form_valid(form)
