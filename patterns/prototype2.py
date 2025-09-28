import copy

class Tree:
    def __init__(self, name: str, children=[]):
        self.name = name
        self.children = children

    def __copy__(self):
        return self.__class__(self.name, self.children)

    def __deepcopy__(self, mem):
        if id(self) in mem:
            return mem[id(self)]
        return self.__class__(self.name, copy.deepcopy(self.children))

    def __repr__(self):
        return self.name + ('' if not self.children else f"->{self.children}")


tree1 = Tree("root", [Tree("child1"), Tree("child2")])
tree2 = copy.deepcopy(tree1)

tree2.children.append(Tree("child3"))  # Добавляем узел только в копию

print(tree1)  # Должно вывести только "child1" и "child2"
print(tree2)  # Должно вывести "child1", "child2" и "child3"

