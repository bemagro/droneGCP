from .transformer import Transformer
from utm import from_latlon

class DegreesToMeters(Transformer):
    """
    Converts a degrees coordinate to an UTM coordinate.
    """
    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def transform(self):
        """
        returns a 4 values tuple.
        """
        latlon_tuple = from_latlon(self.latitude, self.longitude)

        # asserts not empty
        if len(latlon_tuple) > 1:
            latitude = latlon_tuple[0]
            longitude = latlon_tuple[1]
            number = latlon_tuple[2]
            letter = latlon_tuple[3]

            return longitude, latitude, number, letter
