from .transformer import Transformer

class InchToCentimeter(Transformer):
    """
    Loads a value in inches and transforms it into
    centimeters.
    """
    def __init__(self, inch_value):
        self.inches = inch_value
    
    def transform(self):
        return self.inches * 2.54