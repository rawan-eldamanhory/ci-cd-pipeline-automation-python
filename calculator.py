"""
Sample Calculator Application.

This is a demo application for CI/CD pipeline demonstration.
It includes various functions to showcase testing, linting, and documentation.
"""

import logging
from typing import List, Union

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Calculator:
    """
    A simple calculator class with basic arithmetic operations.
    """

    def __init__(self, name: str = "Calculator"):
        """
        Initialize the calculator.
        """
        self.name = name
        self.history: List[str] = []
        logger.info("Calculator '%s' initialized", name)

    def add(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        Add two numbers.
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        logger.debug("Addition: %s + %s = %s", a, b, result)
        return result

    def subtract(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        Subtract b from a.
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        logger.debug("Subtraction: %s - %s = %s", a, b, result)
        return result

    def multiply(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        Multiply two numbers.
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        logger.debug("Multiplication: %s * %s = %s", a, b, result)
        return result

    def divide(
        self, a: Union[int, float], b: Union[int, float]
    ) -> float:
        """
        Divide a by b.
        """
        if b == 0:
            logger.error("Attempted division by zero")
            raise ValueError("Cannot divide by zero")

        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        logger.debug("Division: %s / %s = %s", a, b, result)
        return result

    def power(
        self, base: Union[int, float], exponent: Union[int, float]
    ) -> Union[int, float]:
        """
        Raise base to the power of exponent.
        """
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        logger.debug("Power: %s ^ %s = %s", base, exponent, result)
        return result

    def sqrt(self, number: Union[int, float]) -> float:
        """
        Calculate square root of a number.
        """
        if number < 0:
            logger.error(
                "Attempted square root of negative number: %s", number
            )
            raise ValueError(
                "Cannot calculate square root of negative number"
            )

        result: float = float(number ** 0.5)
        self.history.append(f"√{number} = {result}")
        logger.debug("Square root: √%s = %s", number, result)
        return result

    def get_history(self) -> List[str]:
        """
        Get calculation history.
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """
        Clear the calculation history.
        """
        self.history.clear()
        logger.info("History cleared")


class AdvancedCalculator(Calculator):
    """
    Advanced calculator with additional mathematical operations.

    Inherits from Calculator and adds more complex operations.
    """

    def percentage(
        self, number: Union[int, float], percent: Union[int, float]
    ) -> float:
        """
        Calculate percentage of a number.
        """
        result = (number * percent) / 100
        self.history.append(f"{percent}% of {number} = {result}")
        logger.debug("Percentage: %s%% of %s = %s", percent, number, result)
        return result

    def factorial(self, n: int) -> int:
        """
        Calculate factorial of a number.
        """
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer")
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")

        if n in (0, 1):
            result = 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i

        self.history.append(f"{n}! = {result}")
        logger.debug("Factorial: %s! = %s", n, result)
        return result


def main():
    print("="*60)
    print("  CALCULATOR APPLICATION - DEMO")
    print("="*60)
    print()

    calc = Calculator("BasicCalc")

    print("Basic Operations:")
    print(f"  2 + 3 = {calc.add(2, 3)}")
    print(f"  10 - 4 = {calc.subtract(10, 4)}")
    print(f"  5 * 6 = {calc.multiply(5, 6)}")
    print(f"  20 / 4 = {calc.divide(20, 4)}")
    print(f"  2 ^ 8 = {calc.power(2, 8)}")
    print(f"  √16 = {calc.sqrt(16)}")
    print()

    adv_calc = AdvancedCalculator("AdvancedCalc")

    print("Advanced Operations:")
    print(f"  15% of 200 = {adv_calc.percentage(200, 15)}")
    print(f"  5! = {adv_calc.factorial(5)}")
    print()

    print("Calculation History:")
    for operation in calc.get_history():
        print(f" {operation}")

    print("\n" + "="*60)
    print("  Demo complete!")
    print("="*60)


if __name__ == "__main__":
    main()
