from .regexProcessor import RegexProcessor

class MetaYawProcessor(RegexProcessor):
    """
    MetaYawProcessor inherits the RegexProcessor class to find via
    regex the value for the yaw tag.
    The yaw value gives the direction where the picture was taken.
    """
    def __init__(self,
                phrase = b"<Camera:Yaw>(?:((?:\-?\d*)\.(?:\d*)))<\/Camera:Yaw>",
                content)
        RegexProcessor.__init__(self, phrase, content)
    
    def process():
        matches = self.get_matches()
        for match in matches:
                value = match.groups()[0]
                return float(k)