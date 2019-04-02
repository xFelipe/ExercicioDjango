from django.forms import ModelForm
from .models import Produto


class produtoForm(ModelForm):
    class meta():
        model = Produto
        fields = ['nome', 'preco', 'quantidade']
