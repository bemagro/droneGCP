from .exifProcessor import ExifProcessor

class MetaCoordProcessor(ExifProcessor):
    """
    Loads the image metadata and extracts the coordinates of the points
    returns these values as decimal degrees.

    Parameters
    filepath - str, path to the image
    tag_latitude - str, name of latitude tag
    tag_longitude - str, name of longitude tag
    """
    def __init__(self,
                filepath,
                tag_latitude = 'GPS GPSLatitude',
                tag_longitude = 'GPS GPSLongitude'):
        ExifProcessor.__init__(self, filepath)
        self.tag_latitude = tag_latitude
        self.tag_longitude = tag_longitude

    def _to_degrees(self, tag):
        """
        Converts degree minute seconds coordinate to decimal degrees.

        Parameters
        tag - Ratio obj, contains the coordinates.

        returns
        float - coordinates in decimal degrees.
        """
        degrees = float(tag.values[0].num) / float(tag.values[0].den)
        minutes = float(tag.values[1].num) / float(tag.values[1].den)
        seconds = float(tag.values[2].num) / float(tag.values[2].den)

        return degrees + (minutes / 60.0) + (seconds / 3600.0)

    def process(self):
        latitude = self.get_tag(self.tag_latitude)
        longitude = self.get_tag(self.tag_longitude)

        latitude = self._to_degrees(latitude)
        longitude = self._to_degrees(longitude)

        return longitude, latitude