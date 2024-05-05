
#define a lista inicial 
lista=[1,2,3,4,5,6,7,8,9,10]



#defini a funcao 
def inserir_final (lista, valor):
    lista.append(valor)
    print(lista)



def inserir_meio(lista, valor, posicao):
    for i in range( len(lista) ):
        if i == posicao:
            lista.insert(posicao, valor) 
    print(lista)


def apaga_valor(lista, valor):
    for i in range( len(lista) ):
        if lista[i-1] == valor: # o [i-1] ajusta os valores do for ao da lista
            E = lista[i-1]
            lista.remove(E)     
    print(lista)


def procura_valor (lista, valor):
    for i in range( len(lista) ):
        if lista[i-1] == valor: # o [i-1] ajusta os valores do for ao da lista
            print("indice:",i-1)


def procura_indice (lista, posicao):
    for i in range( len(lista)+1 ):
        if i-1 == posicao: # o [i-1] ajusta os valores do for ao da lista
            print(lista[i-1])#0 como posicao inicial


#interface do terminal
print("---------------------")
print("Manipulador de listas")
print("---------------------")
print("---------------------")
print("lista =",lista)
print("---------------------")
print("---------------------")
print("1- para iniciar")
print("---------------------")
valor = input("inicie: ")
while int(valor) != 6:
    print("---------------------")

    print("escolha a operacao:")
    print("1- inserir no fim")
    print("2-inserir no meio")
    print("3-apagar")
    print("4-procura valor")
    print("5-procura indice")
    print("6-cancelar")


    print("-------------------")
    print("-------------------")
    valor = input("operacao: ")
    if int(valor) == 1:
        valor1 = input("Digite um valor para adicionar à lista: ")
        listaNova = inserir_final (lista, int(valor1) )

    if int(valor) == 2:
        valor2 = input("Digite um valor para adicionar à lista: ")
        posicao2 = input("Digite a posicao do valor: ")
        listaNova = inserir_meio(lista, int(valor2), int(posicao2))

    if int(valor) == 3:
        valor3 = input("Digite um valor para remover da lista: ")
        listaNova = apaga_valor(lista, int(valor3))

    if int(valor) == 4:
        valor4 = input("Digite um valor para procurar lista: ")
        listaNova = procura_valor(lista, int(valor4))

    if int(valor) == 5:
        posicao5 = input("Digite o inidce: ")
        listaNova = procura_indice(lista,int(posicao5))

print("lista",lista)      

   



