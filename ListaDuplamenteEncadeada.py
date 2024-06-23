"""
Disciplina: Estrutura de dados II
Aluno: Matheus Vicente Santos Almeida

Atividade de revisão

Exercicio sobre Fila duplamente encadeada
"""

#A classe nó armazena um dado e uma referência para o próximo nó na sequência. A classe No na lista duplamente encadeada inclui um atributo adicional anterior em cada nó que aponta para o nó anterior na lista.
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

#Construtor da lista duplamente encadeada
class ListaDuplamenteEncadeada:
    def __init__(self):
        
        # Aqui os atributos para as listas de nome e matrícula são inicializados com valores vazios e 0 
        #Diferente da lista simples temos fimNome e fimMatricula que apontam para o ultimo elemento da lista assim fazendo com que ela possa ser percorrida em duas direções
        self.topoNome = None
        self.topoMatricula = None
        self.fimNome = None
        self.fimMatricula = None
        self.tamanhoNome = 0
        self.tamanhoMatricula = 0

    def add(self, elemento, lista):
        
        # Método para adicionar elementos na lista nome
        if lista == "nome":
            novo_no = No(elemento)
            if self.topoNome:
                novo_no.anterior = self.fimNome
                self.fimNome.proximo = novo_no
                self.fimNome = novo_no
            else:
                self.topoNome = novo_no
                self.fimNome = novo_no
            self.tamanhoNome += 1
            
        # Método para adicionar elementos na lista matricula
        elif lista == "matricula":
            novo_no = No(elemento)
            if self.topoMatricula:
                novo_no.anterior = self.fimMatricula
                self.fimMatricula.proximo = novo_no
                self.fimMatricula = novo_no
            else:
                self.topoMatricula = novo_no
                self.fimMatricula = novo_no
            self.tamanhoMatricula += 1

    def adicionar(self, elemento, lista):
        
        # Método para adicionar elementos em uma das listas
        self.add(elemento, lista)

    def imprimir_nome(self):
        
        # Método que exibe a lista nome 
        if self.topoNome:
            ponteiro = self.topoNome
            while ponteiro:
                print(f"[{ponteiro.dado}]", end="")
                ponteiro = ponteiro.proximo
            print("")
        else:
            print("Lista de nome vazia.")

    def imprimir_matricula(self):
        
        # Método que exibe a lista matricula
        if self.topoMatricula:
            ponteiro = self.topoMatricula
            while ponteiro:
                print(f"[{ponteiro.dado}]", end="")
                ponteiro = ponteiro.proximo
            print("")
        else:
            print("Lista de matrícula vazia.")
            
            
# Adicionando os dados as listas
lista = ListaDuplamenteEncadeada()
lista.adicionar('M', "nome")
lista.adicionar('a', "nome")
lista.adicionar('t', "nome")
lista.adicionar('h', "nome")
lista.adicionar('e', "nome")
lista.adicionar('u', "nome")
lista.adicionar('s', "nome")
lista.adicionar('A', "nome")
lista.adicionar('l', "nome")
lista.adicionar('m', "nome")
lista.adicionar('e', "nome")
lista.adicionar('i', "nome")
lista.adicionar('d', "nome")
lista.adicionar('a', "nome")

lista.adicionar(2, "matricula")
lista.adicionar(2, "matricula")
lista.adicionar(9, "matricula")
lista.adicionar(9, "matricula")
lista.adicionar(8, "matricula")
lista.adicionar(7, "matricula")
lista.adicionar(0, "matricula")
lista.adicionar(7, "matricula")

print("Lista de nome:")
lista.imprimir_nome()

print("Lista de matrícula:")
lista.imprimir_matricula()

print("Tamanho da lista de nome:", lista.tamanhoNome)
print("Tamanho da lista de matrícula:", lista.tamanhoMatricula)