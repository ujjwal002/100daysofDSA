def leftRotate(arr, n, k):
  hub = k % n
    s = ""
 
    
    for i in range(n):
        print str(arr[(hub + i) % n]),
    print
    return
 
 

arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
 

leftRotate(arr, n, k)
 
k = 3
 

leftRotate(arr, n, k)
 
k = 4
 

leftRotate(arr, n, k)
