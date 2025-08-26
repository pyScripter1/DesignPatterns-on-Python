# Правильный подход (с паттерном):
# Использовать единый интерфейс итератора для обхода любых коллекций.

class MyCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):  # Делаем объект итерируемым
        self.index = 0
        return self

    def __next__(self):  # Возвращает следующий элемент
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# Использование
collection = MyCollection()
collection.add_item("First")
collection.add_item("Second")

for item in collection:  # Теперь можно использовать for
    print(item)