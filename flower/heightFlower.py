from .flower import Flower

import sys
sys.path.insert(0, r"C:\Users\dougl\Desktop\FELIPE\dronePRI")

from loader import *
from metaProcessor import *

class HeightFlower(Flower):
    """
    HeightFlower Takes the necessary arguments for flowing the
    height identifier.

    Arguments
    jpgs_list - list, contains the path for all images

    """
    
    def __init__(self,
                jpgs_list,
                gcp_dataframe):

        self.jpgs_list = jpgs_list
        self.gcp_dataframe = gcp_dataframe
    
    def flow(self):
        tallest = 0
        smallest = 999

        for jpg in self.jpgs_list:
            # load image
            alt = MetaAltitudeProcessor(jpg).process()
            if alt > tallest:
                tallest = alt

        for alt in self.gcp_dataframe["altitude"]:
            if alt < smallest:
                smallest = alt
        
        return tallest - smallest