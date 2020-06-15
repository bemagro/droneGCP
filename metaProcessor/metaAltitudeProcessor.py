from .exifProcessor import ExifProcessor

class MetaAltitudeProcessor(ExifProcessor):
    """
    Loads the image metadata and extracts the height of a given
    image
    """
    def __init__(self,
                filepath,
                tag_altitude = 'GPS GPSAltitude'):
        ExifProcessor.__init__(self, filepath)
        self.tag_altitude = tag_altitude

    def _to_meters(self, tag):
        """
        Splits a object into 2 values and divides it.
        """
        numerator, divisor = str(tag.values[0]).split("/")

        return int(numerator) / int(divisor)

    def process(self):
        altitude = self.get_tag(self.tag_altitude)
        altitude = self._to_meters(altitude)

        return altitude