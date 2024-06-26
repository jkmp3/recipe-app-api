"""
Sample test cases
"""
from django.test import SimpleTestCase

from app import calculator


class CalculatorTests(SimpleTestCase):
    """Tests functions of calculator module."""

    def test_add_numbers(self) -> None:
        """Tests the add function with numbers."""
        result = calculator.add(1, 3)
        self.assertEqual(result, 4)

    def test_subtract_numbers(self) -> None:
        """Tests the subtract function with numbers"""
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)
