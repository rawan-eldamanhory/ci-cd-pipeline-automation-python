"""
Test Suite for Calculator Application.

Comprehensive tests using pytest with fixtures, parametrize, and markers.
"""

import pytest

from calculator import AdvancedCalculator, Calculator


@pytest.fixture
def calc():
    """Fixture providing a basic Calculator instance."""
    return Calculator("TestCalc")


@pytest.fixture
def adv_calc():
    """Fixture providing an AdvancedCalculator instance."""
    return AdvancedCalculator("TestAdvCalc")


# ==================== BASIC OPERATIONS TESTS ====================


class TestBasicOperations:
    """Test suite for basic arithmetic operations."""

    def test_addition_integers(self, calc):
        """Test addition with integers."""
        assert calc.add(2, 3) == 5
        assert calc.add(0, 0) == 0
        assert calc.add(-1, 1) == 0
        assert calc.add(-5, -3) == -8

    def test_addition_floats(self, calc):
        """Test addition with floating point numbers."""
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtraction_integers(self, calc):
        """Test subtraction with integers."""
        assert calc.subtract(10, 3) == 7
        assert calc.subtract(5, 5) == 0
        assert calc.subtract(3, 10) == -7
        assert calc.subtract(-5, -3) == -2

    def test_subtraction_floats(self, calc):
        """Test subtraction with floating point numbers."""
        assert calc.subtract(5.5, 2.3) == pytest.approx(3.2)
        assert calc.subtract(10.1, 5.05) == pytest.approx(5.05)

    def test_multiplication_integers(self, calc):
        """Test multiplication with integers."""
        assert calc.multiply(4, 5) == 20
        assert calc.multiply(0, 100) == 0
        assert calc.multiply(-3, 4) == -12
        assert calc.multiply(-2, -6) == 12

    def test_multiplication_floats(self, calc):
        """Test multiplication with floating point numbers."""
        assert calc.multiply(2.5, 4) == pytest.approx(10.0)
        assert calc.multiply(1.5, 3.2) == pytest.approx(4.8)

    def test_division_integers(self, calc):
        """Test division with integers."""
        assert calc.divide(10, 2) == pytest.approx(5.0)
        assert calc.divide(7, 2) == pytest.approx(3.5)
        assert calc.divide(-12, 3) == pytest.approx(-4.0)

    def test_division_floats(self, calc):
        """Test division with floating point numbers."""
        assert calc.divide(10.5, 2.0) == pytest.approx(5.25)
        assert calc.divide(7.5, 1.5) == pytest.approx(5.0)

    def test_division_by_zero(self, calc):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_power_integers(self, calc):
        """Test exponentiation with integers."""
        assert calc.power(2, 3) == 8
        assert calc.power(5, 2) == 25
        assert calc.power(10, 0) == 1
        assert calc.power(2, -1) == pytest.approx(0.5)

    def test_sqrt_positive_numbers(self, calc):
        """Test square root with positive numbers."""
        assert calc.sqrt(16) == pytest.approx(4.0)
        assert calc.sqrt(25) == pytest.approx(5.0)
        assert calc.sqrt(2) == pytest.approx(1.414, rel=1e-3)
        assert calc.sqrt(0) == pytest.approx(0.0)

    def test_sqrt_negative_number(self, calc):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(
            ValueError,
            match="Cannot calculate square root of negative number"
        ):
            calc.sqrt(-16)


# ==================== PARAMETRIZED TESTS ====================


class TestParametrizedOperations:
    """Test suite using parametrization for comprehensive coverage."""

    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 2),
        (5, 10, 15),
        (-3, 3, 0),
        (100, 200, 300),
        (0, 0, 0),
    ])
    def test_addition_parametrized(self, calc, a, b, expected):
        """Parametrized test for addition."""
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 5),
        (20, 8, 12),
        (0, 5, -5),
        (7, 7, 0),
    ])
    def test_subtraction_parametrized(self, calc, a, b, expected):
        """Parametrized test for subtraction."""
        assert calc.subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (5, 5, 25),
        (10, 0, 0),
        (-2, 5, -10),
    ])
    def test_multiplication_parametrized(self, calc, a, b, expected):
        """Parametrized test for multiplication."""
        assert calc.multiply(a, b) == expected

    @pytest.mark.parametrize("base, exp, expected", [
        (2, 2, 4),
        (3, 3, 27),
        (5, 0, 1),
        (10, 2, 100),
    ])
    def test_power_parametrized(self, calc, base, exp, expected):
        """Parametrized test for power operation."""
        assert calc.power(base, exp) == expected


# ==================== HISTORY TESTS ====================


class TestHistory:
    """Test suite for calculation history functionality."""

    def test_history_records_operations(self, calc):
        """Test that operations are recorded in history."""
        calc.add(2, 3)
        calc.multiply(4, 5)

        history = calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history
        assert "4 * 5 = 20" in history

    def test_history_clear(self, calc):
        """Test clearing calculation history."""
        calc.add(1, 1)
        calc.subtract(5, 3)

        assert len(calc.get_history()) == 2

        calc.clear_history()
        assert len(calc.get_history()) == 0

    def test_history_isolation(self):
        """Test that history is isolated between instances."""
        calc1 = Calculator("Calc1")
        calc2 = Calculator("Calc2")

        calc1.add(1, 2)
        calc2.add(3, 4)

        assert len(calc1.get_history()) == 1
        assert len(calc2.get_history()) == 1
        assert calc1.get_history() != calc2.get_history()


# ==================== ADVANCED CALCULATOR TESTS ====================


