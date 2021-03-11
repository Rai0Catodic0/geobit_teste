from django.urls import path
from  loja import views

urlpatterns = [
    path("",views.get_livros ),
    path("create/", views.add_livro),
    path("update/<int:id_livro>", views.update_livro),
    path("delete/<int:id_livro>",views.delete_livro),
]