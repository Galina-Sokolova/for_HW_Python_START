# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:

    def __init__(self, name):
        self.name = name


class Fishes(Animals):

    def __init__(self, name, depth):
        self.depth = depth
        super().__init__(name)

    def his_depth(self):
        return f'Глубина обитания {self.name} около {self.depth} m'


class Birds(Animals):

    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        super().__init__(name)

    def his_wingspan(self):
        return f'Размах крыльев {self.name} около {self.wingspan} sm'


class Mammals(Animals):

    def __init__(self, name, wooliness):
        self.wooliness = wooliness
        super().__init__(name)

    def his_wooliness(self):
        return f'Длина шерсти особи {self.name} около {self.wooliness} sm'


class AnimalFabric:

    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"fishes": Fishes, "birds": Birds, "mammals": Mammals}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fish = Fishes('Сatfish', 4.0)
    bird = Birds('Falcon', 135)
    mammal = Mammals('Bear', 5)
    print(fish.his_depth())
    print(bird.his_wingspan())
    print(mammal.his_wooliness())

    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("fishes", "carp", 1)
    animal_from_fabric.commands = ["swim", "eat"]
    print(animal_from_fabric)
    print(animal_from_fabric.__dict__, type(animal_from_fabric))
