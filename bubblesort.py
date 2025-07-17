def bubblesort(lista):
  
  n = len(lista)
  for j in range(n-1):
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            aux = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = aux
  return lista
array = [5, 7, 9, 1, 1, 5, 8, 9, 4, 5, 7]
ordenada = bubblesort(array)
print(ordenada)
