from django import forms
from tempus_dominus.widgets import DatePicker
from saude.tipo_sangue import tipo_sanguineo

class SaudeForms (forms.Form):
    nome = forms.CharField(label = 'NOME:', max_length = 100)
    cpf = forms.CharField(label = 'CPF:', max_length = 11)
    data_nascimento = forms.DateField(label = 'DATA DE NASCIMENTO:', widget=DatePicker())
    tipo_sanguineo = forms.ChoiceField(label = 'TIPO SANGUINEO:', choices = tipo_sanguineo)
    adicionais = forms.CharField(
        label='INFORMAÇÕES ADICIONAIS:',
        max_length = 200,
        widget=forms.Textarea(),
        required= False)

    email = forms.EmailField(
        label='E-MAIL:',max_length=200)