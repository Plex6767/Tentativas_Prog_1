list = ["3", "18", "27", "4", "3", "0.9", "23"]

def bubble_sort(list):
    list = int(list)


    n = len(list)
    for i in range(n-1):
        trocou = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                trocou = True
        if not trocou:
            break

bubble_sort(list)
print(list)