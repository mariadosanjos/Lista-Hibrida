# Classe Node que é responsável pelo encadeamento das listas
class Node:
    def __init__(self, dado):
        self._carga = dado
        self._prox = -1

@property
def carga(self):
    return self._carga


@property
def prox(self):
    return self._prox


@carga.setter
def carga(self, novoDado):
    self._dado = novoDado


@prox.setter
def prox(self, novoProx):
    self._prox = novoProx