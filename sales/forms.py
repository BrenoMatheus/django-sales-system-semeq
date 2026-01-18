from django import forms

class CheckoutForm(forms.Form):
    cep = forms.CharField(
        max_length=9,
        required=True,
        label="CEP"
    )
    rua = forms.CharField(
        max_length=255,
        required=True,
        label="Rua"
    )
    bairro = forms.CharField(
        max_length=100,
        required=True,
        label="Bairro"
    )
    cidade = forms.CharField(
        max_length=100,
        required=True,
        label="Cidade"
    )
    estado = forms.CharField(
        max_length=2,
        required=True,
        label="Estado"
    )
