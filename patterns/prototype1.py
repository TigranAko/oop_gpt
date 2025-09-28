from copy import deepcopy

class Cloner:
    def clone(self):
        return deepcopy(self)

class Character(Cloner):
    def __init__(self, name, lvl, inventory):
        self.name = name
        self.lvl = lvl
        self.inventory = inventory

    def __str__(self):
        return f"Character({self.name=}, {self.lvl=}, {self.inventory=})"

hero1 = Character("Knight", 10, ["sword", "shield"])
hero2 = hero1.clone()

hero2.inventory.append("potion")  # Добавили предмет только в копию

print(hero1)  # Должно быть без "potion"
print(hero2)  # Должно быть с "potion"

