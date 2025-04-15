class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus by zero")
        return a % b

    def increment(self, a):
        return a + 1

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return number ** 0.5

    def factorial(self, number):
        if number < 0:
            raise ValueError("Cannot calculate factorial of a negative number")
        if number == 0:
            return 1
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulus: ", calc.modulus(10, 5))
    print("Increment: ", calc.increment(10))