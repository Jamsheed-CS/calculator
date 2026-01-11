"""
Unit tests for the calculator backend
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

def test_arithmetic_operations():
    """Test basic arithmetic operations"""
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    with pytest.raises(CalculatorError):
        divide(10, 0)

def test_power_operations():
    """Test power operations"""
    assert power(2, 3) == 8
    assert power(4, 0.5) == 2
    assert power(0, 0) == 1  # This is a special case
    assert power(2, -1) == 0.5
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8

def test_root_operations():
    """Test root operations"""
    assert square(4) == 16
    assert cube(3) == 27
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    with pytest.raises(CalculatorError):
        sqrt(-1)
    assert cbrt(8) == 2
    assert cbrt(-8) == -2
    assert cbrt(0) == 0

def test_trigonometric_functions():
    """Test trigonometric functions in degrees"""
    # Test common angles
    assert abs(sin_deg(0) - 0) < 1e-10
    assert abs(sin_deg(30) - 0.5) < 1e-10
    assert abs(sin_deg(45) - math.sqrt(2)/2) < 1e-10
    assert abs(sin_deg(60) - math.sqrt(3)/2) < 1e-10
    assert abs(sin_deg(90) - 1) < 1e-10
    
    assert abs(cos_deg(0) - 1) < 1e-10
    assert abs(cos_deg(30) - math.sqrt(3)/2) < 1e-10
    assert abs(cos_deg(45) - math.sqrt(2)/2) < 1e-10
    assert abs(cos_deg(60) - 0.5) < 1e-10
    assert abs(cos_deg(90) - 0) < 1e-10
    
    assert abs(tan_deg(0) - 0) < 1e-10
    assert abs(tan_deg(45) - 1) < 1e-10
    assert abs(tan_deg(30) - 1/math.sqrt(3)) < 1e-10
    
    # Test inverse trigonometric functions
    assert abs(asin_deg(0) - 0) < 1e-10
    assert abs(asin_deg(1) - 90) < 1e-10
    assert abs(acos_deg(1) - 0) < 1e-10
    assert abs(acos_deg(0) - 90) < 1e-10
    with pytest.raises(CalculatorError):
        asin_deg(1.1)  # Out of domain
    with pytest.raises(CalculatorError):
        acos_deg(1.1)  # Out of domain

def test_logarithmic_functions():
    """Test logarithmic functions"""
    assert abs(log10(100) - 2) < 1e-10
    assert abs(log10(1) - 0) < 1e-10
    assert abs(ln(math.e) - 1) < 1e-10
    assert abs(ln(1) - 0) < 1e-10
    with pytest.raises(CalculatorError):
        log10(0)
    with pytest.raises(CalculatorError):
        ln(0)

def test_exponential_functions():
    """Test exponential functions"""
    assert exp(0) == 1
    assert abs(exp(1) - math.e) < 1e-10
    assert abs(exp(2) - math.e**2) < 1e-10

def test_other_functions():
    """Test other mathematical functions"""
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(3) == 6
    with pytest.raises(CalculatorError):
        factorial(-1)
    with pytest.raises(CalculatorError):
        factorial(3.5)
    with pytest.raises(CalculatorError):
        factorial(171)  # Too large
    
    assert absolute(-5) == 5
    assert absolute(5) == 5
    assert absolute(0) == 0
    
    assert reciprocal(2) == 0.5
    assert reciprocal(0.5) == 2
    with pytest.raises(CalculatorError):
        reciprocal(0)
    
    assert modulo(10, 3) == 1
    assert modulo(10, 2) == 0
    with pytest.raises(CalculatorError):
        modulo(10, 0)

def test_preprocess_expression():
    """Test expression preprocessing"""
    # Test symbol replacement
    assert preprocess_expression("2 × 3") == "2 * 3"
    assert preprocess_expression("10 ÷ 2") == "10 / 2"
    assert preprocess_expression("π") == str(math.pi)
    assert preprocess_expression("e") == str(math.e)
    
    # Test function name replacement
    assert preprocess_expression("sin(30)") == "sin_deg(30)"
    assert preprocess_expression("cos(60)") == "cos_deg(60)"
    assert preprocess_expression("sqrt(16)") == "sqrt(16)"
    assert preprocess_expression("log(100)") == "log10(100)"
    assert preprocess_expression("ln(2.718)") == "ln(2.718)"
    
    # Test special patterns
    assert preprocess_expression("2²") == "2**2"
    assert preprocess_expression("3³") == "3**3"
    assert preprocess_expression("5!") == "factorial(5)"

def test_evaluate_expression():
    """Test expression evaluation"""
    # Basic arithmetic
    assert evaluate_expression("2 + 3") == 5
    assert evaluate_expression("10 - 5") == 5
    assert evaluate_expression("3 × 4") == 12
    assert evaluate_expression("15 ÷ 3") == 5
    
    # Scientific functions
    assert abs(evaluate_expression("sin(30)") - 0.5) < 1e-10
    assert abs(evaluate_expression("cos(60)") - 0.5) < 1e-10
    assert abs(evaluate_expression("sqrt(16)") - 4) < 1e-10
    assert abs(evaluate_expression("log(100)") - 2) < 1e-10
    assert abs(evaluate_expression("ln(2.718281828459045)") - 1) < 1e-10
    
    # Complex expressions
    assert abs(evaluate_expression("2 + 3 × 4") - 14) < 1e-10
    assert abs(evaluate_expression("(2 + 3) × 4") - 20) < 1e-10
    
    # Special cases
    assert evaluate_expression("5!") == 120
    assert evaluate_expression("2²") == 4
    assert evaluate_expression("3³") == 27
    
    # Error cases
    with pytest.raises(CalculatorError):
        evaluate_expression("")
    with pytest.raises(CalculatorError):
        evaluate_expression("5 / 0")
    with pytest.raises(CalculatorError):
        evaluate_expression("sqrt(-1)")
    with pytest.raises(CalculatorError):
        evaluate_expression("log(0)")
    with pytest.raises(CalculatorError):
        evaluate_expression("1000!")

def test_determine_operation_type():
    """Test operation type determination"""
    assert determine_operation_type("2 + 3") == "arithmetic"
    assert determine_operation_type("10 - 5") == "arithmetic"
    assert determine_operation_type("3 × 4") == "arithmetic"
    
    assert determine_operation_type("sin(30)") == "scientific"
    assert determine_operation_type("cos(60)") == "scientific"
    assert determine_operation_type("sqrt(16)") == "scientific"
    assert determine_operation_type("log(100)") == "scientific"
    assert determine_operation_type("ln(2.718)") == "scientific"
    
    assert determine_operation_type("2²") == "scientific"
    assert determine_operation_type("3³") == "scientific"
    assert determine_operation_type("5!") == "scientific"
    assert determine_operation_type("π") == "scientific"
    assert determine_operation_type("e") == "scientific"

def test_edge_cases():
    """Test edge cases for various functions"""
    # Test very large numbers
    assert abs(exp(10) - math.exp(10)) < 1e-10
    
    # Test very small numbers
    assert abs(log10(0.01) - (-2)) < 1e-10
    
    # Test negative numbers
    assert sin_deg(-30) == pytest.approx(-0.5)
    assert cos_deg(-60) == pytest.approx(0.5)
    assert tan_deg(-45) == pytest.approx(-1)
    
    # Test zero cases
    assert sqrt(0) == 0
    assert absolute(0) == 0
    assert cbrt(0) == 0

if __name__ == "__main__":
    pytest.main([__file__])
