
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
     path("chart/", views.chartjsView.as_view(), name="chartjs"),
     path("buttons/", views.buttonsView.as_view(), name="buttons"),
     path("typography/", views.typographyView.as_view(), name="typography"),
     path("icons/", views.iconsView.as_view(), name="icons"),
     path("forms/", views.formsView.as_view(), name="forms"),
     path("table/", views.tableView.as_view(), name="tables"),
     path("blankPage/", views.blankPageView.as_view(), name="Blank_Page"),
     path("404/", views.error404View.as_view(), name="error404"),
     path("500/", views.error500View.as_view(), name="error500"),
]
