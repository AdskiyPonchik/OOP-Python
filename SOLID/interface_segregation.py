"""
My code follows the Interface Segregation Principle (ISP).
The ISP states that clients should not be forced to depend on interfaces that they do not use.
In this code provided, the Creature interface has three methods: swim(), walk(), and talk().
However, not all creatures can do all three things. For example, fish can swim and walk, but they cannot talk.
Cats can walk and swim, but they cannot talk. And humans can swim, walk, and talk.
This means that the Creature interface is not forcing clients to depend on methods that they do not use.
For example, a client that only needs to work with fish can simply implement the SwimmerInterface interface. This would make the code more modular and easier to maintain.
Here is a brief explanation of how the ISP applies to the code you provided:
The Creature interface has three methods: swim(), walk(), and talk().
Not all creatures can do all three things
This means that the Creature interface is not forcing clients to depend on methods that they do not use.
For example, a client that only needs to work with fish can simply implement the SwimmerInterface interface.
By following the ISP, you can create code that is more modular and easier to maintain. This is because your code will be less coupled,
which means that it will be easier to change and adapt to new requirements.
"""
class Creature:
    def __init__(self, name):
        self.name = name

class SwimmerInterface:
    def swim(self):
        pass

class WalkerInterface:
    def walk(self):
        pass

class TalkerInterface:
    def talk(self):
        pass
"""And as you can see, this code also follows the Single Responsibility princip, which we have already covered (if you went in order)"""
class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and i can walk")

    def talk(self):
        print(f"I'm {self.name} and i can talk")

class Fish(Creature, SwimmerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

class Cat(Creature, SwimmerInterface, WalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and i can walk")

human = Human("Daniel")
human.swim()
human.walk()
human.talk()

fish = Fish('Nemo')
fish.swim()

cat = Cat("Garfield")
cat.walk()
cat.swim()