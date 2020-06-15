from flower import *
from loader import *
from glob import glob

import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # base directory argument
    parser.add_argument("base_dir", help="Defines the name of the property")

    # csv name argument
    parser.add_argument("--csv_name", type=str, default='gcp_csv.csv', 
                            help="Csv filename")
    # parses all arguments to an object
    args = parser.parse_args()
    CSV = os.path.join(args.base_dir, args.csv_name)
    JPG_DIR = os.path.join(args.base_dir,'*.jpg')
    
    # identifies working files
    jpgs = glob(JPG_DIR)
    if not len(jpgs) > 1:
        raise Exception('No images found, please correct file path')
    
    # before loop lock and load
    gcp_csv = GcpCsvLoader(CSV).load()
    gcp_json = EmptyGcpJsonLoader(gcp_csv).load()

    # gets flight height
    height = HeightFlower(jpgs, gcp_csv).flow()

    # execute main logic
    gcp_json = GcpJsonFlower(jpgs, gcp_csv, gcp_json, height).flow()