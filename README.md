# Lista-Hibrida

![gif](https://user-images.githubusercontent.com/37851455/132266867-bca823cf-9f95-4d53-8102-ffd882a2c96a.gif)

Projeto de lista encadeada com lista sequencial em Python.
 
Fundamentação

Neste projeto, implementaremos uma Lista Híbrida, que incorpora o conceito de implementação de lista sequencial e encadeada. 




Os elementos da lista são armazenados em um array, logo, poderão ser percorridos de forma indexada. O conteúdo armazenado em cada índice do array é um objeto do tipo Node, constituído por suas propriedades carga e prox, este último um número inteiro que indica o índice em que se encontra o próximo elemento da lista. Entretanto cada novo elemento instanciado tem a propriedade prox igual a -1, em que -1 é uma convenção para o finalizador da lista (o nó com esse valor é o último).

class Node:
   def __init__(self, dado):
       self.carga = dado
       self.prox = -1

A classe Lista  possui, inicialmente, dois atributos: vetor, um list para armazenado dos objetos Node adicionados à lista, e head, uma propriedade controladora que determina qual índice indica o primeiro elemento da lista. Os métodos pertencentes à classe, devem ser implementados para atender aos requisitos de funcionamento da lista.

class Lista:
   def __init__(self):
      self.vetor = []
      self.head = -1
   
   def estaVazia(self):
   def tamanho(self):
   def elemento(self, posicao):
   def busca(self, valor):
   def inserir_inicio(self, valor ):
   def inserir_final(self, valor ):
   def remover_inicio(self, posicao):
   def remover_final(self, posicao):
   def trocar_ordem(self, posicao_elem_1, posicao_elem_2):
   def __str__(self):

Uma vez adicionados os nós à lista, é importante salientar que o percurso não acontece seguindo a ordem natural dos links. Caso fosse seguido esse raciocínio, teríamos a seguinte impressão na tela:

   (0)         (1)        (2)        (3)
[10 | -1]   [20 | 0]   [30 | 1]   [40 | 2] 
                                    head

Porém, a ordem apresentada não representa a ordem correta dos elementos, pois deve ser iniciado pelo índice indicado pelo head. Desta forma, teríamos o percurso da seguinte maneira:

[40 | 2]   [30 | 1]   [20 | 0]   [10 | -1]
head

Isto significa que o primeiro elemento está no índice determinado pelo head, igual a 3 (nó 40). O campo prox do nó armazenado neste índice indica que o deslocamento segue para o índice 2 (nó 30). Chegando ao índice 2, o campo prox do nó armazenado indica que o deslocamento segue para o índice 1 (nó 20). No índice 1, o campo prox do nó armazenado aponta para o índice 0 (nó 10). Por fim, ao chegar ao nó 10, o campo prox tem valor igual a -1, indicando que este é o último elemento da lista.

Todos os métodos básicos constantes na classe lista devem ser implementados respeitando o raciocínio determinado pela Lista Híbrida. Nada impede que você possa implementar métodos adicionais ou até mesmo métodos especiais de Python para facilitar tarefas de comparação entre objetos ou outra finalidade.
