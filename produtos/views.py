from django.shortcuts import render
from .forms import produtoForm
from .models import Produto
# Create your views here.


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


'''
def novo_produto(request):
    form = produtoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'produto_form.html', {'form': form})
'''