#Pior caso : O(N^2)
arrayOriginal= [787,8,5,4,10,23,8]
def bubbleSort(array):
  x = -1
  
  def swap(i, j):
    array[i], array[j] = array[j], array[i]#troca posições no array
  
  n = len(array) #tamanho do array
  trocaFoiFeita= True 
  while trocaFoiFeita:
   trocaFoiFeita = False
   x = x + 1
   for i in range(1, n-x):
    if array[i - 1] > array[i]:
     swap(i - 1, i)
     trocaFoiFeita = True
  return 0



bubbleSort(arrayOriginal)
print(arrayOriginal)
