
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    
     # path("Dashboard", views.MainIndexView.as_view(), name="index"),
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

     path("book_create/", views.BookCreateView.as_view(), name="book_create"),
     path("book_list/", views.BookList.as_view(), name="book_list"),
     path("book_detial/<str:pk>/", views.BookDetialView.as_view(), name="book_detial"),
     path("book_update/<str:pk>/", views.BookUpdateView.as_view(), name="book_update"),
     path("book_delete/<str:pk>/", views.BookDeleteView.as_view(), name="book_delete"),

     path("auther_create/", views.AutherCreateView.as_view(), name="auther_create"),
     path("auther_list/", views.AutherListView.as_view(), name="auther_list"),
     path("auther_detial/<str:pk>/", views.AuthorDetialView.as_view(), name="auther_detial"),
     path("auther_update/<str:pk>/", views.AuthorUpdateView.as_view(), name="auther_update"),
     path("auther_delete/<str:pk>/", views.AuthorDeleteView.as_view(), name="auther_delete"),
]
