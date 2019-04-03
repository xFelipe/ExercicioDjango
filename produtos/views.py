from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import ProdutoForm
from .models import Produto
# Create your views here.


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


def criar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_produto')
    return render(request, 'novo_produto.html', {'form': form})


def apagar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if request.method == 'POST':
        produto.delete()
        return redirect('url_listagem_produto')
    return render(request, 'confirmar_exclusao_produto.html', {'produto': produto})


def visualizar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_produto')
    return render(request, 'produto.html', {'form': form, 'id': id})