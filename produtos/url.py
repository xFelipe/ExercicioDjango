from django.urls import path
#from .views import register
from .views import lista_produtos, criar_produto, apagar_produto, visualizar_produto

urlpatterns = [
    #path('register', register),
    path('', lista_produtos, name='url_listagem_produto'),
    path('criar', criar_produto, name='url_criar_produto'),
    path('apagar/<int:id>', apagar_produto, name='url_apagar_produto'),
    path('visualizar/<int:id>', visualizar_produto, name='url_visualizar_produto'),
]