from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView
from bookapp.models import Books
from bookowner.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from bookowner import forms


# Create your views here.

class AdminDashboardView(TemplateView):
    template_name = "dashboard.html"

class BookAddView(CreateView):
    model = Books
    form_class = forms.BookForm
    template_name = "add-book.html"
    success_url = reverse_lazy("listbook")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Book has been added")
        return super().form_valid(form)


class BookListView(ListView):
    model = Books
    template_name = "list-book.html"
    context_object_name = "books"
    def get_queryset(self):
        return Books.objects.all()


def delete_book(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    messages.success(request,"Book Deleted")
    return redirect("listbook")


class BookEditView(UpdateView):
    model = Books
    form_class = forms.BookEditForm
    template_name = "book-edit.html"
    success_url = reverse_lazy("listbook")
    pk_url_kwarg = "id"
    def form_valid(self, form):
        messages.success(self.request,"Book has been Updated")
        return super().form_valid(form)


class TodoDetailView(DetailView):
    model = Books
    template_name = "book-detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"