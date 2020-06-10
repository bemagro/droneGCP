from .trasformer import Transformer
from math import sqrt


class CoordinatesToScalar(Transformer):
    def __init__(self,
                latitude_1,
                longitude_1,
                latitude_2,
                longitude_2):
        self.latitude_1 = latitude_1
        self.longitude_1 = longitude_1
        self.latitude_2 = latitude_2
        self.longitude_2 = longitude_2

    def transform():
        lat_diff = latitude_2 - latitude_1
        lon_diff = longitude_2 - longitude_1

        return sqrt(lat_diff ** 2 + lon_diff ** 2)