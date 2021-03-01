array = [1,2,3,4,5] #declare array
shift = 2 #number of rotation want to perform

for i in range (0,shift):
  temp = array[0] #save first element of array in temp variable
  
  for j in range (0, len(array)-1):
    array[j]= array[j+1] #shift element toward left  side
  array[j] = temp #copy temp value to last elements array
  
  for i in range (0,len(array)):
    print(array[i])
