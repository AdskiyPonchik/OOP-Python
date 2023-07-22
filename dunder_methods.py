import math


class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Argument should be string")
        return args[0].strip(self.__chars)


class Derivate:  # class decorator
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate  # introducing the class-decorator
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi / 3))


# ---------------------------------------------------------------------

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # show info about object class in Debugging
        return f"{self.__class__}: {self.name}"

    def __str__(self):  # info for user
        return f"{self.name}"


cat = Cat("Timmy")
print(cat)


# ---------------------------------------------------------------------

class Point:
    def __init__(self, x, y, *args: None):
        self.x = x
        self.y = y
        self.__coords = args

    def __len__(self):  # length of string
        return len(self.__coords)

    def __abs__(self):  # module of list/number
        if isinstance(self.__coords, (list, set)):
            return list(map(abs, self.__coords))
        raise TypeError("Absolute value only for hashable type")

    def __eq__(self, other):
        return self.__coords[0] == other.x and self.__coords[1] == other.y


p = Point(-1, 2, -5)
print(len(p))
print(abs(p))


# ---------------------------------------------------------------------

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds should be number")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    @classmethod
    def __validation_check(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Argument should be int or Clock type!")
        return other if type(other) == int else other.seconds

    def __add__(self, other):  # method called for adding
        if not isinstance(other, (int, Clock)):
            raise TypeError("Right operand should be int or Clock type!")
        if type(other) == Clock:  # for adding other class object
            return Clock(self.seconds + other.seconds)
        return Clock(self.seconds + other)

    def __radd__(self, other):  # method for adding integer from left side
        return self + other

    def __iadd__(self, other):  # method for increment
        if not isinstance(other, (int, Clock)):
            raise TypeError("Increment should be int or Clock type!")
        if type(other) == Clock:
            other = other.seconds
        self.seconds += other
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Right operand should be int or Clock type!")
        if type(other) == Clock:  # for adding other class object
            return Clock(self.seconds - other.seconds)
        return Clock(self.seconds - other)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Decrement should be int or Clock type!")
        if type(other) == Clock:
            other = other.seconds
        self.seconds -= other
        return self

    def __eq__(self, other):  # equality check
        sc = self.__validation_check(other)
        return self.seconds == sc

    def __lt__(self, other):  # minority check
        sc = self.__validation_check(other)
        return self.seconds < sc

    def __gt__(self, other):  # majority check
        sc = self.__validation_check(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__validation_check(other)
        return self.seconds <= sc

    def __ge__(self, other):
        sc = self.__validation_check(other)
        return self.seconds >= sc


c1 = Clock(1100)
c2 = Clock(2000)
c1 -= 100  # == c1.__add__(100)
print(c1.get_time())
print(
    c1 != c2)  # Python interpreter use expression 'not(c1 == c2)' instead of '!=' if we haven't __ne__() method in class
print(
    c1 > c2)  # For default, Python just change argument place in: 'c2 < c1'. But in my example I'm using funny '__gt__()'
# ---------------------------------------------------------------------
p1 = Point(1, 2)
p2 = Point(1, 2)
print(hash(p1), hash(p2), sep='\n')
print(p1 == p2)