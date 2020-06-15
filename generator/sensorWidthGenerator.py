from .generator import Generator
from math import atan, cos

class SensorWidthGenerator(Generator):
    """
    SensorWidthGenerator calculates the sensor width

    Arguments
    width - int, image width
    height - int, image height
    diagonal - float, sensor diagonal
    crop_factor - float, crop factor
    """
    def __init__(self, crop_factor, width, height):
        self.crop_factor = crop_factor

        self.width = width
        self.height = height

        self._diagonal_dimension()
    
    def _diagonal_dimension(self):
        self.diagonal_dimension = 43.2666 / self.crop_factor

    def get_angle(self):
        return atan(self.height/ self.width)

    def _sensor_width(self):
        angle = self.get_angle()
        
        return self.diagonal_dimension * cos(angle)
    
    def generate(self):
        return self._sensor_width()
