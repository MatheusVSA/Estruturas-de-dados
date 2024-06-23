"""
Disciplina: Estrutura de dados II
Aluno: Matheus Vicente Santos Almeida

Atividade de revisão

Exercicio sobre Fila
"""

#A classe nó armazena um dao e uma referência para o próximo nó na sequência
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

#Contrutor da Fila
class FilaSimples:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def enqueue(self, elemento):
        
        # Adiciona um elemento no final da fila
        if self.topo:
            ponteiro = self.topo
            while ponteiro.proximo:
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elemento)
        else:
            self.topo = No(elemento)
        self.tamanho += 1

    def dequeue(self):
        
        # Remove o elemento que está no início da fila e o retorna
        if self.topo:
            elementoRemovido = self.topo.dado
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return elementoRemovido

# Adicionando os dados a fila nome
filaNome = FilaSimples()
filaNome.enqueue('M')
filaNome.enqueue('a')
filaNome.enqueue('t')
filaNome.enqueue('h')
filaNome.enqueue('e')
filaNome.enqueue('u')
filaNome.enqueue('s')
filaNome.enqueue('A')
filaNome.enqueue('l')
filaNome.enqueue('m')
filaNome.enqueue('e')
filaNome.enqueue('i')
filaNome.enqueue('d')
filaNome.enqueue('a')

# Adicionando os dados a fila matricula
filaMatricula = FilaSimples()
filaMatricula.enqueue(2)
filaMatricula.enqueue(2)
filaMatricula.enqueue(9)
filaMatricula.enqueue(9)
filaMatricula.enqueue(8)
filaMatricula.enqueue(7)
filaMatricula.enqueue(0)
filaMatricula.enqueue(7)

#Exibição dos elementos da fila 
print("Fila de nome:")
while filaNome.tamanho > 0:
    print(f"[{filaNome.dequeue()}]", end="")
print("")

print("Fila de matrícula:")
while filaMatricula.tamanho > 0:
    print(f"[{filaMatricula.dequeue()}]", end="")
print("")
