class ZeroGoodException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Количество товара не может быть отрицательным или нулевым.'

    def __str__(self):
        return self.message
