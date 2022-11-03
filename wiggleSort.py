#algoritimo de ordenação legalzinho


// cria um padrão de ordenação seria  valormenor < array[1] > valormenor : valormenor <  array[3] > valormenor .. 
def wiggleSort(array):
 for i in range(len(array)):
  if (i % 2 == 1) == (array[i-1] > array[i]):
   print(i,i % 2 == 1)
   array[i-1], array[i] = array[i], array[i-1]   