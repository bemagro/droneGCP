from .transformer import transformer
from utm import from_latlon

class DegreesToMeters(transformer):
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
        return from_latlon(self.latitude, self.longitude)
        