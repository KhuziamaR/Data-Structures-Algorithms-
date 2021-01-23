class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    def getHash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h%100
    def __setitem__(self,key,val):
        h = self.getHash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key and len(element) == 2:
                self.arr[h][index] = (key,val)
                found = True
                break
        if found == False:
            self.arr[h].append((key,val))
        # self.arr[h] = val
    def __getitem__(self,key):
        h = self.getHash(key)
        if (len(self.arr[h])==0):
            return None
        else:
            for element in self.arr[h]:
                if element[0] == key:
                    return element[1]
    def __delitem__(self,key):
        h = self.getHash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index] 
    def keys(self):
        for element in self.arr:
            if len(element) != 0:
                for item in element:
                    print (item[0])
        
    
h = HashTable()
h['march 5'] = 120
h['march 5'] = 130
h['march 7'] = 140
h['march 17'] =134
h['december 17'] =140

# h.keys()
# del h['december 17']
# print(h['march 17'])
# print(h['december 17'])
# print(h['march 5'])
# print(h.arr)

# def getHash(key):
#     h=0
#     for i in key:
#         h+= ord(i)
#     return h%100

  

# ////////////////////////// HASH TABLE QUESTIONS ! //////////////

def firstReccur(arr):
    lookup= dict()
    for num in arr:
        if(num in lookup):
            return num
        else:
            lookup[num]= True

first = [2,5,1,5,3,5,1,2,4]

print(firstReccur(first))
