from django.urls import path
from bookowner import views

urlpatterns=[
    path('',views.AdminDashboardView.as_view(),name="dashboard"),
    path("book/change/<int:id>", views.BookEditView.as_view(), name="edit-book"),
    path("book/add", views.BookAddView.as_view(), name="addbook"),
    path("book/all", views.BookListView.as_view(), name="listbook"),
    path("book/remove/<int:id>", views.delete_book, name="remove-book"),
    path("book/details/<int:id>", views.TodoDetailView.as_view(), name="book-detail"),

]