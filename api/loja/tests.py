from django.test import TestCase
import json
import  requests


livro = {"nome":"fundacao","autor":"asimov","numero_de_paginas":200,"preco":17.45}

requests.post()
# Create your tests here.
class ApiViews(TestCase):
    
    def test_list_view(self):
        response = self.client.get('/api/')
            self.assertEqual(response,'[]')
    def test_livro_post(self):
        livro = {"nome":"fundacao"}
        livro = json.dumps(livro)
        response = self.client.post('/api/create',data=livro)
        print(response.status_code)
