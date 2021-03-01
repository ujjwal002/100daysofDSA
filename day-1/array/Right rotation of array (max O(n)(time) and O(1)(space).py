num = [1,2,3,4,5,6,7] #declare array as list
shift = 2 #number of rotation

def rightarrayrotation(num_array, shhift):
  for i in range (0, shift):
     temp = num_array[len(num_array)-1]
      for k in range(len(num_array)-1,0,-1):
        num_array[0]=temp
        
        return num_array
      
  def printarray(array):
    for i in range (0, len(array)):
      print(array[i], ends=' ')
      
      rotated_array = right_rotated(num, shift)
      printarray(rotated_array)
    
