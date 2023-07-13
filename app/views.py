from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from . models import Book,BookAuthor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class MainIndexView(LoginRequiredMixin ,TemplateView):
    template_name='app/mainindex.html'

class IndexView(LoginRequiredMixin ,TemplateView):
    template_name='app/index.html'

class ChartjsView(TemplateView):
    template_name='app/charts/chartjs.html'

class ButtonsView(TemplateView):
    template_name='app/ui-features/buttons.html'
    
class TypographyView(TemplateView):
    template_name='app/ui-features/typography.html'

class IconsView(TemplateView):
    template_name='app/icons/mdi.html'

class FormsView(TemplateView):
    template_name='app/forms/basic_elements.html'

class TableView(TemplateView):
    template_name='app/tables/basic-table.html'

class BlankPageView(TemplateView):
    template_name='app/samples/blank-page.html'

class Error404View(TemplateView):
    template_name='app/samples/error-404.html'

class Error500View(TemplateView):
    template_name='app/samples/error-500.html'


# book views start

class BookCreateView(LoginRequiredMixin ,CreateView):
    model = Book
    template_name='app/viewstemplate/createview.html'
    fields = "__all__"
    # success_url= reverse_lazy('app:book_list',)
    
    
class BookList(LoginRequiredMixin ,ListView):
    model = Book
    template_name='app/viewstemplate/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Book List"
        return context

class BookDetialView(LoginRequiredMixin ,DetailView):
    model = Book
    template_name='app/viewstemplate/detialview.html'

class BookUpdateView(LoginRequiredMixin ,UpdateView):
    model = Book
    template_name='app/viewstemplate/updateview.html'
    fields = "__all__"

class BookDeleteView(LoginRequiredMixin ,DeleteView):
    model = Book
    template_name='app/viewstemplate/deleteview.html'
    success_url= reverse_lazy('app:book_list',)

# book views end



# book author views start
class AutherCreateView(LoginRequiredMixin ,CreateView):
    model = BookAuthor
    template_name='app/autherviews/createview.html'
    fields = "__all__"
    # success_url= reverse_lazy('app:book_list',)
    
    
class AutherListView(LoginRequiredMixin ,ListView):
    model = BookAuthor
    template_name='app/autherviews/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Auther"
        return context

class AuthorDetialView(LoginRequiredMixin ,DetailView):
    model = BookAuthor
    template_name='app/autherviews/detialview.html'

class AuthorUpdateView(LoginRequiredMixin ,UpdateView):
    model = BookAuthor
    template_name='app/autherviews/updateview.html'
    fields = "__all__"

class AuthorDeleteView(LoginRequiredMixin ,DeleteView):
    model = BookAuthor
    template_name='app/autherviews/deleteview.html'
    success_url= reverse_lazy('app:auther_list',)
# book author views start