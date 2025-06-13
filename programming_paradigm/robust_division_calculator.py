def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Attempt the division
        result = num / den
        return f"Result: {result}"
    
    except ValueError:
        return "Error: Both numerator and denominator must be numeric."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
