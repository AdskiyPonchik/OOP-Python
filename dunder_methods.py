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


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # show info about object class in Debugging
        return f"{self.__class__}: {self.name}"

    def __str__(self):  # info for user
        return f"{self.name}"


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):  # length of string
        return len(self.__coords)

    def __abs__(self):  # module of list/number
        return list(map(abs, self.__coords))


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


@Derivate
def df_sin(x):
    return math.sin(x)


# ------------------------------------------------------------------
print(df_sin(math.pi / 3))
cat = Cat("Timmy")
print(cat)
# ------------------------------------------------------------------
p = Point(-1, 2, -5)
print(len(p))
print(abs(p))
# ------------------------------------------------------------------
c1 = Clock(1000)
print(c1.get_time())
