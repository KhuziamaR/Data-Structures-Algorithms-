# Merge Sort 
def merge_sort(a,key='name',descending=False):
    if len(a) <=1:
        return 

    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)

    merge_sorted_array(left,right,a,key,descending)


def merge_sorted_array(arr1,arr2, arr3,key,descending):
    i = j = k = 0
    size1 = len(arr1)
    size2 = len(arr2)
    if descending == False:
        while i <  size1 and j < size2:
            if arr1[i][key] < arr2[j][key]:
                arr3[k] = arr1[i]
                i+=1
                k+=1
            else:
                arr3[k] = arr2[j]
                j+=1
                k+=1
    else:
        while i <  size1 and j < size2:
            if arr1[i][key] > arr2[j][key]:
                arr3[k] = arr1[i]
                i+=1
                k+=1
            else:
                arr3[k] = arr2[j]
                j+=1
                k+=1

        
    while i< size1:
        arr3[k]=arr1[i]
        i+=1
        k+=1
    while j<size2:
        arr3[k]=arr2[j]
        j+=1
        k+=1

# a = [3 ,5,8,9 ,15,90,134]
# b = [1,4,6,8,10,12,42,91,98,144]
c=[434,23423,423,4234,123,7,896,1,32,2,3,4,5]
# merge_sorted_array(a,b,c)
elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
print(elements)
print("     ")
merge_sort(elements, key='age', descending=False)
print(elements)
