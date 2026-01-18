from django import forms

class CheckoutForm(forms.Form):
    cep = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "cep",
            "placeholder": "00000-000"
        })
    )

    rua = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "rua"
        })
    )

    bairro = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "bairro"
        })
    )

    cidade = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "cidade"
        })
    )

    estado = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "estado",
            "maxlength": "2"
        })
    )
