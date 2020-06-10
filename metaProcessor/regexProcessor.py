from .metaProcessor import MetaProcessor
import re

class RegexProcessor(MetaProcessor):
    """
    Creates a regex processor and finds values inside of a string.
    """
    def __init__(self, phrase, content):
        self.phrase = phrase
        self.content = content
    
    def get_matches(self):
        return re.finditer(self.phrase, self.content)