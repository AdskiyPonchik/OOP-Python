class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.__old = new_old

    @old.deleter
    def old(self):
        del self.__old

p = Person("Jacob", 20)
del p.old
print(p.__dict__)