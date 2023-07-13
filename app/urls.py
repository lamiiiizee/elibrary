
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
     path("chart/", views.ChartjsView.as_view(), name="chartjs"),
     path("buttons/", views.ButtonsView.as_view(), name="buttons"),
     path("typography/", views.TypographyView.as_view(), name="typography"),
     path("icons/", views.IconsView.as_view(), name="icons"),
     path("forms/", views.FormsView.as_view(), name="forms"),
     path("table/", views.TableView.as_view(), name="tables"),
     path("blankPage/", views.BlankPageView.as_view(), name="Blank_Page"),
     path("404/", views.Error404View.as_view(), name="error404"),
     path("500/", views.Error500View.as_view(), name="error500"),
]
