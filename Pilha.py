"""
Disciplina: Estrutura de dados II
Aluno: Matheus Vicente Santos Almeida

Atividade de revisão

Exercicio sobre Pilha
"""

#A classe nó armazena um dado e uma referência para o próximo nó na sequência
class No:
    def __init__(self, dado, lista):
        self.dado = dado
        self.proximo = None
        self.lista = lista  # Identifica a qual pilha pertence o nó

#Construtor da pilha
class Pilha:
    def __init__(self):
        #Aqui os atributos da pilha são inicializados com valores vazios e 0 
        self.topoNome = None
        self.topoMatricula = None
        self.tamanhoNome = 0
        self.tamanhoMatricula = 0
        
    #Método de inserir um elemento no topo da pilha     
    def push(self, elemento, lista):
        novo_no = No(elemento, lista)
        if lista == "nome":
            novo_no.proximo = self.topoNome
            self.topoNome = novo_no
            self.tamanhoNome += 1
        elif lista == "matricula":
            novo_no.proximo = self.topoMatricula
            self.topoMatricula = novo_no
            self.tamanhoMatricula += 1

    #Método para remover um elemento do topo da pilha 
    def pop(self, lista):
        
        #Remove o elemento no topo da lista nome 
        if lista == "nome" and self.topoNome:
            elemento = self.topoNome.dado
            self.topoNome = self.topoNome.proximo
            self.tamanhoNome -= 1
            return elemento
            
        #Remove o elemento no topo da lista matricula 
        elif lista == "matricula" and self.topoMatricula:
            elemento = self.topoMatricula.dado
            self.topoMatricula = self.topoMatricula.proximo
            self.tamanhoMatricula -= 1
            return elemento

    def imprimir(self, lista):
        
        #Método de exibição da pilha nome 
        if lista == "nome" and self.topoNome:
            ponteiro = self.topoNome
            while ponteiro:
                print(f"[{ponteiro.dado}]", end="")
                ponteiro = ponteiro.proximo
            print("")
        
        #Método de exibição da pilha matricula 
        elif lista == "matricula" and self.topoMatricula:
            ponteiro = self.topoMatricula
            while ponteiro:
                print(f"[{ponteiro.dado}]", end="")
                ponteiro = ponteiro.proximo
            print("")


# # Adicionando os dados as pilhas
pilhas = Pilha()
pilhas.push('M', "nome")
pilhas.push('a', "nome")
pilhas.push('t', "nome")
pilhas.push('h', "nome")
pilhas.push('e', "nome")
pilhas.push('u', "nome")
pilhas.push('s', "nome")
pilhas.push('A', "nome")
pilhas.push('l', "nome")
pilhas.push('m', "nome")
pilhas.push('e', "nome")
pilhas.push('i', "nome")
pilhas.push('d', "nome")
pilhas.push('a', "nome")

pilhas.push('2', "matricula")
pilhas.push('2', "matricula")
pilhas.push('9', "matricula")
pilhas.push('9', "matricula")
pilhas.push('8', "matricula")
pilhas.push('7', "matricula")
pilhas.push('0', "matricula")
pilhas.push('7', "matricula")

print("Pilha de nome:")
pilhas.imprimir("nome")

print("Pilha de matrícula:")
pilhas.imprimir("matricula")

print("Tamanho da pilha de nome:", pilhas.tamanhoNome)
print("Tamanho da pilha de matrícula:", pilhas.tamanhoMatricula)