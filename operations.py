class CalculatorBMI:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @staticmethod
    def calculate(weight, height):
        result = weight / (height ** 2)
        return round(result, 1)
