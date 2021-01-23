# 6,5,3,1,8,7,2,4 
# BUBBLE SORT AND SELECTION SORT 
def bubbleSort(arr,key="transaction_amount"):
    for t in range(len(arr)-1):
        swapped = False
        for i in range(len(arr)-1-t):
            if (arr[i][key]>arr[i+1][key]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped = True
            if not swapped:
                break
    return arr

# iterate over list, keep track of smallest number, swap smallest with index, increment index
def selectionSort(arr):
    for i in range(len(arr)):
        smallest_index=i
        for j in range(len(arr)):
            if arr[smallest_index]<arr[j]:
                smallest_index=j
            arr[smallest_index],arr[i] = arr[i],arr[smallest_index]
    return arr

# loop over elements, if one is greater than the other, [place]
def insertionSort(A):
    for i in range(len(A)):
        key = A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j = j - 1
        A[j+1]=key
    return A


            

arr = [3,2,4,6,1,5,7]
print(insertionSort(arr))
# print(selectionSort(arr))
    
              
        
        




arr = [6,4,2,5,7,3,8,3,9,2]
# print(bubbleSort(arr))
    
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
# print(bubbleSort(elements,'name'))


