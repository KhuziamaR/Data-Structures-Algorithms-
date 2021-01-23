
def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    
    end = len(elements)-1
    while start<end:
        while start<len(elements) and elements[start] <= pivot:
            start+=1
        while elements[end]> pivot:
            end -=1
        if start<end:
            elements[start],elements[end] = elements[end],elements[start]
    elements[pivot_index],elements[end] = elements[end],elements[pivot_index]
    return end

def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1)
        quick_sort(elements,pi+1,end)





elements =  [11,5,13,3,19,21,2,99]
quick_sort(elements,0,len(elements)-1)
print(elements)