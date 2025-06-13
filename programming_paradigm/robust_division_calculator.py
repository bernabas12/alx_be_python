def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Attempt the division
        result = num / den
        return result
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
