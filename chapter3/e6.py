from .StackAndQueue import *
import unittest


class Animal:
    name: str
    priority: int

    def __init__(self, name: str = "default_name", priority: int = 99999):
        self.name = name
        self.priority = priority


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalShelter:
    cat_queue: Queue
    dog_queue: Queue
    priority: int

    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()
        self.priority = 0

    def enqueue(self, animal: Animal) -> "AnimalShelter":
        animal.priority = self.priority
        self.priority += 1
        if isinstance(animal, Dog):
            self.dog_queue.add(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.add(animal)

        return self

    def dequeue_any(self) -> Animal:
        if self.dog_queue.is_empty():
            animal = self.cat_queue.peek()
            self.cat_queue.remove()
        elif self.cat_queue.is_empty():
            animal = self.dog_queue.peek()
            self.dog_queue.remove()
        elif self.cat_queue.peek().priority < self.dog_queue.peek().priority:
            animal = self.cat_queue.peek()
            self.cat_queue.remove()
        else:
            animal = self.dog_queue.peek()
            self.dog_queue.remove()
        return animal

    def dequeue_dog(self) -> Dog:
        dog = self.dog_queue.peek()
        self.dog_queue.remove()
        return dog

    def dequeue_cat(self) -> Cat:
        cat = self.cat_queue.peek()
        self.cat_queue.remove()
        return cat


class TestAnimalShelter(unittest.TestCase):
    def test_shelter(self):
        shelter = AnimalShelter()
        d1 = Dog()
        c1 = Cat()

        s = shelter.enqueue(d1).enqueue(c1)
        assert s.dequeue_any() == d1

        s = shelter.enqueue(c1).enqueue(d1)
        assert s.dequeue_any() == c1

        s = shelter.enqueue(d1).enqueue(c1)
        assert s.dequeue_dog() == d1

        s = shelter.enqueue(c1).enqueue(d1)
        assert s.dequeue_cat() == c1

        s = shelter.enqueue(d1).enqueue(c1)
        assert s.dequeue_cat() == c1

        s = shelter.enqueue(c1).enqueue(d1)
        assert s.dequeue_dog() == d1


if __name__ == "__main__":
    unittest.main()
