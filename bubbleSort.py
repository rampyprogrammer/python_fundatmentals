def BubbleSort(arr):
    n=len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            print('j-->',j)
            print('j+1-->',j+1)
            print(arr)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)    
 
list=[1,43,24,14,13]               
BubbleSort(list)


print("after the sort")
print(list)
