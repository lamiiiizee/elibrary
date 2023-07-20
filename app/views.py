from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from . models import Book,BookAuthor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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
    template_name='app/book_view/createview.html'
    fields = "__all__"
    # success_url= reverse_lazy('app:book_list',)

class BookTableView(LoginRequiredMixin ,ListView):
    model = Book
    template_name='app/book_view/book_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Book table"
        return context
    
class BookList(LoginRequiredMixin ,ListView):
    model = Book
    template_name='app/book_view/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Book List"
        return context

class BookDetialView(LoginRequiredMixin ,DetailView):
    model = Book
    template_name='app/book_view/detialview.html'

class BookUpdateView(LoginRequiredMixin ,UpdateView):
    model = Book
    template_name='app/book_view/updateview.html'
    fields = "__all__"
    success_url= reverse_lazy('app:book_list',)


class BookDeleteView(LoginRequiredMixin ,DeleteView):
    model = Book
    template_name='app/book_view/deleteview.html'
    success_url= reverse_lazy('app:book_list',)

# book views end



# book author views start
class AutherCreateView(LoginRequiredMixin ,CreateView):
    model = BookAuthor
    template_name='app/auther_views/createview.html'
    fields = "__all__"
    # success_url= reverse_lazy('app:book_list',)
    
    
class AutherListView(LoginRequiredMixin ,ListView):
    model = BookAuthor
    template_name='app/auther_views/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Auther"
        return context

class AuthorDetialView(LoginRequiredMixin ,DetailView):
    model = BookAuthor
    template_name='app/auther_views/detialview.html'

class AuthorUpdateView(LoginRequiredMixin ,UpdateView):
    model = BookAuthor
    template_name='app/auther_views/updateview.html'
    fields = "__all__"
    success_url= reverse_lazy('app:auther_list',)


class AuthorDeleteView(LoginRequiredMixin ,DeleteView):
    model = BookAuthor
    template_name='app/auther_views/deleteview.html'
    success_url= reverse_lazy('app:auther_list',)
# book author views end



# book user views start
class UserCreateView(LoginRequiredMixin ,CreateView):
    model = User
    template_name='app/user_view/createview.html'
    fields = ('username','email','password')
    success_url= reverse_lazy('app:user_list',)

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)
    
    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.set_password(form.cleaned_data['password'])
    #     user.save()
    #     return super().form_valid(form)

    
class UserListView(LoginRequiredMixin ,ListView):
    model = User
    template_name='app/user_view/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "user"
        return context

class UserUpdateView(LoginRequiredMixin ,UpdateView):
    model = User
    template_name='app/user_view/updateview.html'
    fields = ('username','email','password')
    success_url= reverse_lazy('app:user_list',)

class UserDeleteView(LoginRequiredMixin ,DeleteView):
    model = User
    template_name='app/user_view/deleteview.html'
    success_url= reverse_lazy('app:user_list',)
# book user views end
