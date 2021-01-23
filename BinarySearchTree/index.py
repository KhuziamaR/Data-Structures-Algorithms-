class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return #Node Already Exists
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def search(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements+= self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+= self.right.in_order_traversal()
        return elements
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements+= self.left.in_order_traversal()
        if self.right:
            elements+= self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()
# def find_min(root):
#     p= root
#     while(p.left):
#         p=p.left
#     return p.data
# def find_max(root):
#     p= root
#     while(p.right):
#         p=p.right
#     return p.data
        
        
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = build_tree(countries)

print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())


print(numbers_tree.find_min())


