class Calculator:
    def sum(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("Suma 2 + 2 =", calc.sum(2, 2))
    print("Resta 5 - 3 =", calc.restar(5, 3))
    print("Multiplicación 3 * 4 =", calc.multiply(3, 4))
    print("División 10 / 2 =", calc.divide(10, 2))