"""
Simple unit tests for the calculator backend
"""
import math
import pytest
from backend.calculator import (
    CalculatorError,
    add, subtract, multiply, divide, power,
    square, cube, sqrt, cbrt,
    sin_deg, cos_deg, tan_deg, asin_deg, acos_deg, atan_deg,
    log10, ln, exp, factorial, absolute, reciprocal, modulo,
    preprocess_expression, evaluate_expression, determine_operation_type
)

def test_basic_operations():
    """Test basic arithmetic operations"""
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    #