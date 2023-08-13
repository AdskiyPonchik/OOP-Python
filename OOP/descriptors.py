class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:  # raw_data-descriptor
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Coord should be integer")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)  # instance.__dict__[self.name] = value - alternative


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
print(pt.xr, pt.__dict__)