class TestAdvancedCalculator:
    """Test suite for AdvancedCalculator operations."""

    def test_percentage_basic(self, adv_calc):
        """Test basic percentage calculations."""
        assert adv_calc.percentage(200, 15) == pytest.approx(30.0)
        assert adv_calc.percentage(50, 20) == pytest.approx(10.0)
        assert adv_calc.percentage(100, 50) == pytest.approx(50.0)

    @pytest.mark.parametrize("number, percent, expected", [
        (100, 10, 10.0),
        (200, 25, 50.0),
        (50, 50, 25.0),
        (1000, 5, 50.0),
    ])
    def test_percentage_parametrized(
        self, adv_calc, number, percent, expected
    ):
        """Parametrized test for percentage calculations."""
        assert adv_calc.percentage(number, percent) == pytest.approx(
            expected
        )

    def test_factorial_basic(self, adv_calc):
        """Test basic factorial calculations."""
        assert adv_calc.factorial(0) == 1
        assert adv_calc.factorial(1) == 1
        assert adv_calc.factorial(5) == 120
        assert adv_calc.factorial(10) == 3628800

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
    ])
    def test_factorial_parametrized(self, adv_calc, n, expected):
        """Parametrized test for factorial."""
        assert adv_calc.factorial(n) == expected

    def test_factorial_negative(self, adv_calc):
        """Test factorial with negative number raises error."""
        with pytest.raises(
            ValueError,
            match="Factorial not defined for negative numbers"
        ):
            adv_calc.factorial(-5)

    def test_factorial_float(self, adv_calc):
        """Test factorial with float raises error."""
        with pytest.raises(ValueError, match="Factorial requires an integer"):
            adv_calc.factorial(5.5)

    def test_inheritance(self, adv_calc):
        """Test that AdvancedCalculator inherits basic operations."""
        # Should have access to basic Calculator methods
        assert adv_calc.add(2, 3) == 5
        assert adv_calc.multiply(4, 5) == 20
        assert adv_calc.divide(10, 2) == pytest.approx(5.0)


# ==================== INTEGRATION TESTS ====================


class TestIntegration:
    """Integration tests for complex calculation scenarios."""

    def test_complex_calculation_sequence(self, calc):
        """Test a sequence of related calculations."""
        # (10 + 5) * 2 / 3 = 10
        result1 = calc.add(10, 5)  # 15
        result2 = calc.multiply(result1, 2)  # 30
        result3 = calc.divide(result2, 3)  # 10

        assert result3 == pytest.approx(10.0)
        assert len(calc.get_history()) == 3

    def test_calculator_state_management(self, calc):
        """Test calculator maintains state correctly."""
        # Perform several operations
        calc.add(1, 2)
        calc.subtract(5, 3)
        calc.multiply(4, 5)

        # Check history
        history = calc.get_history()
        assert len(history) == 3

        # Clear and verify
        calc.clear_history()
        assert len(calc.get_history()) == 0

        # New operation should start fresh history
        calc.add(10, 20)
        assert len(calc.get_history()) == 1


# ==================== EDGE CASES ====================


class TestEdgeCases:
    """Test suite for edge cases and boundary conditions."""

    def test_very_large_numbers(self, calc):
        """Test operations with very large numbers."""
        large_num = 10**100
        result = calc.add(large_num, large_num)
        assert result == 2 * large_num

    def test_very_small_numbers(self, calc):
        """Test operations with very small numbers."""
        small_num = 10**-10
        result = calc.add(small_num, small_num)
        assert result == pytest.approx(2 * small_num)

    def test_mixed_integer_float_operations(self, calc):
        """Test operations mixing integers and floats."""
        result = calc.add(5, 2.5)
        assert result == pytest.approx(7.5)

        result = calc.multiply(3, 1.5)
        assert result == pytest.approx(4.5)

    def test_zero_operations(self, calc):
        """Test operations involving zero."""
        assert calc.add(0, 0) == 0
        assert calc.multiply(100, 0) == 0
        assert calc.power(0, 5) == 0
        assert calc.sqrt(0) == pytest.approx(0.0)


# ==================== MARKERS ====================


@pytest.mark.slow
class TestPerformance:
    """Tests marked as slow for performance testing."""

    def test_factorial_large_number(self, adv_calc):
        """Test factorial with larger number (slower operation)."""
        result = adv_calc.factorial(20)
        assert result == 2432902008176640000

    def test_many_operations(self, calc):
        """Test performing many operations."""
        for i in range(1000):
            calc.add(i, i)

        assert len(calc.get_history()) == 1000


@pytest.mark.smoke
class TestSmoke:
    """Smoke tests for basic functionality verification."""

    def test_calculator_creation(self):
        """Test calculator can be created."""
        calc = Calculator()
        assert calc is not None

    def test_basic_add(self, calc):
        """Smoke test for addition."""
        assert calc.add(1, 1) == 2

    def test_advanced_calculator_creation(self):
        """Test advanced calculator can be created."""
        adv_calc = AdvancedCalculator()
        assert adv_calc is not None


# ==================== TEST SUMMARY ====================


def test_suite_info():
    """Print information about the test suite."""
    print("\n" + "="*60)
    print("  CALCULATOR TEST SUITE")
    print("="*60)
    print("\nTest Coverage:")
    print(" Basic operations (add, subtract, multiply, divide)")
    print(" Advanced operations (power, sqrt, percentage, factorial)")
    print(" Error handling (division by zero, negative sqrt, etc.)")
    print(" History management")
    print(" Edge cases and boundary conditions")
    print(" Integration tests")
    print(" Parametrized tests for comprehensive coverage")
    print("\n" + "="*60)
