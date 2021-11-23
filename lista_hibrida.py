# Classe que vamos usar para tratar as exceções.
from node import Node


class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


# Inicio da classe Lista, para instanciar as listas como objetos.

class Lista:
    def __init__(self):
        self._vetor = []
        self._head = None

    @property
    def vetor(self):
        return self._vetor

    @property
    def head(self):
        return self._head

    @vetor.setter
    def vetor(self, novo):
        self._vetor = novo

    @head.setter
    def head(self, novo):
        self._head = novo

    # Método para checar se a lista está vazia.

    def estaVazia(self):
    
        if not self._vetor:
            return True
        else:
            return False

    # Método para checar o tamanho atual da lista em questão.

    def tamanho(self):
        print("Total de elementos na lista: ", end='')
        return (len(self._vetor))

    # Método para consultar o conteúdo de um elemento na lista.

    def elemento(self, posicao):
        try:
            if (self.estaVazia()):
                raise ListaException("A lista está vazia!")

            cursor = self._head
            contador = 1
            while(cursor != None):
                if(contador == posicao):
                    return (f'O valor referente ao elemento inserido é: {cursor._carga}')
                cursor = cursor._prox
                contador += 1
        except AttributeError:
            raise ListaException(
                'Valor inserido não consta como um elemento presente na lista. Por favor, tente novamente inserindo um número em que haja elemento referente na lista.')

    # Método para buscar um valor na lista.

    def busca(self, valor):
        try:
            if (self.estaVazia()):
                raise ListaException("A lista está vazia!")

            cursor = self._head
            contador = 1

            while(cursor != None):
                if(cursor._carga == valor):
                    return contador

                cursor = cursor._prox
                contador += 1

        except AttributeError:
            raise ListaException(
                'Valor inserido não consta como um valor presente na lista. Por favor, tente novamente inserindo um número em que haja elemento referente na lista.')


    # Método para inserir um valor no início da lista.

    def inserir_inicio(self, valor):
        no = Node(valor)
        if not self._head:
            self._head = no
        else:
            no._prox = self._head
            self._head = no
        self._vetor.append(no)


    # Método para inserir um valor no final da lista.

    def inserir_final(self, valor):
        no = Node(valor)
        if not self._head:
            self._head = no
        else:
            cursor = self._head
            while cursor != -1:
                if cursor._prox == -1:
                    cursor._prox = no
                    break
                cursor = cursor._prox
        self._vetor.append(no)


    # Método para trocar a ordem dos elementos da lista.

    def trocar_ordem(self, posicao_elem_1, posicao_elem_2):
        try:
          if posicao_elem_1 <= 0 or posicao_elem_2 <= 0:
            raise ListaException ("\nPosição inválida. Por favor, insira uma posição presente na lista, maior que zero.")
          else:
            elem_pos_1 = self._vetor[posicao_elem_1-1]
            elem_pos_2 = self._vetor[posicao_elem_2-1]
            aux = elem_pos_1._carga
            elem_pos_1._carga = elem_pos_2._carga
            elem_pos_2._carga = aux

        except IndexError:
            raise ListaException ("\nPosição não encontrada. Por favor, insira um valor que esteja presente na lista.")


    # Método para imprimir os elementos contidos na lista atual.
    def imprimir_lista(self):
      self.__str__()   

    # Método para remover um elemento do início da lista.
    def remover_inicio(self):
        if (self.estaVazia()):
            raise ListaException('Não é possível remover de uma lista vazia')
        else:
            aux = self._head
            self._head = self._head._prox
            self._vetor.remove(aux)

    # Método para remover um elemento do fim da lista.
    def remover_final(self):
    
        if (self.estaVazia()):
          raise ListaException ('Não é possível remover de uma lista vazia.')
        elif len(self._vetor) == 1:
          self.remove_todos()
        else:
            cursor = self._head
            while cursor != -1:
                #Captura o penultimo elemento
                if cursor._prox._prox == -1:
                    ultimo = cursor._prox
                    self._vetor.remove(ultimo)
                    cursor._prox = -1
                    break
                cursor = cursor._prox


    # Método para limpar a lista, removendo todos seus elementos.

    def remove_todos(self):
        self._vetor = []
        self._head = None

    def __str__(self):
      cursor = self._head
      if not self._head:
          print('[]')
      else:
          while cursor != -1:
              if cursor._prox == -1:
                  print(f'[{cursor._carga} | -1 ]  \n')
              else:
                  print(
                      f'[{cursor._carga} | {self._vetor.index(cursor._prox)}]  ', end='')
              cursor = cursor._prox