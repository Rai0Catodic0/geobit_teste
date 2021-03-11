from rest_framework import  serializers
from loja.models import Autor, Livro


class AutorSerializer(serializers.ModelSerializer):
    class meta:
        model = Autor
        fields = "__all__"

class LivroSerializer(serializers.ModelSerializer):
    class meta:
        model = Livro
        fields ="__all__"

    