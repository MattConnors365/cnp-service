import random

def generate_unique_code():
    """
    Generates a unique sequence between "001" and "999"
    Returns: 
        str: A 3-digit string representation (zero-padded)
    """
    unique_code = random.randint(1, 999)
    return f"{unique_code:03}"
