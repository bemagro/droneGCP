from .metaProcessor import MetaProcessor


class degreesCoordProcessor(MetaProcessor):
    """
    Loads the XMP meta values and gets the latitude and
    longitude values in degrees.
    """
    def __init__(self, metadata):
        self.data = metadata
    
    def process():
        pass