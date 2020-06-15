from PIL import Image
from .loader import Loader

class PillowLoader(Loader):
    """
    PillowLoader

    Interface for loading the .jpg images
    
    Arguments
    image_path - str, path for desired image
    """
    def __init__(self, image_path):
        self.image_path  = image_path

    def load(self):
        return Image.open(self.image_path)