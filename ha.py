def insertion_sort(arr):
    for i in range(1,len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]=arr[b-1],arr[b]
            b-=1
    return arr
            
            


arr = [1,2,5,6,87,12]
print(insertion_sort(arr))
