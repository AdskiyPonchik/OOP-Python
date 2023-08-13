class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):   #   Returns value if public attribute
        if item == 'x':
            raise ValueError("Access denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):      # setting new attribute
        if key == 'z':
            raise AttributeError(f"There is no {key} attribute")
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):    # method if attribute not exists
        if item not in ['x', 'y']:
            print(f"Attribute {item} is not exists")
        else:
            pass

    def __delattr__(self, item):    # deleting attr
        del self.__dict__[item] # hehe

pt1 = Point(1, 2)
pt1.__getattribute__('y')
pt1.__setattr__('x', 5)
pt1.__getattr__('z')
pt1.__delattr__('y')