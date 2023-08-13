from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, age: int, ps: str, weight: float):
        self.verify_fio(fio)
        self.veriry_age(age)
        self.verify_ps(ps)
        self.veriry_weight(weight)

        self.__fio = fio.split()
        self.age = age
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("Fio should be string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Wrong format")

        letters = ascii_letters = cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("FIO should consists at least one symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError("Wrong symbol")

    @classmethod
    def veriry_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError("Age should be number in range [14; 120]")

    @classmethod
    def veriry_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Weight should be float number from 20 to ?")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Passport should be string")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Incorrect passport format")
        for p in s:
            if not p.isdigit():
                raise TypeError("Series and number of passport should be numbers")

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.veriry_age(new_age)
        self.__age = new_age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.veriry_weight(new_weight)
        self.__weight = new_weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, new_ps):
        self.verify_ps(new_ps)
        self.__passport = new_ps


p = Person("Иванов Иван Владимирович", 30, '1234 567890', 80.0)
p.age = 20
p.passport = '4657 123456'
p.weight = 70.0
print(p.__dict__)