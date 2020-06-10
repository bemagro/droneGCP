from .metaProcessor import MetaProcessor
import exifread


class ExifProcessor(MetaProcessor):
    """
    Loads the jpg image and extracts its Exif metafeatures

    Parameters
    filepath - str, path to the jpg file
    """
    def __init__(self, filepath):
        self.file = open(filepath, 'rb')
        self._load_tags()

    def _load_tags(self):
        self.tags = exifread.process_file(self.file)
    
    def get_tag(self, tag):
        return self.tags[tag]