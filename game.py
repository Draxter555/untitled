class Basket():
    def init(self):
        self.items = []

class Goods():
    def init(self, name, value):
        self.name = name
        self.value = value


class Coca_Cola(Goods):
    def init(self):
        super().init(name='Кока Кола', value=49)

    def get_good(self, basket):
        coca_cola = Coca_Cola()
        basket.items.append(coca_cola)
        if coca_cola in basket.items:
            print('Вы купили этот товар(', coca_cola.name, ')!')


basket = Basket()
print('Добро пожаловать в магазин!')
print('Список имеющихся товаров:\n1 - Кока Кола\n2 - ...\n3 - ...')
choice = int(input('Чего желаете?\n'))
if choice == 1:
    Coca_Cola().get_good(basket)