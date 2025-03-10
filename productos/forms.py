from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):
    METODOS_PAGO = [
        ('nequi', 'Nequi'),
        ('bancolombia', 'Bancolombia'),
    ]

    metodo_pago = forms.ChoiceField(
        choices=METODOS_PAGO,
        widget=forms.RadioSelect,
        required=True
    )

    class Meta:
        model = Orden
        fields = ['nombre', 'email', 'telefono', 'metodo_pago']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tucorreo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu número de teléfono'}),
        }
