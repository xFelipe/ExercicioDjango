from django.urls import path
#from .views import register
from .views import lista_produtos

urlpatterns = [
    #path('register', register),
    path('listagem', lista_produtos, name='url_listagem_produto')
]