from .transformer import transformer

class InchToCentimeter(transformer.py):
    """
    Loads a value in inches and transforms it into
    centimeters.
    """
    def __init__(self, inch_value):
        self.inches = inch_value
    
    def transform():
        return self.inches * 2.54