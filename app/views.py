from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from . models import Book

# Create your views here.

class IndexView(TemplateView):
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
