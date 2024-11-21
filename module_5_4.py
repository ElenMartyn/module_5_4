class House:
    houses_history = []  # история созданных объектов

    def __new__(cls, *args, **kwargs):
        if args:
            cls.houses_history.append(args[0])
        return super(House, cls).__new__(cls)  # вызываем метод new родительского объекта

    def __init__(self, name, number_of_floors):
        self.name = name  # атрибут имени дома
        self.number_of_floors = number_of_floors  # атрибут количества этажей

    def __del__(self):
        # Печатаем сообщение об удалении объекта
        print(f"{self.name} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
h4 = House('ЖК Калыгардыма', 30)
print(House.houses_history)

del h2
del h3
print(House.houses_history)
del h1
print(House.houses_history)