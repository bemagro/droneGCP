from .regexProcessor import RegexProcessor


class MetaDfgProcessor(RegexProcessor):
    """
    MetaDfgProcessor, extracts data from the XMP tag after that
    via regex extracts the distance from ground value.
    """
    def __init__(self,
                content,
                phrase = b"<Camera:AboveGroundAltitude>(?:((?:\d*)\.(?:\d*))|(?:(\d*)\/(\d*)))<\/Camera:AboveGroundAltitude>"):
        RegexProcessor.__init__(self, phrase, content)
    
    def process():
        matches = self.get_matches()
        value_1 = matches.groups()[1]               # numerator
        value_2 = matches.groups()[2]               # divisor
        return value_1 / value_2
