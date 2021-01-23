# class TreeNode:
#     def __init__(self, name,pos):
#         self.name = name
#         self.pos = pos
#         self.children = []
#         self.parent = None

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level

#     def print_tree(self,str):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         if str == 'both':
#             print(prefix + self.name + ' ('+ self.pos+')')
#         if str == 'name':
#             print(prefix + self.name)
#         if str == 'designation':
#             print(prefix + '('+ self.pos +')')
#         if self.children:
#             for child in self.children:
#                 child.print_tree(str)

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
# def build_management_tree():
#     root = TreeNode("Nilupul","CEO")
#     chinay = TreeNode("Chinmay", "CTO")

# # def build_product_tree():
# #     root = TreeNode("Electronics")

# #     laptop = TreeNode("Laptop")
# #     laptop.add_child(TreeNode("Mac"))
# #     laptop.add_child(TreeNode("Surface"))
# #     laptop.add_child(TreeNode("Thinkpad"))

# #     cellphone = TreeNode("Cell Phone")
# #     cellphone.add_child(TreeNode("iPhone"))
# #     cellphone.add_child(TreeNode("Google Pixel"))
# #     cellphone.add_child(TreeNode("Vivo"))

# #     tv = TreeNode("TV")
# #     tv.add_child(TreeNode("Samsung"))
# #     tv.add_child(TreeNode("LG"))

# #     root.add_child(laptop)
# #     root.add_child(cellphone)
# #     root.add_child(tv)

# #     root.print_tree()

# # build_product_tree()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if(self.get_level()<=level):
            print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree(1)
build_product_tree()

