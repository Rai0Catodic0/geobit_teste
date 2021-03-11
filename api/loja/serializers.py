from rest_framework import  serializers
from loja.models import Autor, Livro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields ="__all__"

    