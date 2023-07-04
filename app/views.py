from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from . models import Book

# Create your views here.

class IndexView(TemplateView):
    template_name='app/index.html'

class chartjsView(TemplateView):
    template_name='app/charts/chartjs.html'

class buttonsView(TemplateView):
    template_name='app/ui-features/buttons.html'
    
class typographyView(TemplateView):
    template_name='app/ui-features/typography.html'

class iconsView(TemplateView):
    template_name='app/icons/mdi.html'

class formsView(TemplateView):
    template_name='app/forms/basic_elements.html'

class tableView(TemplateView):
    template_name='app/tables/basic-table.html'

class blankPageView(TemplateView):
    template_name='app/samples/blank-page.html'

class error404View(TemplateView):
    template_name='app/samples/error-404.html'

class error500View(TemplateView):
    template_name='app/samples/error-500.html'
