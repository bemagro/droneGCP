from .exifProcessor import ExifProcessor

class MetaFocalProcessor(ExifProcessor):
    """
    Loads the image metadata and extracts the focal length
    of a given image.
    """
    def __init__(self,
                filepath,
                tag_focal_length = 'EXIF FocalLength'):
        ExifProcessor.__init__(self, filepath)
        self.tag_focal_length = tag_focal_length

    def _value(self, tag):
        """
        Converts tag to value.
        """
        numerator, denominator = str(tag.values[0]).split("/")
        return int(numerator) / int(denominator)

    def process(self):
        focal_length = self.get_tag(self.tag_focal_length)
        focal_length = self._value(focal_length)

        return focal_length