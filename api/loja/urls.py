from django.urls import path
from  loja import views

urlpatterns = [
    path("",views.get_livros, name="get_livros"),
    path("create/", views.add_livro, name="add_livro")
]