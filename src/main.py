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
    print("Suma:", calc.sum(2, 2))