"""
Calculator engine with arithmetic and scientific operations
All trigonometric functions work in DEGREES
"""
import math
import re

class CalculatorError(Exception):
    """Custom exception for calculator errors"""
    pass

# Mathematical operations

def add(a, b):
    """Addition"""
    return a + b

def subtract(a, b):
    """Subtraction"""
    return a - b

def multiply(a, b):
    """Multiplication"""
    return a * b

def divide(a, b):
    """Division with zero check"""
    if b == 0:
        raise CalculatorError("Division by zero")
    return a / b

def power(a, b):
    """Power operation a^b"""
    try:
        return math.pow(a, b)
    except ValueError as e:
        raise CalculatorError(f"Invalid power operation: {str(e)}")
    except OverflowError:
        raise CalculatorError("Result too large")

def square(a):
    """Square of a number"""
    return a * a

def cube(a):
    """Cube of a number"""
    return a * a * a

def sqrt(a):
    """Square root with domain check"""
    if a < 0:
        raise CalculatorError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def cbrt(a):
    """Cube root"""
    if a < 0:
        return -math.pow(-a, 1/3)
    return math.pow(a, 1/3)

# Trigonometric functions (DEGREES mode)

def sin_deg(a):
    """Sine in degrees"""
    return math.sin(math.radians(a))

def cos_deg(a):
    """Cosine in degrees"""
    return math.cos(math.radians(a))

def tan_deg(a):
    """Tangent in degrees"""
    return math.tan(math.radians(a))

def asin_deg(a):
    """Arcsine in degrees"""
    if a < -1 or a > 1:
        raise CalculatorError("Domain error: arcsin requires input between -1 and 1")
    return math.degrees(math.asin(a))

def acos_deg(a):
    """Arccosine in degrees"""
    if a < -1 or a > 1:
        raise CalculatorError("Domain error: arccos requires input between -1 and 1")
    return math.degrees(math.acos(a))

def atan_deg(a):
    """Arctangent in degrees"""
    return math.degrees(math.atan(a))

# Logarithmic functions

def log10(a):
    """Logarithm base 10"""
    if a <= 0:
        raise CalculatorError("Logarithm requires positive number")
    return math.log10(a)

def ln(a):
    """Natural logarithm"""
    if a <= 0:
        raise CalculatorError("Natural logarithm requires positive number")
    return math.log(a)

# Exponential functions

def exp(a):
    """e^x"""
    try:
        return math.exp(a)
    except OverflowError:
        raise CalculatorError("Result too large")

# Other functions

def factorial(n):
    """Factorial with integer check"""
    if n < 0:
        raise CalculatorError("Factorial requires non-negative number")
    if n != int(n):
        raise CalculatorError("Factorial requires integer")
    if n > 170:
        raise CalculatorError("Number too large for factorial")
    return math.factorial(int(n))

def absolute(a):
    """Absolute value"""
    return abs(a)

def reciprocal(a):
    """1/x"""
    if a == 0:
        raise CalculatorError("Cannot calculate reciprocal of zero")
    return 1 / a

def modulo(a, b):
    """Modulo operation"""
    if b == 0:
        raise CalculatorError("Modulo by zero")
    return a % b

# Expression evaluation

def preprocess_expression(expression):
    """
    Preprocess the expression to replace special functions and symbols
    with Python-compatible syntax
    """
    expr = expression.strip()

    # Replace mathematical symbols
    expr = expr.replace('×', '*')
    expr = expr.replace('÷', '/')
    expr = expr.replace('π', str(math.pi))
    expr = expr.replace('e', str(math.e))

    # Replace function names with Python equivalents (degrees mode)
    replacements = {
        'sin(': 'sin_deg(',
        'cos(': 'cos_deg(',
        'tan(': 'tan_deg(',
        'asin(': 'asin_deg(',
        'acos(': 'acos_deg(',
        'atan(': 'atan_deg(',
        'log(': 'log10(',
        'ln(': 'ln(',
        'sqrt(': 'sqrt(',
        'cbrt(': 'cbrt(',
        'abs(': 'absolute(',
        'exp(': 'exp(',
    }

    for old, new in replacements.items():
        expr = expr.replace(old, new)

    # Handle special patterns
    # x² -> x**2
    expr = re.sub(r'(\d+)²', r'\1**2', expr)
    # x³ -> x**3
    expr = re.sub(r'(\d+)³', r'\1**3', expr)
    # x! -> factorial(x)
    expr = re.sub(r'(\d+)!', r'factorial(\1)', expr)

    return expr

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression

    Args:
        expression (str): Mathematical expression to evaluate

    Returns:
        float: Result of the evaluation

    Raises:
        CalculatorError: If expression is invalid or calculation fails
    """
    if not expression or expression.strip() == '':
        raise CalculatorError("Empty expression")

    try:
        # Preprocess the expression
        processed_expr = preprocess_expression(expression)

        # Create a safe namespace with allowed functions
        safe_namespace = {
            '__builtins__': {},
            'sin_deg': sin_deg,
            'cos_deg': cos_deg,
            'tan_deg': tan_deg,
            'asin_deg': asin_deg,
            'acos_deg': acos_deg,
            'atan_deg': atan_deg,
            'log10': log10,
            'ln': ln,
            'sqrt': sqrt,
            'cbrt': cbrt,
            'exp': exp,
            'factorial': factorial,
            'absolute': absolute,
            'abs': absolute,
            'pow': power,
        }

        # Evaluate the expression
        result = eval(processed_expr, safe_namespace)

        # Check for infinity or NaN
        if math.isinf(result):
            raise CalculatorError("Result is infinity")
        if math.isnan(result):
            raise CalculatorError("Result is not a number")

        return float(result)

    except CalculatorError:
        raise
    except ZeroDivisionError:
        raise CalculatorError("Division by zero")
    except SyntaxError:
        raise CalculatorError("Invalid expression syntax")
    except NameError as e:
        raise CalculatorError(f"Unknown function or variable: {str(e)}")
    except Exception as e:
        raise CalculatorError(f"Calculation error: {str(e)}")

def determine_operation_type(expression):
    """
    Determine if expression is arithmetic or scientific

    Args:
        expression (str): The mathematical expression

    Returns:
        str: 'arithmetic' or 'scientific'
    """
    scientific_keywords = [
        'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
        'log', 'ln', 'sqrt', 'cbrt', 'exp', 'abs',
        'π', '²', '³', '!', 'e'
    ]

    expr_lower = expression.lower()
    for keyword in scientific_keywords:
        if keyword in expr_lower:
            return 'scientific'

    return 'arithmetic'

# Testing
if __name__ == '__main__':
    # Test cases
    test_cases = [
        "2 + 2",
        "10 - 5",
        "3 × 4",
        "15 ÷ 3",
        "2 ** 3",
        "sqrt(16)",
        "sin(30)",
        "cos(60)",
        "tan(45)",
        "log(100)",
        "ln(2.718281828459045)",
        "abs(-5)",
        "5!",
    ]

    print("Calculator Engine Test")
    print("=" * 50)

    for expr in test_cases:
        try:
            result = evaluate_expression(expr)
            op_type = determine_operation_type(expr)
            print(f"{expr:30} = {result:15.6f} [{op_type}]")
        except CalculatorError as e:
            print(f"{expr:30} ERROR: {e}")

    print("\nTesting error cases:")
    error_cases = ["5 / 0", "sqrt(-1)", "log(0)", "1000!"]
    for expr in error_cases:
        try:
            result = evaluate_expression(expr)
            print(f"{expr:30} = {result}")
        except CalculatorError as e:
            print(f"{expr:30} ERROR: {e}")
