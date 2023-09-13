def MergeSort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        print(f'left :{left }  right :{right}')
    MergeSort(left)
    MergeSort(right)
    # MergeSort(right)
    # print(left)
    # print(right)
    i=0
    j=0
    
    k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            mylist[k]=left[i]
            i+=1
        else:
            mylist[k]=right[j]
            j+=1
            print(mylist)
        k+=1   
    while i <len(left):
        mylist[k]=mylist[left]
        i+=1
        k+=1
    
    while j<len(right):
        mylist[k]=mylist[right]
        i+=1
        k+=1
        
        
    
mylist=[8,4,6,9]
MergeSort(mylist)
