def reverse_array(arr, start, end):
    while start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start=start+1
        end= end-1
def left_rotate(arr,d,n):
    if d == 0:
        return None
    d = d%n 
    reverse_array(arr,0,d-1)
    reverse_array(arr,d,n-1)
    reverse_array(arr,0,n-1)


    return(arr)


arr = [1,3,5,7,9,6]
d= 2
n= len(arr)

print(left_rotate(arr,d,n)) 
