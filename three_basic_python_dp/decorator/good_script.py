# Правильный подход (с паттерном):
# Создаем классы-декораторы, которые "оборачивают" базовый объект.

# Базовый компонент
class Coffee:
    def cost(self):
        return 90

# Базовый класс декоратора
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee  # Храним ссылку на декорируемый объект

# Конкретные декораторы
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 30  # Добавляем стоимость молока

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 10  # Добавляем стоимость сахара

# Использование
simple_coffee = Coffee()
print("Простой кофе:", simple_coffee.cost())  # 90

latte = MilkDecorator(simple_coffee)  # Оборачиваем кофе в декоратор молока
print("Латте:", latte.cost())  # 90 + 30 = 120

sweet_latte = SugarDecorator(latte)  # Оборачиваем латте в декоратор сахара
print("Сладкий латте:", sweet_latte.cost())  # 120 + 10 = 130

# Можно создавать любые комбинации!
just_sweet_coffee = SugarDecorator(simple_coffee)
print("Кофе с сахаром:", just_sweet_coffee.cost())  # 90 + 10 = 100