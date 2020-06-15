from .exifProcessor import ExifProcessor

class MetaAdjFocalProcessor(ExifProcessor):
    """
    Loads the image metadata and extracts the height of a given
    image.
    """
    def __init__(self,
                filepath,
                tag_focal_length = 'EXIF FocalLengthIn35mmFilm'):
        ExifProcessor.__init__(self, filepath)
        self.tag_focal_length = tag_focal_length

    def _value(self, tag):
        """
        Converts tag to value.
        """
        return tag.values[0]

    def process(self):
        focal_length = self.get_tag(self.tag_focal_length)
        focal_length = self._value(focal_length)

        return focal_length