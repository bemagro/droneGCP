from .loader import Loader
import pandas as pd

L2 = ['latitude', 'longitude', 'altitude', 'label']

class GcpCsvLoader(Loader):
    """
    GcpCsvLoader

    Interface for loading the csv containing coordinates for the
    ground control points
    """
    def __init__(self, csv_path):
        self.dataframe = pd.read_csv(csv_path)

        if not self.check_equal(self.dataframe.columns):
          raise Exception('wrong columns at {}'.format(csv_path))

    def check_equal(self, columns):
        return len(columns) == len(L2) and sorted(columns) == sorted(L2)

    def load(self):
        return self.dataframe