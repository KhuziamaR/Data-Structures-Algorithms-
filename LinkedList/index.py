class Node:
    def __init__(self,data=None , next=None,prev=None):
        self.data = data
        self.next = next 
        self.prev = prev
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head,None)
        self.head = node
        
    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data,None,None)
            return
        itr = self.head
        while(itr.next is not None):
            itr=itr.next
        itr.next = Node(data,None,itr)
    def print(self):
        if(self.head is None):
            print("Linked List is empty")
            return 
        itr = self.head
        while itr != None:
            print(itr.data)
            itr= itr.next
    def get_len(self):
        if self.head is None:
            return 0
        itr = self.head
        count=0
        while itr:
            itr= itr.next
            count+=1 
        return count
    def insert_at(self,index,data):
        if index < 0 or index > self.get_len():
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                return
            itr =itr.next
            count += 1
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr=itr.next
    def remove_by_value(self,data):
        if self.head == None:
            return
        if data == self.head.data:
            self.head=self.head.next
        if self.get_len()==0 or self.get_len()==1:
            self.head=None
            return
        itr= self.head
        prev=self.head
        itr= itr.next
        while itr:
            if data == itr.data:
                prev.next=itr.next
            itr=itr.next
            prev=prev.next
    def print_forward(self):
        if self.head == None:
            return 
        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.next
    def print_backward(self):
        if self.head == None:
            return 
        itr=self.head
        while itr.next != None:
            itr= itr.next
        while itr:
            print(itr.data)
            itr=itr.prev



        


        
        

l = LinkedList()
# a = LinkedList()
data = [1,2,3,4,5,6,7,8,9,0]

# l.insert_at_begining(1)
# l.insert_at_begining(2)
# l.insert_at_begining(3)
# l.insert_at_begining(4)
# l.insert_at_begining(5)
# l.insert_at_begining(6)
# l.insert_at_end(1)
# l.insert_at_end(2)
# l.insert_at_end(3)
# l.insert_at_end(4)
# l.insert_at_end(5)
# # l.insert_at(1,'TWO')
l.insert_values(data)
# l.print_forward()
l.print_backward()
