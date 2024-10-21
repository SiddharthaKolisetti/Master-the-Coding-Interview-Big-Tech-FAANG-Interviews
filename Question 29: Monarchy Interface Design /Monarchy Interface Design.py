class Person:
    def __init__(self):
        self.name = name
        self.isAlive = True
        self.children = []
        
class Monarchy:
    def __init__(self, king):
        self.king = Person(king)
        self._persons = {self.king.name: self.king}
        
    def birth(self, child, parent):
        parent = self._persons[parent]
        newChild = Person(child)
        parent.children.push(newChild)
        self._persons[child] = newChild
    
    def death(self, name):
        person = self._persons[name]
        if person is None:
            return None
        person.isAlive = False
        
    
    def getOrderOfSuccession(self):
        order = []
        self._DFS(self.king, order)
        return order
        
    def _DFS(self, currentPerson, order):
        if currentPerson.isAlive:
            order.push(currentPerson.name)
        for i in range(len(children)):
            self._DFS(currentPerson.children[i], order)
