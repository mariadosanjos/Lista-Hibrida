from lista_hibrida import Lista
from lista_hibrida import ListaException

class App:

    def __init__(self):
        self._listas = []
    
    def set_listas(self, listas):
        self._listas = listas
    
    def get_listas(self):
        return self._listas
    
    def gera_listas(self, qtd_listas = 5):
        for i in range (qtd_listas):
            self._listas.append(Lista())
    
    def busca_lista(self, posicao):
        try:  
          return self._listas[posicao - 1]
        except IndexError:
          raise ListaException ('Posição informada para consulta é inválida')

    def retorna_id_lista_atual(self, lista_atual):
        for i in range(len(self._listas)):
            if self._listas[i] == lista_atual:
                return i+1
    
    def mudar_lista(self, posicao_lista):
        try:
          if posicao_lista <= 0:
            raise ListaException ('Posição informada para consulta é inválida, por favor, tente novamente inserindo um número inteiro dentre a quantidade de listas.')
          else:
            return self._listas[posicao_lista-1]
        except IndexError:
          raise ListaException ('Posição informada para consulta é inválida, por favor, tente novamente inserindo um número inteiro dentre a quantidade de listas.')