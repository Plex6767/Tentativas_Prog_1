"""lista_cru = [3, 18, 27, 4, 3, 0.9, 23]
def list_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list_sort(lista_cru)
print(lista_cru)"""



lista = ["a", "b", "j", "h", "e", "o", "p" , "d"]

def bubble(lista):

    tamanho = len(lista) - 1
    trocou = True

    while trocou:
        trocou = False
        for elemento in range(0,tamanho):
            if lista[elemento] > lista[elemento + 1]:
                mantem = lista[elemento + 1]
                lista[elemento + 1] = lista[elemento]
                lista[elemento] = mantem

                trocou = True
bubble(lista)
print(lista)
