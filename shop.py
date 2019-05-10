class Basket():
    def __init__(self):
        self.items = []

class Goods():
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Coca_Cola(Goods):
    def __init__(self):
        super().__init__(name='Кока Кола', value=49)

    def get_good(self, basket):
        coca_cola = Coca_Cola()
        basket.items.append(coca_cola)
        if coca_cola in basket.items:
            print('Вы купили этот товар(', coca_cola.name, ')!')


class Choco_Pie(Goods):
    def __init__(self):
        super().__init__(name='Чоко Пай', value=49)

    def get_good(self, basket):
        choco_pie = Choco_Pie()
        basket.items.append(choco_pie)
        if choco_pie in basket.items:
            print('Вы купили этот товар(', choco_pie.name, ')!')


basket = Basket()
print('Добро пожаловать в магазин!')
print('Список имеющихся товаров:\n1 - ', Coca_Cola().name, '\n2 - ', Choco_Pie().name, '\n3 - ...')
choice = int(input('Чего желаете?\n'))
if choice == 1:
    Coca_Cola().get_good(basket)
if choice == 2:
    Choco_Pie().get_good(basket)