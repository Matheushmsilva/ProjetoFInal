from django import forms
from tempus_dominus.widgets import DatePicker
from saude.tipo_sangue import tipo_sanguineo

class SaudeForms (forms.Form):
    nome = forms.CharField(label = 'NOME:', max_length = 100)
    cpf = forms.CharField(label = 'CPF:', max_length = 11)
    data_nascimento = forms.DateField(label = 'DATA DE NASCIMENTO:', widget=DatePicker())
    email = forms.EmailField(
        label='E-MAIL:',max_length=200)
    endereco = forms.CharField(label = 'ENDEREÇO:', max_length = 100)
    tipo_sanguineo = forms.ChoiceField(label = 'TIPO SANGUINEO:', choices = tipo_sanguineo)
    nome_responsavel = forms.CharField(label = 'NOME DO RESPONSÁVEL:', max_length = 100)
    adicionais = forms.CharField(
        label='INFORMAÇÕES ADICIONAIS:',
        max_length = 200,
        widget=forms.Textarea(),
        required= False)


