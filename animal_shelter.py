# An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat.

class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self,animal):
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if len(self.cats):
            return self.dequeueCat()
        return self.dequeueDog()

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        dog = self.dogs[0]
        self.dogs = self.dogs[1:]
        return dog