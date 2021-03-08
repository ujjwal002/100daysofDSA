def binary_Search (arr, l, r, x): 
  
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else:  # Element is not present in the array 
       
        return -1
 
arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9] 
x = 10
  
# Function call 
result = binary_Search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
