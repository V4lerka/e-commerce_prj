class MixinPrinter:
    """Класс-миксин, который будет при создании объекта, печатать в консоль информацию о том, от какого класса и с
    какими параметрами был создан объект"""

    def __init__(self):
        print(repr(self))


    def __repr__(self):
        return f"{__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

