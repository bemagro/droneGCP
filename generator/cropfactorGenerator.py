from .generator import Generator

class CropfactorGenerator(Generator):
    """
    CropfactorGenerator based on images settings generates the crop
    factor ratio, to further calculate the GSD of an image

    Arguments
    equivalent_focal_length - float, equivalent 35mm focal len
    focal_length - float, focal length
    """
    def __init__(self, equivalent_focal_length, focal_length):
        self.equivalent_focal_length = equivalent_focal_length
        self.focal_length = focal_length
    
    def generate(self):
        return self.equivalent_focal_length / self.focal_length
