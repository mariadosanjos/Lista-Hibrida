from lista_hibrida import ListaException
from aplicacao import App

if __name__ == "__main__":
    # Instâncias da classe Lista

    app = App()
    app.gera_listas()

    # definição da lista padrão (1)
    try:
        lista_atual = app.busca_lista(1)
    except ListaException as e:
        print(e)

    # input do menu

    while True:
        try:
            print('      ------------------------------------------')
            print(f'      Lista {app.retorna_id_lista_atual(lista_atual)}')
            print('      ------------------------------------------')
            print('''
      (i) Inserir no início
      (f) Inserir no final
      (b) Procurar um valor na lista
      (e) Consultar o conteúdo de um elemento
      (t) Trocar ordem dos elementos
      (v) Consultar se a lista está vazia
      (s) Obter o tamanho da lista
      (r) Remover do início
      (o) Remover do final
      (l) Remover todos os elementos da lista
      (p) Imprimir lista
      (m) Mudar a lista
      (x) Sair do programa
            ''')

            opcao = input('Insira a opção desejada: ').lower()
            # Cadeia de ifs de acordo com as opções do menu

            # Opção de inserir valor no início da lista, com a chamada do respectivo método: inserir.inicio.

            if opcao == 'i':
                try:
                    valor = int(input('Informe o valor a ser inserido: '))
                    lista_atual.inserir_inicio(valor)
                    print ("Valor inserido no início da lista.")
                except ValueError:
                   print ('\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')
                    
            # Opção de inserir valor no final da lista, com a chamada do respectivo método: inserir.final

            elif opcao == 'f':
                try:
                    valor = int(input('Informe o valor a ser inserido: '))
                    lista_atual.inserir_final(valor)
                    print ("Valor inserido no fim da lista.")
                except ValueError:
                    print ('\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            # Opção de buscar um valor na lista, com a chamada do respectivo método: busca.

            elif opcao == 'b':
                try:
                    valor = int(input('Informe o valor a ser pesquisado: '))
                    print (lista_atual.busca(valor))
                except ListaException as e:
                  print (e)
                except ValueError:
                    print ('\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

             # Opção de consultar o conteúdo de um elemento e a chamada do respectivo método: elemento.

            elif opcao == 'e':
                try:
                    valor = int(input('Informe a posição do elemento desejado: '))
                    print(lista_atual.elemento(valor))

                except ListaException as e:
                  print (e)
                except ValueError:
                    print ('\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')
      

            # Opção para checar se a lista está vazia, com a chamada do respectivo método: estaVazia

            elif opcao == 'v':
                print(lista_atual.estaVazia())

             # Opção para obter o tamanho da lista, com a chamada do respectivo método: tamanho.

            elif opcao == 's':
                print (lista_atual.tamanho())

            # Opção para remover um elemento do início da lista, com a chamada do respectivo método: remover_inicio.

            elif opcao == 'r':
              try:
                lista_atual.remover_inicio()
                print('Elemento removido!')
              except ListaException as e:
                print(e)
            # Opção para remover um elemento do final da lista, com a chamada do respectivo método: remover_final.

            elif opcao == 'o':
              try:  
                lista_atual.remover_final()
                print("Elemento removido!")
              except ListaException as e:
                print(e)

             # Opção para remover todos os elementos da lista, com a chamada do seu respectivo método: remove_todos.

            elif opcao == 't':
              try:
                e1 = int(input('Informe a posição do primeiro elemento: '))
                e2 = int(input('Informe a posição do segundo elemento: '))
                lista_atual.trocar_ordem(e1, e2)
                print ('\nTroca realizada com sucesso!')
              except ValueError:
                print ('\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')
              except ListaException as e:
                print (e)


            elif opcao == 'l':
                lista_atual.remove_todos()
                print('Todos os elementos foram removidos!')

            # Opção para imprimir a lists, com a chamada do respectivo método: imprimir_lista.

            elif opcao == 'p':
                lista_atual.imprimir_lista()

             # Opção para mudar de lista, com a chamada dos seu respectivo método: mudar_lista.

            elif opcao == 'm':
                try:
                    posicao_lista = int(
                        input(f'Há {len(app._listas)} listas disponíveis. Para qual deseja mudar? '))
                    lista_atual = app.mudar_lista(posicao_lista)
                except ValueError:
                    print ("!- Erro na Operação -!\n\nValor inserido não é válido. Por favor, tente novamente inserindo um número inteiro dentre a quantidade de listas disponíveis.")
                except ListaException as e:
                    print (e)
                   
             # Opção para encerrar o programa.

            elif opcao == 'x':
                break

            # Estrutura de decisão para caso o usuário digite algum valor não referente a nenhuma opção no menu, fazendo com que o laço reinicie.

            else:
                print(
                    '\nOpção inválida. Por favor, insira uma letra referente à uma das opções que estejam no menu. ')

             # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

        except KeyboardInterrupt:
            print('\n !- Erro na Operação -!')
            print('\nComando de teclas pare encerrar a aplicação pressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')