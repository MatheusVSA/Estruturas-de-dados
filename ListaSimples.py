"""
Disciplina: Estrutura de dados II
Aluno: Matheus Vicente Santos Almeida

Atividade de revisão

Exercicio sobre Lista
"""

#A classe nó armazena um dado e uma referência para o próximo nó na sequência
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

#Construtor da lista
class ListaSimples:
    def __init__(self):
        #Aqui os atributos para as listas de nome e matrícula são inicializados com valores vazios e 0 
        self.topoNome = None
        self.topoMatricula = None
        self.tamanhoNome = 0
        self.tamanhoMatricula = 0

    def add(self, elemento, lista):
        # Método para adicionar elementos na lista nome
        if lista == "nome":
            if self.topoNome:
                ponteiro = self.topoNome
                while ponteiro.proximo:
                    ponteiro = ponteiro.proximo
                ponteiro.proximo = No(elemento)
            else:
                self.topoNome = No(elemento)
            self.tamanhoNome += 1
            
        # Método para adicionar elementos na lista matricula
        elif lista == "matricula":
            if self.topoMatricula:
                ponteiro = self.topoMatricula
                while ponteiro.proximo:
                    ponteiro = ponteiro.proximo
                ponteiro.proximo = No(elemento)
            else:
                self.topoMatricula = No(elemento)
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


# Adicionando os dados as listas
lista = ListaSimples()
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
