from .flower import Flower

import sys
sys.path.insert(0, r"C:\Users\dougl\Desktop\FELIPE\dronePRI")

from loader import *
from metaProcessor import *
from generator import *
import utm

class GcpJsonFlower(Flower):
    """
    Takes the necessary arguments for flowing the
    json filler

    Arguments
    jpgs_list - list, contains the path for all images

    """
    
    def __init__(self,
                jpgs_list,
                gcp_dataframe,
                gcp_json,
                height, 
                correction_ratio = 0.5):

        self.jpgs_list = jpgs_list
        self.height = height
        self.gcp_dataframe = gcp_dataframe
        self.gcp_json = gcp_json
        self.correction_ratio = 1 + correction_ratio
    
    def flow(self):
        for jpg in self.jpgs_list:
            # load image
            # get image settings
            img = PillowLoader(jpg).load()
            img_height = img.height
            img_width = img.width

            # extract meta data
            focal_length = MetaFocalProcessor(jpg).process()
            adj_focal_length = MetaAdjFocalProcessor(jpg).process()
            crop_factor=  CropfactorGenerator(adj_focal_length, focal_length).generate()
            sensor_width = SensorWidthGenerator(crop_factor, img_width, img_height).generate()
            pixel_resolution = GsdGenerator(sensor_width, focal_length, self.height, img.width).generate()
            lat, lon = MetaCoordProcessor(jpg).process()

            # hardcode
            lat = -lat; lon = -lon
            x, y, sig, let = utm.from_latlon(lat, lon)

            # check which will be used for calculating threshold
            if img_height > img_width:
                greater_size= (img_height * pixel_resolution / 100) / 2
            else:
                greater_size = (img_width * pixel_resolution / 100) / 2 
            greater_size = float(self.correction_ratio) * greater_size
            
            # slice dataframe for points between threshold
            df_slice = self.gcp_dataframe[
                    (self.gcp_dataframe['longitude'] < x + greater_size) & \
                    (self.gcp_dataframe['longitude'] > x - greater_size) & \
                    (self.gcp_dataframe['latitude'] > y - greater_size) & \
                    (self.gcp_dataframe['latitude'] < y + greater_size)]
            
            # if image contains a gcp
            if len(df_slice) > 0:
                for label in df_slice['label']:
                    self.gcp_json[str(label)].append(jpg)

        return self.gcp_json