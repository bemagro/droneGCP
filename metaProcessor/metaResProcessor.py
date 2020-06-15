from .exifProcessor import ExifProcessor

class MetaResProcessor(ExifProcessor):
    """
    """
    def __init__(self,
                filepath,
                tag_xres = 'Image XResolution',
                tag_yres = 'Image YResolution'):
        ExifProcessor.__init__(self, filepath)
        self.tag_xres = tag_xres
        self.tag_yres = tag_yres

    def _to_cm(self, tag):
        """
        """
        unit = self.get_tag('Image ResolutionUnit').values[0]

        value_1 = float(str(tag.values[0]))

        if unit == 2:
            return 2.54 / value_1

        elif unit == 3:
            return 1 / value_1
        
        elif unit == 4:
            return 1 / (value_1 * 10)

    def process(self):
        xres = self.get_tag(self.tag_xres)
        yres = self.get_tag(self.tag_yres)

        xres = self._to_cm(xres)
        yres = self._to_cm(yres)

        return xres, yres