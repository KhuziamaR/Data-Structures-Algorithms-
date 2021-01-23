names=[1,2,3,4]
names2=[5,6,7,8,9,10]


# def reverseList(str):
#     if(len(str) < 2 or not str):
#         return str
#     res=[]
#     for i in str:
#         res.insert(0,i)
#     return res;
    
def reverseListV2(str):
    return str[::-1]

# print(reverseListV2(names))
# print(reverseList(names2)) 

# ///// MERGE TWO SORTED ARRAYS! 

def mergeSorted(arr1,arr2,n1,n2):
    arr3 = [None] * (n1 + n2)
    i=0
    j=0
    k=0
    while(i<n1 and j<n2):
        if(arr1[i]<arr2[j]):
            arr3[k]=arr1[i]
            i=i+1
            k=k+1
        else:
            arr3[k]=arr2[j]
            j=j+1
            k=k+1
    while(i<n1):
        arr3[k]=arr1[i]
        i=i+1
        k=k+1
    while(j<n2):
        arr3[k]=arr2[j]
        j=j+1
        k=k+1
    print("Merged Array: ")
    for i in range(n1+n2):
        print(arr3[i], " ")


# mergeSorted(names,names2,len(names),len(names2))


# iterate through array, total =0 , add total to next element, if total is greater than 

