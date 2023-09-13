#insertion sort
def InsertionSort(array):
    for a in range(1,len(array)):
        b=a
        while b>0 and array[b-1]>array[b]:
            array[b-1],array[b]=array[b],array[b-1]
            b-=1
            
l1=[12,4,56,6,7,45]
InsertionSort(l1)

print('after the sort')
print(l1)