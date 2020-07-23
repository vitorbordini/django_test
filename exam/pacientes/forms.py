from django import forms

class PacienteForm(forms.Form):
    nome = forms.CharField(label='Your name', max_length=100)
    opcoes = forms.CharField(
        max_length=100,
    )
    
    resultado = forms.BooleanField()
    data = forms.DateTimeField()