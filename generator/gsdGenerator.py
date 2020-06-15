from .generator import Generator
from math import atan, cos


class GsdGenerator(Generator):
    """
    SensorWidthGenerator calculates the sensor width

    Arguments
    sensor_width - float, size of camera's sensor width
    focal_length - float, cameras focal length
    flight_height - int, relative altitude
    image_width - int, image width
    """
    def __init__(self,
                sensor_width,
                focal_length,
                flight_height,
                image_width):
        self.sensor_width = sensor_width

        self.focal_length = focal_length
        self.flight_height = flight_height
        self.image_width = image_width
    
    def get_gsd(self):
        return (self.sensor_width * self.flight_height * 100) / (self.focal_length * self.image_width)

    def generate(self):
        return self.get_gsd()
