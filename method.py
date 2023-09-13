# def Bubble(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     print(arr)
        





# Bubble([1,5,4,6,12,9])

def insertion(arr):
    for i in range(1,len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b-1],arr[b]=arr[b],arr[b-1]
            b-=1
    print(arr)
    
arr=[3,4,9,8,7,6,12,11]
insertion(arr)