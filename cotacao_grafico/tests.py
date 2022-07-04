from pydoc import resolve

from django.test import TestCase
from django.urls import reverse

from cotacao_grafico import views
from cotacao_grafico.models import Precos


class Cotacao_grafico_Test(TestCase):
    def test_url_home(self):
        '''Testa se a url inicial é realmente / '''
        home_url = reverse('cotacao_grafico:home')
        self.assertEqual(home_url, '/')


    def test_view_home_errada_404(self):
        '''Testando url invalida se foi 404'''
        response = self.client.get( '/urlinvalida')
        self.assertEqual(response.status_code, 404)



    def test_view_home_is_ok(self):
        '''Verifica se status code foi 200'''
        response = self.client.get(reverse('cotacao_grafico:home'))
        self.assertEqual(response.status_code, 200)


    def test_load_do_template(self):
        '''Verifica se o template chamado foi o predefinido no programa inicial'''
        response = self.client.get(reverse('cotacao_grafico:home'))
        self.assertTemplateUsed(response, 'cotacao_grafico/pages/home.html')


    def test_consulta_vazia_retorna_msg(self):
        '''Teste verifica o corpo da resposta se possui strings campo vazio
        Isso confirma que o HTML renderizou e não passamos parâmetros GET
        '''
        response = self.client.get(reverse('cotacao_grafico:home'))
        self.assertIn(
            'Campo moeda vazio<br>Campo inicio vazio<br>Campo data vazio foi substituido',
            response.content.decode('utf-8')
        )


    def test_ORM_Django(self):
        ''''Verifica Operacao ORM'''
        preco=5.3 
        moeda='BRL'
        data='2022-07-02'
        Precos.objects.create(preco=preco, moeda=moeda, data=data)
        existeEmBD = Precos.objects.filter(moeda=moeda).filter(data=data).exists()
        self.assertIs(existeEmBD, True)
