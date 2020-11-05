from django import forms
from .. models import Endereco


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ['rua', 'bairro', 'estado', 'numero', 'complemento', 'pais', 'cep', 'cidade', 'pais']

